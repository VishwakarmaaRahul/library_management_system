select * from Libraries; 
select * from books ;
select * from categories;
select * from borrowing;
select * from members;
select * from reviews;
select * from authors;  
select * from bookauthor;
select * from bookcategory;


-- Book with their author and categories

select bk.book_id, bk.title,ba.author_id,CONCAT(a.first_name,' ', a.last_name) as AuthorName, bc.category_id ,c.category 
from  books bk 
left join bookauthor ba  on bk.book_id = ba.book_id 
left join authors a on ba.author_id = a.author_id
left join BookCategory bc on bc.book_id = bk.book_id
left join categories c on c.category_id = bc.category_id  ;


-- Most borrowd books in the last 30 days

select b.book_id ,b.title
from books b 
join borrowing br 
on b.book_id = br.book_id 
where br.borrow_date  >= CURRENT_DATE - INTERVAL 30 DAY;

-- Members with overdue books and calculated late fees

SELECT 
    m.member_id,
    CONCAT( m.first_name,' ',  m.last_name)as MemberName,
    bk.book_id,
    bk.title,
    br.due_date,
    DATEDIFF(CURDATE(), br.due_date) AS days_overdue,
    ROUND(DATEDIFF(CURDATE(), br.due_date) * 1.50, 2) AS calculated_late_fee
FROM Borrowing br
JOIN Members m ON br.member_id = m.member_id
JOIN Books bk ON br.book_id = bk.book_id
WHERE br.return_date IS NULL
  AND br.due_date < CURDATE();



-- Average rating per book with author information

select bk.book_id, bk.title,ba.author_id,CONCAT(a.first_name,' ', a.last_name) as AuthorName, 
a.birth_date ,a.nationality ,a.biography  ,AVG(r.rating) as "Average Rating"  
from  books bk 
left join bookauthor ba on bk.book_id = ba.book_id 
left join authors a on ba.author_id = a.author_id
join reviews r on bk.book_id = r.book_id
group by bk.book_id, bk.title,ba.author_id,a.first_name, a.last_name,a.birth_date ,a.nationality ,a.biography,r.rating
order by AVG(r.rating)  desc;


-- Books available in each library with stock levels

SELECT 
    b.book_id,
    b.title,
    b.isbn,
    b.publication_date,
    b.available_copies,
    l.library_id,
    l.library_name
FROM 
    books b
JOIN 
    libraries l ON b.library_id = l.library_id;



-- Window function (Rank books by average rating (within each library))


SELECT 
    l.library_name,
    b.title,
    ROUND(AVG(r.rating), 2) AS avg_rating,
    RANK() OVER (PARTITION BY l.library_id ORDER BY AVG(r.rating) DESC) AS rating_rank
FROM 
    Books b
JOIN 
    Libraries l ON b.library_id = l.library_id
JOIN 
    Reviews r ON b.book_id = r.book_id
GROUP BY 
    l.library_id, l.library_name, b.book_id, b.title;


-- Dense Rank

SELECT 
    l.library_name,
    b.title,
    ROUND(AVG(r.rating), 2) AS avg_rating,
    DENSE_RANK() OVER (PARTITION BY l.library_id ORDER BY AVG(r.rating) DESC) AS rating_rank
FROM 
    Books b
JOIN 
    Libraries l ON b.library_id = l.library_id
JOIN 
    Reviews r ON b.book_id = r.book_id
GROUP BY 
    l.library_id, l.library_name, b.book_id, b.title;



-- find how many books each member has borrowed

WITH BorrowCount AS (
    SELECT 
        member_id,
        COUNT(*) AS total_borrowed
    FROM 
        Borrowing
    GROUP BY 
        member_id
)
SELECT 
    m.member_id,
    CONCAT(m.first_name, ' ', m.last_name) AS member_name,
    bc.total_borrowed
FROM 
    Members m
JOIN 
    BorrowCount bc ON m.member_id = bc.member_id
ORDER BY 
    total_borrowed DESC;



-- Find members who have borrowed books but never returned any

SELECT member_id, CONCAT(first_name,' ', last_name)as MemberName
FROM Members
WHERE member_id IN (
    SELECT DISTINCT member_id
    FROM Borrowing
    WHERE return_date IS NULL
);


-- List books with their total borrow count

WITH BookBorrowCount AS (
    SELECT book_id, COUNT(*) AS borrow_count
    FROM Borrowing
    GROUP BY book_id
)
SELECT b.title, b.book_id, COALESCE(bc.borrow_count, 0) AS borrow_count
FROM Books b
LEFT JOIN BookBorrowCount bc ON b.book_id = bc.book_id
ORDER BY borrow_count DESC;


START TRANSACTION;

SELECT available_copies 
FROM Books 
WHERE book_id = 3 FOR UPDATE;

INSERT INTO Borrowing (
    borrowing_id, member_id, book_id, borrow_date, due_date
) VALUES (
    26, 4, 3, CURDATE(), DATE_ADD(CURDATE(), INTERVAL 14 DAY)
);

UPDATE Books
SET available_copies = available_copies - 2
WHERE book_id = 3;

rollback;

COMMIT;

select * from borrowing;

START TRANSACTION;

-- Update return date
UPDATE Borrowing
SET return_date = CURDATE()
WHERE borrowing_id = 2;

-- Apply late fee if overdue (assume Rs. 1.50/day)
UPDATE Borrowing
SET late_fee = DATEDIFF(CURDATE(), due_date) * 1.50
WHERE borrowing_id = 2 AND CURDATE() > due_date;

-- Restore book copy
UPDATE Books
SET available_copies = available_copies + 1
WHERE book_id = (SELECT book_id FROM Borrowing WHERE borrowing_id = 3);

rollback;

COMMIT;

select * from borrowing;
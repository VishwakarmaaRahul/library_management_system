INSERT INTO Libraries (library_id, library_name, campus_location, contact_email, phone_number)
VALUES
(1, 'Central Library', 'Main Campus', 'central@university.edu', '1234567890'),
(2, 'Science Library', 'North Campus', 'science@university.edu', '1234567891'),
(3, 'Law Library', 'South Campus', 'law@university.edu', '1234567892');


INSERT INTO Books (book_id, title, isbn, publication_date, total_copies, available_copies, library_id)
VALUES
(1, 'Introduction to Algorithms', '9780262033848', '2009-07-31', 5, 5, 1),
(2, 'Clean Code', '9780132350884', '2008-08-01', 3, 3, 1),
(3, 'Design Patterns', '9780201633610', '1994-10-21', 4, 4, 1),
(4, 'A Brief History of Time', '9780553380163', '1998-09-01', 2, 2, 2),
(5, 'The Selfish Gene', '9780192860927', '1989-08-01', 3, 3, 2),
(6, 'The Origin of Species', '9781509827695', '1859-11-24', 1, 1, 2),
(7, 'Constitutional Law', '9780198765865', '2015-05-01', 2, 2, 3),
(8, 'Criminal Law', '9780198852695', '2019-06-01', 2, 2, 3),
(9, 'Law and Society', '9780130253264', '2002-03-01', 3, 3, 3),
(10, 'Artificial Intelligence', '9780136042597', '2009-02-01', 4, 4, 1),
(11, 'Database Systems', '9780133970770', '2015-01-01', 5, 5, 1),
(12, 'Machine Learning', '9781107057135', '2014-03-10', 3, 3, 1),
(13, 'Physics for Scientists', '9780321993724', '2013-01-01', 4, 4, 2),
(14, 'Organic Chemistry', '9780321803222', '2013-01-01', 2, 2, 2),
(15, 'Environmental Law', '9780199577515', '2011-04-01', 2, 2, 3);


INSERT INTO Authors (author_id, first_name, last_name, birth_date, nationality, biography)
VALUES
(1, 'Thomas', 'Cormen', '1956-01-01', 'American', 'Co-author of Introduction to Algorithms'),
(2, 'Robert', 'Martin', '1952-12-05', 'American', 'Known for Clean Code'),
(3, 'Erich', 'Gamma', '1961-03-13', 'Swiss', 'Co-author of Design Patterns'),
(4, 'Stephen', 'Hawking', '1942-01-08', 'British', 'Author of A Brief History of Time'),
(5, 'Richard', 'Dawkins', '1941-03-26', 'British', 'Author of The Selfish Gene'),
(6, 'Charles', 'Darwin', '1809-02-12', 'British', 'Father of evolutionary biology'),
(7, 'John', 'Smith', '1975-06-10', 'American', 'Expert in constitutional law'),
(8, 'Jane', 'Doe', '1980-04-25', 'Canadian', 'Environmentalist and author');


INSERT INTO Categories (category_id, category, descriptions)
VALUES
(1, 'Computer Science', 'Books on computer science and programming'),
(2, 'Physics', 'Books on physical sciences and theories'),
(3, 'Biology', 'Books related to living organisms'),
(4, 'Law', 'Legal textbooks and case studies'),
(5, 'Environment', 'Books focused on environmental issues');


INSERT INTO Members (member_id, first_name, last_name, email, phone_number, member_type, registration_date)
VALUES
(1, 'Alice', 'Wong', 'alice1@example.com', '9000000001', 'student', '2024-01-15'),
(2, 'Bob', 'Lee', 'bob2@example.com', '9000000002', 'faculty', '2023-09-20'),
(3, 'Carla', 'Smith', 'carla3@example.com', '9000000003', 'student', '2024-02-10'),
(4, 'David', 'Chan', 'david4@example.com', '9000000004', 'faculty', '2022-11-18'),
(5, 'Eva', 'Patel', 'eva5@example.com', '9000000005', 'student', '2024-03-12'),
(6, 'Frank', 'Yu', 'frank6@example.com', '9000000006', 'faculty', '2023-06-23'),
(7, 'Grace', 'Kim', 'grace7@example.com', '9000000007', 'student', '2024-04-09'),
(8, 'Henry', 'Nguyen', 'henry8@example.com', '9000000008', 'faculty', '2022-12-05'),
(9, 'Ivy', 'Brown', 'ivy9@example.com', '9000000009', 'student', '2024-05-07'),
(10, 'Jack', 'Wilson', 'jack10@example.com', '9000000010', 'faculty', '2023-08-11'),
(11, 'Karen', 'Lopez', 'karen11@example.com', '9000000011', 'student', '2024-06-21'),
(12, 'Leo', 'Perez', 'leo12@example.com', '9000000012', 'faculty', '2022-10-04'),
(13, 'Mona', 'White', 'mona13@example.com', '9000000013', 'student', '2024-07-15'),
(14, 'Nate', 'King', 'nate14@example.com', '9000000014', 'faculty', '2023-05-29'),
(15, 'Olivia', 'Martinez', 'olivia15@example.com', '9000000015', 'student', '2024-01-03'),
(16, 'Paul', 'Walker', 'paul16@example.com', '9000000016', 'faculty', '2023-02-22'),
(17, 'Queenie', 'Hall', 'queenie17@example.com', '9000000017', 'student', '2024-03-30'),
(18, 'Ryan', 'Scott', 'ryan18@example.com', '9000000018', 'faculty', '2023-01-17'),
(19, 'Sophia', 'Adams', 'sophia19@example.com', '9000000019', 'student', '2024-04-25'),
(20, 'Tom', 'Bennett', 'tom20@example.com', '9000000020', 'faculty', '2022-09-09');


INSERT INTO Borrowing (borrowing_id, member_id, book_id, borrow_date, due_date, return_date, late_fee)
VALUES
(1, 1, 1, '2025-07-01', '2025-07-15', '2025-07-14', 0.00),
(2, 2, 2, '2025-07-01', '2025-07-15', NULL, NULL),
(3, 3, 3, '2025-06-10', '2025-06-24', '2025-06-26', 1.50),
(4, 4, 4, '2025-06-05', '2025-06-19', '2025-06-20', 0.50),
(5, 5, 5, '2025-07-10', '2025-07-24', NULL, NULL),
(6, 6, 6, '2025-06-15', '2025-06-29', '2025-07-01', 2.00),
(7, 7, 7, '2025-07-05', '2025-07-19', '2025-07-19', 0.00),
(8, 8, 8, '2025-06-20', '2025-07-04', '2025-07-03', 0.00),
(9, 9, 9, '2025-07-11', '2025-07-25', NULL, NULL),
(10, 10, 10, '2025-07-01', '2025-07-15', '2025-07-16', 1.00),
(11, 11, 11, '2025-07-03', '2025-07-17', NULL, NULL),
(12, 12, 12, '2025-06-22', '2025-07-06', '2025-07-08', 1.50),
(13, 13, 13, '2025-06-25', '2025-07-09', '2025-07-09', 0.00),
(14, 14, 14, '2025-07-02', '2025-07-16', '2025-07-18', 1.00),
(15, 15, 15, '2025-07-06', '2025-07-20', NULL, NULL),
(16, 16, 1, '2025-06-10', '2025-06-24', '2025-06-23', 0.00),
(17, 17, 2, '2025-07-01', '2025-07-15', '2025-07-20', 2.50),
(18, 18, 3, '2025-06-30', '2025-07-14', NULL, NULL),
(19, 19, 4, '2025-07-08', '2025-07-22', '2025-07-22', 0.00),
(20, 20, 5, '2025-07-10', '2025-07-24', NULL, NULL),
(21, 1, 6, '2025-06-01', '2025-06-15', '2025-06-20', 2.50),
(22, 2, 7, '2025-06-20', '2025-07-04', '2025-07-06', 1.00),
(23, 3, 8, '2025-07-05', '2025-07-19', NULL, NULL),
(24, 4, 9, '2025-07-07', '2025-07-21', '2025-07-22', 0.50),
(25, 20, 15, '2025-07-20', '2025-08-03', NULL, NULL);

INSERT INTO Reviews (review_id, member_id, book_id, rating, comments, review_date)
VALUES
(1, 1, 1, 5, 'Excellent reference book.', '2025-07-15'),
(2, 2, 2, 4, 'Very useful for clean code practices.', '2025-07-16'),
(3, 3, 3, 5, 'Design patterns are clearly explained.', '2025-07-17'),
(4, 4, 4, 4, 'Insightful book on the universe.', '2025-07-18'),
(5, 5, 5, 3, 'Interesting but a bit dense.', '2025-07-18'),
(6, 6, 6, 4, 'Classic and still relevant.', '2025-07-19'),
(7, 7, 7, 4, 'Covers the basics well.', '2025-07-19'),
(8, 8, 8, 3, 'Good overview of criminal law.', '2025-07-20'),
(9, 9, 9, 4, 'Useful for law and society studies.', '2025-07-20'),
(10, 10, 10, 5, 'Very informative and modern.', '2025-07-21'),
(11, 11, 11, 4, 'Detailed and clear explanations.', '2025-07-22'),
(12, 12, 12, 5, 'Best ML book.', '2025-07-23');


INSERT INTO BookAuthor (book_id, author_id)
VALUES
(1, 1),
(2, 2),
(3, 3),
(4, 4),
(5, 5),
(6, 6),
(7, 7),
(8, 7),
(9, 7),
(10, 1);


INSERT INTO BookCategory (book_id, category_id)
VALUES
(1, 1),   
(2, 1),
(3, 1),
(4, 2),  
(5, 3),   
(6, 3),
(7, 4),   
(8, 4),
(9, 4),
(15, 5);
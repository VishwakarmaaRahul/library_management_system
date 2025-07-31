CREATE DATABASE libraryDB;



CREATE TABLE Libraries(
    library_id INT PRIMARY KEY,
    library_name VARCHAR(50) NOT NULL,
    campus_location VARCHAR(50),
    contact_email VARCHAR(50) UNIQUE,
    phone_number VARCHAR(15) UNIQUE,
	createdAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);


CREATE TABLE Books   (
    book_id INT PRIMARY KEY,
    title VARCHAR(50) NOT NULL,
    isbn VARCHAR(20) UNIQUE,
    publication_date DATE,
    total_copies INT DEFAULT 1,
    available_copies INT DEFAULT 1,
    library_id INT,
	createdAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (library_id) REFERENCES Libraries(library_id)
);

CREATE TABLE Authors   (
    author_id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    birth_date DATE,
    nationality VARCHAR(50),
    biography TEXT,
	createdAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);


CREATE TABLE Categories   (
    category_id INT PRIMARY KEY,
    category  VARCHAR(50),
    descriptions TEXT,
	createdAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE Members    (
    member_id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(50) UNIQUE,
    phone_number VARCHAR(15) UNIQUE,
    member_type VARCHAR(20),
    registration_date DATE,
    CHECK (member_type IN ('student', 'faculty')),
    createdAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
    
);


CREATE TABLE Borrowing    (
    borrowing_id INT PRIMARY KEY,
    member_id INT,
    book_id INT,
    borrow_date DATE NOT NULL,
    due_date DATE NOT NULL,
    return_date DATE,
    late_fee DECIMAL(6,2),
    createdAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (member_id) REFERENCES Members(member_id),
    FOREIGN KEY (book_id) REFERENCES Books(book_id)  
);


CREATE TABLE Reviews (
    review_id INT PRIMARY KEY,
    member_id INT,
    book_id INT,
    rating INT CHECK (rating BETWEEN 1 AND 5),
    comments TEXT,
    review_date DATE,
    createdAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (member_id) REFERENCES Members(member_id),
    FOREIGN KEY (book_id) REFERENCES Books(book_id),
    UNIQUE (member_id, book_id) 
);

CREATE TABLE BookAuthor (
    book_id INT,
    author_id INT,
    FOREIGN KEY (author_id) REFERENCES Authors(author_id),
    FOREIGN KEY (book_id) REFERENCES Books(book_id),
    PRIMARY KEY (book_id, author_id)  
);


CREATE TABLE BookCategory (
    book_id INT,
    category_id INT,
    FOREIGN KEY (category_id) REFERENCES Categories(category_id),
    FOREIGN KEY (book_id) REFERENCES Books(book_id),
    PRIMARY KEY (book_id, category_id)
);








-- CREATE TABLE Libraries(
--     library_id INT primary key ,
--     library_name VARCHAR(50) not null ,
--     campus_location VARCHAR(50) not null ,
--     contact_email VARCHAR(50) unique not null  ,
--     phone_number VARCHAR(15) unique ,
-- 	createdAt TIMESTAMP default  CURRENT_TIMESTAMP,
--     updatedAt TIMESTAMP default	 CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
-- );


-- CREATE TABLE Books   (
--     book_id INT PRIMARY KEY,
--     title VARCHAR(50) NOT NULL,
--     isbn VARCHAR(20) unique not null ,
--     publication_date DATE not null ,
--     total_copies INT DEFAULT 1 not null ,
--     available_copies INT DEFAULT 1,
--     library_id INT not null ,
-- 	createdAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
--     updatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
--     FOREIGN KEY (library_id) REFERENCES Libraries(library_id)
-- );

-- CREATE TABLE Authors   (
--     author_id INT PRIMARY KEY,
--     first_name VARCHAR(50) not null ,
--     last_name VARCHAR(50) not null ,
--     birth_date DATE,
--     nationality VARCHAR(50),
--     biography TEXT,
-- 	createdAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
--     updatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
-- );


-- CREATE TABLE Categories   (
--     category_id INT PRIMARY KEY,
--     category  VARCHAR(50) not null ,
--     descriptions TEXT,
-- 	createdAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
--     updatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
-- );



-- CREATE TABLE Members    (
--     member_id INT PRIMARY KEY,
--     first_name VARCHAR(50) not null ,
--     last_name VARCHAR(50) not null , 
--     email VARCHAR(50) unique not null ,
--     phone_number VARCHAR(15) UNIQUE,
--     member_type VARCHAR(20) not null ,
--     registration_date DATE,
--     CHECK (member_type IN ('student', 'faculty')),
--     createdAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
--     updatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
--     
-- );


-- CREATE TABLE Borrowing    (
--     borrowing_id INT PRIMARY KEY,
--     member_id INT not null ,
--     book_id INT not null ,
--     borrow_date DATE NOT NULL,
--     due_date DATE NOT NULL,
--     return_date DATE,
--     late_fee DECIMAL(6,2),
--     createdAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
--     updatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
--     FOREIGN KEY (member_id) REFERENCES Members(member_id),
--     FOREIGN KEY (book_id) REFERENCES Books(book_id)  
-- );


-- CREATE TABLE Reviews (
--     review_id INT PRIMARY KEY,
--     member_id INT not null ,
--     book_id INT not null ,
--     rating INT CHECK (rating BETWEEN 1 AND 5) not null ,
--     comments TEXT,
--     review_date DATE,
--     createdAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
--     updatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
--     FOREIGN KEY (member_id) REFERENCES Members(member_id),
--     FOREIGN KEY (book_id) REFERENCES Books(book_id),
--     UNIQUE (member_id, book_id) 
-- );

-- CREATE TABLE BookAuthor (
--     book_id INT,
--     author_id INT,
--     FOREIGN KEY (author_id) REFERENCES Authors(author_id),
--     FOREIGN KEY (book_id) REFERENCES Books(book_id),
--     PRIMARY KEY (book_id, author_id)  
-- );


-- CREATE TABLE BookCategory (
--     book_id INT,
--     category_id INT,
--     FOREIGN KEY (category_id) REFERENCES Categories(category_id),
--     FOREIGN KEY (book_id) REFERENCES Books(book_id),
--     PRIMARY KEY (book_id, category_id)
-- );






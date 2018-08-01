CREATE TABLE 'departments' (
    'id' INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    'name' TEXT NOT NULL,
    'budget' INTEGER NOT NULL
);

INSERT INTO departments VALUES (null, 'Information Technology', 15000)
INSERT INTO departments VALUES (null, 'Human Resources', 5000)
INSERT INTO departments VALUES (null, 'Research and Development', 25000)
INSERT INTO departments VALUES (null, 'Accounting', 5000)



CREATE TABLE 'employees' (
    'id' INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    'name' TEXT NOT NULL,
    'title' TEXT NOT NULL,
    'supervisor' BOOLEAN,
    'department_id' TEXT
    FOREIGN KEY('department_id') REFERENCES 'department'('id')
);


INSERT INTO employees VALUES (null, 'Steve Jobs', 'IT Director', 1, 0)
INSERT INTO employees VALUES (null, 'Bill Gates', 'IT Support 1', 0, 0)
INSERT INTO employees VALUES (null, 'Bill Gates', 'IT Support 2', 0, 0)

INSERT INTO employees VALUES (null, 'Justin Timberlake', 'HR Director', 1, 1)
INSERT INTO employees VALUES (null, 'Steve Brownlee', 'HR Associate 1', 0, 1)
INSERT INTO employees VALUES (null, 'Riley Mathews', 'HR Associate 2', 0, 1)

INSERT INTO employees VALUES (null, 'Joe Shepherd', 'R&D Lead', 1, 2)
INSERT INTO employees VALUES (null, 'Kimmy Bird', 'Engineer', 0, 2)
INSERT INTO employees VALUES (null, 'Greg Korte', 'Scientist', 0, 2)

INSERT INTO employees VALUES (null, 'Warren Buffet', 'Head Accountant', 1, 3)
INSERT INTO employees VALUES (null, 'Warren Buffet', 'Accountant', 0, 3)
INSERT INTO employees VALUES (null, 'Warren Buffet', 'Accounts Payable', 0, 3)


CREATE TABLE 'computers' (
    'id' INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    'model_name' TEXT NOT NULL,
    'purchase_date' TEXT,
    'decomm-date' TEXT
);

INSERT INTO computers VALUES (null, 'Macbook Pro 1', date())
INSERT INTO computers VALUES (null, 'Macbook Pro 2', date())
INSERT INTO computers VALUES (null, 'Macbook Pro 3', date())
INSERT INTO computers VALUES (null, 'Macbook Pro 4', date())
INSERT INTO computers VALUES (null, 'Macbook Pro 5', '2012-06-01', date())

CREATE TABLE 'trainings' (
    'id' INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    'program_name' TEXT NOT NULL,
    'start_date' TEXT,
    'end_date' TEXT,
    'max_capacity' INTEGER NOT NULL
);

INSERT INTO trainings VALUES (null, 'Onboarding: Our Tech Stack', '2018-08-15', '2018-08-15', 15)
INSERT INTO trainings VALUES (null, 'Onboarding: Our Tech Stack', '2018-08-16', '2018-08-16', 15)
INSERT INTO trainings VALUES (null, 'Teamwork: Sprinting', null, null, 8)
INSERT INTO trainings VALUES (null, 'Onboarding: Our Tech Stack', '2018-08-18', '2018-08-18', 15)

CREATE TABLE 'customers' (
    'id' INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    'first_name' TEXT NOT NULL,
    'last_name' TEXT NOT NULL,
    'acct_created' TEXT NOT NULL,
    '240_active' BOOLEAN
);

INSERT INTO customers VALUES (null, 'Bobby', 'Boucher', date(), 0)
INSERT INTO customers VALUES (null, 'Caroline', 'Caruthers', date(), 1)
INSERT INTO customers VALUES (null, 'David', 'Duke', date(), 1)

CREATE TABLE 'product_type' (
    'id' INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    'category' TEXT NOT NULL
);

INSERT INTO product_type VALUES (null, 'Technology')
INSERT INTO product_type VALUES (null, 'Music')
INSERT INTO product_type VALUES (null, 'Fashion')
INSERT INTO product_type VALUES (null, 'Outdoors')
INSERT INTO product_type VALUES (null, 'Sports')

CREATE TABLE 'products' (
    'id' INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    'title' TEXT NOT NULL,
    'price' INTEGER NOT NULL,
    'description' TEXT,
    'customer_id' INTEGER NOT NULL,
    'product_type_id' INTEGER NOT NULL,
    FOREIGN KEY('customer_id') REFERENCES 'customers'('id'),
    FOREIGN KEY('product_type_id') REFERENCES 'product_type'('id')
);

INSERT INTO products VALUES (null, 'Iphone X', 1000, 'The most versatile phone to date', 0)
INSERT INTO products VALUES (null, 'Organic Dog Food', 50, 'The most versatile dog food to date', 1)
INSERT INTO products VALUES (null, 'Lawn chairs', 1000, 'The most versatile lawn chairs to date', 2)

CREATE TABLE 'payment_type' (
    'id' INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    'name' TEXT NOT NULL
);

INSERT INTO payment_type VALUES (null, 'Visa',)


CREATE TABLE 'payment-customers' (
    'id' INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    'customer_id' INTEGER NOT NULL,
    'payment_id' INTEGER NOT NULL,
    FOREIGN KEY('customer_id') REFERENCES 'customers'('id'),
    FOREIGN KEY('payment_id') REFERENCES 'payment'
);
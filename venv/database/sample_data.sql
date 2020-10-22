DELETE FROM addresses;
DELETE FROM users;

INSERT INTO users(first_name, last_name) VALUES ('Asad', 'Akul')
INSERT INTO users(first_name, last_name) VALUES ('Tailer', 'Swift')


INSERT INTO addresses(user_id, email, address) VALUES (1, 'a@gmail.com','BD')
INSERT INTO addresses(user_id, email, address) VALUES (2, 't@gmail.com','USA')

SELECT first_name, last_name FROM users WHERE last_name LIKE 'M%';

SELECT u.last_name as last_name,
        a.email as email, a.address as address
FROM users AS u
LEFT JOIN addresses as a
WHERE u.id=a.user_id AND u.last_name LIKE 'M%';

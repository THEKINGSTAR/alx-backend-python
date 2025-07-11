-- Active: 1751719636449@@127.0.0.1@3306@ALX_prodev
DROP DATABASE IF EXISTS ALX_prodev;

CREATE DATABASE ALX_prodev;

-- Active: 1751719636449@@
USE DATABASE ALX_prodev;

CREATE TABLE
    user_data (
        user_id CHAR(36) PRIMARY KEY,
        name VARCHAR(50) NOT NULL,
        email VARCHAR(50) NOT NULL,
        age DECIMAL NOT NULL
    );

CREATE INDEX idx_user_id ON user_data(user_id);


SELECT * FROM user_data;
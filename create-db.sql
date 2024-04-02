CREATE DATABASE bookcollector;

CREATE USER book_collector_admin WITH PASSWORD 'password';

GRANT ALL PRIVILEGES ON DATABASE bookcollector TO bookcollector_admin;


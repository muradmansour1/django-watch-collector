CREATE DATABASE watchcollector;

CREATE USER watch_admin WITH PASSWORD 'password';

GRANT ALL PRIVILEGES ON DATABASE watchcollector TO watch_admin;


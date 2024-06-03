CREATE DATABASE IF NOT EXISTS go;

USE go;

CREATE TABLE IF NOT EXISTS go.Users (
    User_id UInt64,
    User_tg_id UInt64,
    User_registration_date DateTime,
    User_type bool,
    User_close_tasks UInt32,
    User_open_tasks UInt32,
    User_rating Float32
) ENGINE = MergeTree()
ORDER BY User_id
PRIMARY KEY User_id;;

CREATE TABLE IF NOT EXISTS go.Tasks (
    Task_id UInt64,
    Task_owner_id UInt64,
    Task_creation_datetime DateTime,
    Task_name String,
    Task_description String,
    Task_address Point,
    Task_datetime DateTime,
    Task_time_range UInt8,
    Task_full_price UInt16,
    Task_hour_price UInt16,
    Task_minimal_price_rate UInt8,
    Task_people_count UInt8,
    Task_urgent Bool,
    Task_day_night Bool
) ENGINE = MergeTree()
ORDER BY Task_id
PRIMARY KEY Task_id;

CREATE TABLE IF NOT EXISTS go.Journal (
    Journal_user_id UInt64,
    Journal_task_id UInt64
) ENGINE = MergeTree()
ORDER BY (Journal_user_id, Journal_task_id);
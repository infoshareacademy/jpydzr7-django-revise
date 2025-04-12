CREATE DATABASE django_rest_tutorial_infoshare;
CREATE TABLE django_rest_tutorial_infoshare.user
(
    id         int auto_increment primary key,
    username   varchar(100),
    first_name varchar(100),
    last_name  varchar(100),
    email      varchar(100),
    password   varchar(100),
    created_at datetime
);
CREATE TABLE django_rest_tutorial_infoshare.password_data
(
    id           int auto_increment primary key,
    user_id      int,
    service_name varchar(100),
    username     varchar(100),
    email        varchar(100),
    password     varchar(100),
    created_at   DATETIME,
    constraint user_id_foreign_key foreign key (user_id) references django_rest_tutorial_infoshare.user (id)
)
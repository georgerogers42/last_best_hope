CREATE TABLE pages(id serial primary key, slug varchar(127) not null unique, title varchar(255) not null, contents text not null, ctime timestamp with time zone not null default now(), utime timestamp with time zone not null default now());

CREATE TABLE movie (
id serial primary key,
title varchar(250) not null check (length(title)>0),
tagline varchar(250) not null check (length(tagline)>0),
summary text not null check (length(summary)>0),
release_year int not null,
genre_id integer references genre(id)
);

CREATE TABLE genre (
id serial primary key,
name varchar(250) not null check (length(name)>0)
);

CREATE TABLE people (
id serial primary key,
name varchar(250) not null check (length(name)>0),
birth_day date
);

CREATE TABLE people_movie (
id_people integer references movi(id),
id_movie integer references people(id),
character varchar(250) not null,
);

INSERT INTO movie (title, tagline, summary, release_year) 
VALUES
('Troy', 'For Troy', 'Its testing Troy', 2004),
('Rembo', 'First Blood', 'Its testing Rembo', 1997),
('Meg', 'Big Shark', 'Its testing Meg', 2019),
('Lord of the rings', 'My ring', 'Its testing Owner rings', 2001),
('Harry Potter', 'Reducto', 'Its testing Garry', 2002,);

INSERT INTO genre (name) 
VALUES
('Action movie'),
('Historical'),
('Fantastic'),
('Adventure');

INSERT INTO people (name, birth_day) 
VALUES
('STALONE', 1938-02-12),
('PITT', 1963-04-06),
('JASON', 1970-03-01),
('DANIEL', 1991-02-09),
('WOOD', 1982-01-08);

INSERT INTO people_movie (people_id, movie_id, character) 
VALUES
(1, 3, 'REMBO'),
(2, 2, 'AHIL'),
(3, 4, 'SHARK_D'),
(4, 6, 'GARRY'),
(5, 5, 'FRODO');




## Shell Commands for PSQL

>To show version:`SELECT version();`
>
>To Get time: `SELECT now();`

>### Create a database: `CREATE DATABASE favoritecolors;` 
>
>favoritecolors is the name of the database
>
>To List all Databases: `\l`
>
>To switch database: `\c favoritecolors`
>
>Create a table: `CREATE TABLE colors(ColorID int, ColorName char(20));`
>
>Store data into the DB: `INSERT INTO colors VALUES (1, 'red'), (2,'green'), (3, 'blue');`
>
> Display stored data: `SELECT * FROM colors;`
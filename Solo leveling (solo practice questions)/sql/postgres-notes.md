# On the SQL Shell
The SQL shell comes preinstalled with PgAdmin app
YOu might need to initially enter the password that you have set for your database
```sql
\l # This gives list of available database
```

To create a new database

```sql
create database <name-of-database>
```

# On the PgAdmin app
PgAdmin comes preinstalled along with Postgres. 
In this app select servers > PostgresSQL 15 > Databases > `<name-of-database>` 

Say if `<name-of-database>`  is `sql-demo` then, right click on it and select query-tool to open up the code editor

Here if you need to execute the code then select f5, by default all codes will be executed but if you only want to execute selected number of commands then you have to first select the desired code and then hit f5



# make a new table

First let's make a new table in this database

TO do so we enter the following 

```sql
CREATE TABLE table_name(column_name datatype, column_name datatype, ...)

```
This code creates a new database file when you run it. If you try to run it again, you'll get an error because the table already exists. If you want to run it multiple times, you need to add a check to see if the table already exists before creating it.

This is how it's done

```sql

	DROP TABLE IF EXISTS table_name;
	CREATE TABLE table_name (column_name datatype, column_name datatype, ...);

```

## To insert values
```sql
INSERT INTO example_table(column_name, column_name, column_name) VALUES (value1, value2, value3)
```

## To retrive data
```sql
SELECT column_name1, column_name2, ... FROM table_name
```
__`* means to select all columns`__


## To Update Data

```sql
UPDATE table_name SET column_name = desired value WHERE column_name = initial/unique value
```

for example 
<table>
  <tr>
    <th>id</th>
    <th>Names</th>
    <th>Occupations</th>
  </tr>
  <tr>
    <td>1</td>
    <td>John Doe</td>
    <td>Engineer</td>
  </tr>
  <tr>
    <td>2</td>
    <td>Jane Smith</td>
    <td>Teacher</td>
  </tr>
  <tr>
    <td>3</td>
    <td>Michael Johnson</td>
    <td>Doctor</td>
  </tr>
  <tr>
    <td>4</td>
    <td>Sarah Williams</td>
    <td>Artist</td>
  </tr>
</table>

__say this is example_table__


In this table, if I want to replace the occupation of John Doe (id 1) then,

```sql
UPDATE example_table
SET Occupations = "Actor"
WHERE id = 1
```

so the updated table is 


<table>
  <tr>
    <th>id</th>
    <th>Names</th>
    <th>Occupations</th>
  </tr>
  <tr>
    <td>1</td>
    <td>John Doe</td>
    <td>Actor</td>
  </tr>
  <tr>
    <td>2</td>
    <td>Jane Smith</td>
    <td>Teacher</td>
  </tr>
  <tr>
    <td>3</td>
    <td>Michael Johnson</td>
    <td>Doctor</td>
  </tr>
  <tr>
    <td>4</td>
    <td>Sarah Williams</td>
    <td>Artist</td>
  </tr>
</table>


# To delete a row

```sql
DELETE FROM table_name
WHERE column_name  = unique_value
```

for eg
```sql
DELETE FROM example_table
WHERE id  = 4
```

THE RESULT

<table>
  <tr>
    <th>id</th>
    <th>Names</th>
    <th>Occupations</th>
  </tr>
  <tr>
    <td>1</td>
    <td>John Doe</td>
    <td>Actor</td>
  </tr>
  <tr>
    <td>2</td>
    <td>Jane Smith</td>
    <td>Teacher</td>
  </tr>
  <tr>
    <td>3</td>
    <td>Michael Johnson</td>
    <td>Doctor</td>
  </tr>
  
</table>

# Where, between and in

## Where
Let's take this example table

<table>
  <tr>
    <th>id</th>
    <th>names</th>
    <th>occupations</th>
    <th>salary</th>
  </tr>
  <tr>
    <td>1</td>
    <td>John Doe</td>
    <td>Engineer</td>
    <td>5000</td>
  </tr>
  <tr>
    <td>2</td>
    <td>Jane Smith</td>
    <td>Teacher</td>
    <td>4000</td>
  </tr>
  <tr>
    <td>3</td>
    <td>Michael Johnson</td>
    <td>Doctor</td>
    <td>7000</td>
  </tr>
  <tr>
    <td>4</td>
    <td>Sarah Williams</td>
    <td>Artist</td>
    <td>3000</td>
  </tr>
</table>

Let's do some cool shit now

```sql

SELECT * FROM example_table
WHERE salary > 4000
```

RESULT is 

<table>
  <tr>
    <th>ID</th>
    <th>Names</th>
    <th>Occupations</th>
    <th>Salary</th>
  </tr>
  <tr>
    <td>1</td>
    <td>John Doe</td>
    <td>Engineer</td>
    <td>5000</td>
  </tr>
  <tr>
    <td>3</td>
    <td>Michael Johnson</td>
    <td>Doctor</td>
    <td>7000</td>
  </tr>
</table>


If I just want the names then

```sql

SELECT names FROM example_table
WHERE salary > 4000
```

Result is 
<table>
  <tr>
    <th>Names</th>
  </tr>
  <tr>
    <td>John Doe</td>
  </tr>
  <tr>
    <td>Michael Johnson</td>
  </tr>
</table>

## between

```sql
SELECT * FROM movies
WHERE salary BETWEEN 3000 AND 5000

```

Result is 

<table>
  <tr>
    <th>ID</th>
    <th>Names</th>
    <th>Occupations</th>
    <th>Salary</th>
  </tr>
  <tr>
    <td>1</td>
    <td>John Doe</td>
    <td>Engineer</td>
    <td>5000</td>
  </tr>
  <tr>
    <td>2</td>
    <td>Jane Smith</td>
    <td>Teacher</td>
    <td>4000</td>
  </tr>
</table>

## in

```sql

SELECT * FROM example_table
WHERE salary IN (5000, 3000)

```

<table>
  <tr>
    <th>ID</th>
    <th>Names</th>
    <th>Occupations</th>
    <th>Salary</th>
  </tr>
  <tr>
    <td>1</td>
    <td>John Doe</td>
    <td>Engineer</td>
    <td>5000</td>
  </tr>
  <tr>
    <td>4</td>
    <td>Sarah Williams</td>
    <td>Artist</td>
    <td>3000</td>
  </tr>
</table>



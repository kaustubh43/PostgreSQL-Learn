### Postgres is a relational database management system

*Relational Database Management System:*
A relational database organizes data into rows and columns, 
which collectively form a table. Data is typically structured across multiple tables,
which can be joined together via a primary key or a foreign key. 
These unique identifiers demonstrate the different relationships which exist between tables,
and these relationships are usually illustrated through different types of data models. 

### Organizing tables using Schemas:
> Schemas are a way to organize and group objects in a database.
> Schemas are te skeleton of the database
> They define constrainst like tables, primary keys, etc.
> Schema doesn't represent the data type of the attributes.

SELECT Query
> Select a table `SELECT * FROM manufacturing.products`
>
> Select and join two tables
>>``` 
>> SELECT products.product_id,
>>	products.name AS products_name,
>>	products.manufacturing_cost,
>>	categories.name AS category_name,
>>	categories.market
>> FROM manufacturing.products JOIN manufacturing.categories
>> ON products.category_id = categories.category_id
>>WHERE market = 'domestic';
>>```
> The above Query will query products where market is domestic and helps us join two tables with the help of primary and foreign keys.

SQL to query employees that work in the south building
```commandline
SELECT employees.employee_id,
employees.first_name,
employees.last_name,
departments.building
FROM human_resources.departments JOIN human_resources.employees
ON departments.department_id = employees.department_id
WHERE building='South'
ORDER BY employee_id ASC

```
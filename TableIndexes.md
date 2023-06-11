## Table Indexes
> Like indexes in textbook, they point to the content in the table
> 
> Help the Postgres database engine find records faster
> 
> Without an index, postgres performs a full table scan
> 
> Created on one or more columns in a table
>
 
### Creating an index
> btree method is the most common algorithm
>
> Typical naming convention is `table_column_idx`
> 
> The idx helps us determine that this is the index that is being created
>
> Query: 

### Setting a default value
> This helps us quickly enter a data with a default value.
> 
> The default value is the most common value entered.
>
> Query: ```ALTER TABLE IF EXISTS manufacturing.categories
    ALTER COLUMN category_id SET DEFAULT 4;```

### Constraints: Check Constraint
> This makes sure that we enter the correct data into columns that have common entries
>
> Example: `industrial` can be entered with a type `industriall`
> 
> To avoid this we set up a check constraint
> 
> Query: ```ALTER TABLE IF EXISTS manufacturing.categories
    ADD CONSTRAINT categories_market_check CHECK (market = 'domestic' OR market = 'industrial')
    NOT VALID;```
> 
> Query for date ```ALTER TABLE IF EXISTS human_resources.departments
    ADD CONSTRAINT departments_date_check CHECK (hire_date > '202-01-01')
    NOT VALID;```
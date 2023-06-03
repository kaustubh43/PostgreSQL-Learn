### Relational Databases:

Columns are name with snake case like so: `publication_key`

> A unique identifier is needed for table
> Usually it's name as name of the table with and underscore like so `book_id`
> This unique identifier is called Primary Key

## Data Types
Numeric, Binary, Boolean, Date/Time, Character, Monetary, Geometric

>### Numeric Data Types:
>>Use integer, smallint, or bigint for storing whole numbers 
>> 
>>Integer values range from -2 billion to +2 billion
>>
>>Use `numeric` or `decimal` for numbers with decimal points
>>
>>The value of 123.45 would require a `numeric(5,2)` data type
>>
>> Use `real` and `double precision` for floating point values. Used in data science applications

>### Character Data Types
>> Fixed-length strings use `character(n)` or `char(n)`
>>
>> The state abbreviation 'CA' would fit in `char(2)` column
>>
>> Variable length string use character `varying(n)` or `varchar(n)`.
>>
>> For unlimited length character data, use `text` data type. Perfect for blog posts and newspaper articles.

>### Date Data Types
>> `date` stores dates between 4713 BC and 587397 AD
>>
>> `time` will store time of day accurate to 1 microsecond
>>
>> Use `timestamp` to record both time and date in one column 
>>
>> `timestamp with time zone` adds time zone awareness

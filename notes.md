# Django Full Text Search

## PowerShell
```
$topicsjson = import-csv .\book_title_author.csv | ConvertTo-Json
$topicsjson | Add-Content -Path "mydata.json"
```

## Find Replace - Preparing Fixtures
```
"title"
"fields": { "title"
}},
```

## Postgres
####
```python
# Logging in via console
su - postgres
psql
psql -d postgres -c 'CREATE EXTENSION pg_trgm;'

# tsvector example
SELECT to_tsvector('english', 'Something in the summer makes everything just fine') AS search;

# Count book rows
SELECT 
   COUNT(*) 
FROM 
   book_book

# Simularity
SELECT show_trgm('I love Django search') AS A
SELECT word_similarity('word', 'two words');

SELECT title, word_similarity(title, 'harry potter') AS word_similarity
FROM book_book
WHERE title % 'harry potter'  
ORDER BY word_similarity DESC;

# Show indexes
select *
from pg_indexes
where tablename not like 'pg%';

# Get all schemas
=> \dt *.*
```

```python
# Accessing db from docker terminal
docker exec -it pgdb_books psql -U postgres -d postgres -c "SELECT * FROM book_book WHERE id=1"
docker exec -it pgdb_books psql -U postgres -d postgres -c "SELECT to_tsvector('english', 'Something in the summer makes everything just fine') AS search;"
```

https://django.cowhite.com/blog/mastering-search-in-django-postgres/

https://pganalyze.com/blog/full-text-search-django-postgres

https://www.compose.com/articles/mastering-postgresql-tools-full-text-search-and-phrase-search/

https://www.postgresql.org/docs/9.1/sql-explain.html

https://stackoverflow.com/questions/1074212/how-can-i-see-the-raw-sql-queries-django-is-running

https://stackoverflow.com/questions/12452395/difference-between-like-and-in-postgres

https://hevodata.com/blog/postgresql-full-text-search-setup/

https://www.jbssolutions.com/resources/blog/postsql-indexing-gin-django-trigram-similarity/

https://stackoverflow.com/questions/43793987/how-to-create-gin-index-in-django-migration

https://stackoverflow.com/questions/49922092/

https://blacksheephacks.pl/optimizing-django-database-queries-part-2/

https://forestry.io/blog/full-text-searching-with-postgres/

https://www.postgresql.org/docs/9.1/textsearch-controls.html
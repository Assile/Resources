# Useful resources for coding
I've decided to start my own collection. Mostly to be useful to myself, but if you get any use out of it yourself I'd love to hear about it! If you have suggestions for additions or edits, feel free to open an issue too 😄

Sections are sorted by alphabet (but by hand, so might not be perfect).

# Overview
- [Useful resources for coding](#useful-resources-for-coding)
- [Overview](#overview)
- [Databases](#databases)
- [Python](#python)
    - [Data related](#data-related)
        - [Database connectors](#database-connectors)
        - [Object-relational mapping (ORM)](#object-relational-mapping-orm)
    - [Performance](#performance)
    - [Web development](#web-development)
    - [Other](#other)

# Databases
- Microsoft SQL Server: [Website](https://www.microsoft.com/en-us/sql-server)
    - Microsoft SQL Server Management Studio (SSMS): [Website](https://learn.microsoft.com/en-us/sql/ssms/download-sql-server-management-studio-ssms)
        > This is the management suite for Microsoft SQL Server
- MySQL: [Website](https://www.mysql.com/)
    > See XAMPP for an easy way to spin up a MySQL-like database with a web-interface.
- PostgreSQL: [Website](https://www.postgresql.org/)
- SQLite: [Website]()
    > A database that works with a file or completely in memory instead of a server. This makes it a great choice for development, projects that only need a small database, a portable database, or when the overhead of a server would cost too many resources.
- XAMPP: [Website](https://www.apachefriends.org/download.html)
    > An easy way to spin up a MariaDB (MySQL dialect?) database with a web-interface.

# Python: [Website](https://www.djangoproject.com/), [Docs](https://docs.python.org/3/)
## Data related
- Pandas: [Website](https://pandas.pydata.org/), [Personal docs](./documentation/pandas/README.md)
    > Amazing package to easily load data from sources such as CSV, Excel, JSON, and even databases when using [SQLAlchemy](#object-relational-mapping-orm).
    > 
    > Since it's built on [Numpy](#other) it is quicker than using pure Python on your data. Try using it's built-in methods as much as you can!
    >
    > **Learn highlights** from my [personal docs](./documentation/pandas/README.md).
### Database connectors
- General connector: [PyODBC GitHub](https://github.com/mkleehammer/pyodbc)
    > Works for a lot of databases, as long as you have the relevant ODBC connector installed.
- SQLite: [SQLite3 built-in official docs](https://docs.python.org/3/library/sqlite3.html)
    > In contrast to the other connectors here, this one is built-in into Python
    > See also my comments on it under SQLite in the section [Databases](#databases).
- MySQL: [Official connector documentation](https://dev.mysql.com/doc/connector-python/en/)
- SQL Server: [Documentation](https://learn.microsoft.com/en-us/sql/connect/python/python-driver-for-sql-server), [Official mssql connector](https://learn.microsoft.com/en-us/sql/connect/python/pymssql/python-sql-driver-pymssql?view=sql-server-ver16), See also PyODBC

### Object-relational mapping (ORM)
- SQLAlchemy: [Website](https://docs.sqlalchemy.org/), [Official 2.0 tutorial](https://docs.sqlalchemy.org/en/20/tutorial/index.html)

## Performance
- Line profiler: [GitHub](https://github.com/pyutils/line_profiler)
    > For information on how leave the profiling decorator in code permanently see [personal documentation](./documentation/line_profiler/README.md).

## Web development
- Django: [Website](https://www.djangoproject.com/)
- Flask: [Website with docs and tutorial](https://flask.palletsprojects.com/)

## Other
- Numpy: [Website](https://numpy.org/)
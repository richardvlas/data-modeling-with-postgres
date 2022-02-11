# Data modeling with Postgres
The repository shows how to model user activity data to create a database and ETL pipeline in Postgres for a music streaming app. Fact and Dimension tables are defined and data are inserted into new tables.


### Database Setup

In this section, we describe how to start a PostgreSQL server. The instructions apply to Linux and the first step is to install PostgreSQL

```bash
sudo apt-get update
sudo apt-get install postgresql
```

Next start the PostgreSQL server by typing:

```bash
sudo service postgresql start
```

Once the postgres server is up and running, the next step is to configure it for use. Run the following command:

```bash
psql postgres
```

We have logged into the postgres service and now ready to execute psql commands. We are going to create a new user that will have the privileges to create and manage databases within the service. You can execute the command as follows to create the new user with the right access:

```bash
CREATE ROLE student WITH LOGIN PASSWORD 'student';
ALTER ROLE student CREATEROLE CREATEDB;
```

The second command gives the role the ability to create new databases.

Once the new user is created, you can check that it's available by typing the following command:

```bash
postgres=# \du
                                   List of roles
 Role name |                         Attributes                         | Member of 
-----------+------------------------------------------------------------+-----------
 postgres  | Superuser, Create role, Create DB, Replication, Bypass RLS | {}
 student   | Create DB                                                  | {}
```

Use the following statement to create a new database named studentdb in the PostgreSQL database server, which will be used initially in the scripts of this project:

```bash
CREATE DATABASE studentdb;
```

or use this one from the command line before loging into psql:

```bash
createdb -U postgres studentdb
```


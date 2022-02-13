# Data modeling with Postgres
A startup called Sparkify wants to analyze the data they've been collecting on songs and user activity on their new music streaming app. The analytics team is particularly interested in understanding what songs users are listening to. Currently, they don't have an easy way to query their data, which resides in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app.

They'd like a data engineer to create a Postgres database with tables designed to optimize queries on song play analysis. The role of this project is to create a database schema and ETL pipeline for this analysis. We will be also testing the database and ETL pipeline by running queries given by the analytics team from Sparkify and compare the results with their expected results.

## Project Description
In this project, we will model data with Postgres and build an ETL pipeline using Python. We will need to define fact and dimension tables for a star schema for a particular analytic focus, and write an ETL pipeline that transfers data from files in two local directories into these tables in Postgres using Python and SQL.

## Dependencies

You will need to install all Python dependencies that are stored in the [requirements.txt](requirements.txt) file. 

To install them, first open a terminal window in the folder of this repository and create & activate a virtual environment: 

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Then install the dependencies from the [requirements.txt](requirements.txt) file:

```bash
pip install -r requirements.txt 
```

## Database Setup

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

## Data Modelling


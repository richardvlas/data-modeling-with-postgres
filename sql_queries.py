# DROP TABLES
songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES
songplay_table_create = ("""
CREATE TABLE IF NOT EXISTS songplays (
    songplay_id int PRIMARY KEY, 
    start_time timestamp, 
    user_id int, 
    level varchar, 
    song_id int, 
    artist_id int, 
    session_id int, 
    location varchar, 
    user_agent varchar
);
""")

user_table_create = ("""
CREATE TABLE IF NOT EXISTS users (
    user_id int PRIMARY KEY, 
    first_name varchar, 
    last_name varchar, 
    gender varchar, 
    level varchar
);
""")

song_table_create = ("""
CREATE TABLE IF NOT EXISTS songs (
    song_id int PRIMARY KEY, 
    title varchar, 
    artist_id int, 
    year int, 
    duration numeric
);
""")

artist_table_create = ("""
CREATE TABLE IF NOT EXISTS artists (
    artist_id int PRIMARY KEY, 
    name varchar, 
    location varchar, 
    latitude numeric, 
    longitude numeric
);
""")

time_table_create = ("""
CREATE TABLE IF NOT EXISTS time (
    start_time timestap PRIMARY KEY, 
    hour int, 
    day int, 
    week int, 
    month int, 
    year int, 
    weekday int
);
""")


# INSERT RECORDS

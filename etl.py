import os
import glob
import psycopg2
import pandas as pd
from sql_queries import *


SONG_DATA_FILE_PATH = 'data/song_data'
LOG_DATA_FILE_PATH = 'data/log_data'


def process_song_file(cur, filepath):
    """
    Extract data from song json file and load the data into 'songs' and 
    'artists' tables.

    Parameters
    ----------
    cur : psycopg2.cursor
        a cursor object to database

    filepath : int
        path to song json file folder
    """
    # open song file
    df = pd.read_json(filepath, lines=True)

    # insert song record
    song_table_columns = ['song_id', 'title', 'artist_id', 'year', 'duration']
    song_data = df[song_table_columns].values[0].tolist()
    cur.execute(song_table_insert, song_data)

    # insert artist record
    artist_table_columns = ['artist_id', 'artist_name', 'artist_location', 
               'artist_latitude', 'artist_longitude']
    artist_data = df[artist_table_columns].values[0].tolist()
    cur.execute(artist_table_insert, artist_data)


def process_log_file(cur, filepath):
    """ 
    Extract data from log json file and load the data into 'user', 'songplay' 
    and 'time' tables.

    Parameters
    ----------
    cur : psycopg2.cursor
        a cursor object to database

    filepath : int
        path to log json file folder
    """
    # open log file
    df = pd.read_json(filepath, lines=True)

    # filter by NextSong action
    df = df[df['page'] == 'NextSong'].copy()

    # convert timestamp column to datetime
    t = pd.to_datetime(df['ts'], unit='ms')
    
    # insert time data records
    time_data = [t.values, t.dt.hour.values, t.dt.day.values, 
                 t.dt.isocalendar().week.values, t.dt.month.values, 
                 t.dt.year.values, t.dt.weekday.values]

    time_columns = ['start_time', 'hour', 'day', 'week', 'month', 'year', 'weekday']
    
    labeled_time_data = dict(zip(time_columns, time_data))

    time_df = pd.DataFrame(data=labeled_time_data)
    
    for i, row in time_df.iterrows():
        cur.execute(time_table_insert, list(row))

    # load user table
    users_columns = ['userId', 'firstName', 'lastName', 'gender', 'level']
    user_df = df[users_columns]

    # insert user records
    for i, row in user_df.iterrows():
        cur.execute(user_table_insert, row)

    # convert timestamp column to datetime and assign it to dataframe
    df['ts'] = pd.to_datetime(df['ts'], unit='ms')

    # insert songplay records
    for index, row in df.iterrows():

        # get songid and artistid from song and artist tables
        cur.execute(song_select, (row.song, row.artist, row.length))
        results = cur.fetchone()

        if results:
            songid, artistid = results
        else:
            songid, artistid = None, None
        
        # insert songplay record
        songplay_data = [row.ts, row.userId, row.level, songid, artistid, 
                         row.sessionId, row.location, row.userAgent]
        
        cur.execute(songplay_table_insert, songplay_data)


def process_data(cur, conn, filepath, func):
    """
    Process all files and insert data into database tables

    Parameters
    ----------
    cur : psycopg2.cursor
        a cursor object to database

    conn : psycopg2.connection
        a new connection object to database  

    filepath : int
        path to json file folder

    func : function
        function for processing data in each file
    """
    # get all files matching extension from directory
    all_files = []
    for root, dirs, files in os.walk(filepath):
        files = glob.glob(os.path.join(root, '*.json'))
        for f in files:
            all_files.append(os.path.abspath(f))

    # get total number of files found
    num_files = len(all_files)
    print('{} files found in {}'.format(num_files, filepath))

    # iterate over files and process
    for i, datafile in enumerate(all_files, 1):
        func(cur, datafile)
        conn.commit()
        print('{}/{} files processed.'.format(i, num_files))


def main():
    conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=student password=student")
    cur = conn.cursor()

    process_data(cur, conn, filepath=SONG_DATA_FILE_PATH, func=process_song_file)
    process_data(cur, conn, filepath=LOG_DATA_FILE_PATH, func=process_log_file)

    cur.close()


if __name__ == "__main__":
    main()

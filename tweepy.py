# first install the tweepy module by running ‘pip3 install tweepy’ in the command prompt/terminal
# add Twitter credentials (consumer key, consumer secret, access token, and access token secret) to secrets.py

## Fetching data & Storing it to a database

import tweepy
import json
import sys
import sqlite3
from secrets import *

DB_NAME='tweets.sqlite'

def get_tweets(search_term, num_tweets):
    auth=tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    api=tweepy.API(auth)
    searched_tweets=[status for status in tweepy.Cursor(api.search, q=search_term).items(num_tweets)]
    return searched_tweets

def init_db(db_name):
    ##code to create a new database and handle exception if connection fails
    try:
        conn=sqlite3.connect(db_name)
    except:
        print("Error: fail to create the SQLite database")
    cur=conn.cursor()
    #code to test whether table already exists
    st_exist_table='''SELECT count(*) FROM sqlite_master WHERE type="table" AND name="Tweets"'''
    cur.execute(st_exist_table)
    exi=cur.fetchall()[0][0]
    #if exists, prompt to user
    if exi==1:
        exist_input=input("Tweets Table already exists. Drop table? yes/no: ")
        #if user input is yes, drop table. Else, use move on and use existing table
        if exist_input=="yes":
            st_drop_table='''DROP TABLE "Tweets";'''
            cur.execute(st_drop_table)
            conn.commit()
            exi=0
    #if not exists or droppd, create table
    if exi==0:
        st_creat_table= '''CREATE TABLE 'Tweets' ('TweetId' INTEGER PRIMARY KEY UNIQUE,'TweetText' TEXT,'RetweetCount' INTEGER,
            'UserId' TEXT,'ScreenName' TEXT,'Location' TEXT,'FollowerCount' INTEGER);'''
        cur.execute(st_creat_table)
        conn.commit()
    #close database connection
    conn.close()

def insert_tweet_data(tweets):
    #code to connect to database and get a Cursor
    try:
        conn=sqlite3.connect('tweets.sqlite')
    except:
        print("Error: fail to connect to the SQLite database")
    cur=conn.cursor()
    #insert each of these data of interest to the Tweets table
    for tweet in tweets:
        cur.execute("SELECT COUNT(*) FROM Tweets WHERE TweetId= ?", (tweet.id,))
        exist_key=cur.fetchone()[0]
        if exist_key==0:
            insertion=(tweet.id,tweet.text.encode('utf8'),tweet.retweet_count,tweet.user.id,tweet.user.screen_name,tweet.user.location,tweet.user.followers_count)
            st_save_data='INSERT INTO "Tweets" '
            st_save_data+='VALUES (?, ?, ?, ?, ?, ?, ?)'
            cur.execute(st_save_data, insertion)
    conn.commit()
    #close database connection
    conn.close()
    #Comment these print statements when you submit code to us.
    # for tweet in tweets:
    #     print("Tweet ID:", tweet.id)
    #     print("Tweet Text:", tweet.text.encode('utf8'))
    #     print ("Retweet Count:", tweet.retweet_count)
    #     print("User ID:", tweet.user.id)
    #     print("User Screen Name:", tweet.user.screen_name)
    #     print("User Location:", tweet.user.location)
    #     print("User Follower Count:", tweet.user.followers_count)


if __name__ == "__main__":
    search_term=input("Enter search term: ")
    num_tweets=int(input("Enter number of tweets to retrieve: "))
    #fetch tweets
    tweets=get_tweets(search_term, num_tweets)
    print("Fetched",len(tweets),"tweets")
    #create database and table
    init_db(DB_NAME)
    #insert data into table
    insert_tweet_data(tweets)

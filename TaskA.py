# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 22:49:14 2019

@author: Vinay_Locharulu
"""

import tweepy
import csv
import pandas as pd
####input your credentials here
consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)
csvFile = open('ua7.csv', 'a')
csvWriter = csv.writer(csvFile)

hashtags=["#USElection2020","#Election2020","#Elections2020"]
hashtags_incomplete = ["#MAGA2020","#2020President","#2020poll", "#US2020","#2020Elections","#2020Election","#2020PresidentialElection","#2020_Presidential_Election","#USElection","#2020Presidential", "#PresentialElections","#2020USElections","#FederalElections","#UnitedStatesElections","#USAElections","#2020electionpoll" ]          
list1=[]          
df= pd.DataFrame()
vdf= pd.DataFrame()

list2=[]
list3=[]
list4 = []
count=0      
for i in hashtags_incomplete:
    print("Hashtag" + i)
    for tweet in tweepy.Cursor(api.search,q=i,count=3000,
                               lang="en",
                               since="2015-01-01").items():
        if (not tweet.retweeted) and ('RT @' not in tweet.text):
        
            count+=1
            print(i)
            print(count)
            print (tweet.user.location)
            if count >6000:
                break
            list1.append(tweet.created_at)
            list2.append(tweet.text)
            list3.append(tweet.user.location)
            list4.append(i)
                   
vdf['Date']= list1
vdf['tweets']= list2
vdf['User Location']= list3
vdf['hashtag']=list4
result_df1 = vdf.drop_duplicates(subset=['tweets'], keep='first')
vdf.to_csv('6ktweets.csv', encoding='utf-8')

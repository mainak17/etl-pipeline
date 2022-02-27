import os
import sys
import configparser
# import requests module
import requests


config = configparser.ConfigParser()
config.read('configfile.properties')

#Reading DataBase Details
db_name = config.get("database", "db_name")
db_schema = config.get("database", "db_schema")
db_user = config.get("database", "db_user")
db_password = config.get("database", "db_password")
db_host = config.get("database", "db_host")

#Reading Api details
api_address = config.get("api", "api_address")
api_topic = config.get("api", "api_topic")
api_topic_id = config.get("api", "api_topic_id")

url = api_address+api_topic+api_topic_id

def get_response(url):
    response = requests.get(url)
    return response.json()

def create_dataframe(data):
    from pandas import json_normalize 
    df = json_normalize(data)
    return df



if __name__ == "__main__":
    
    print("Hello World")


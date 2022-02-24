import os
import sys
import configparser
# import requests module
import requests


config = configparser.ConfigParser()
config.read('configfile.properties')

# print(config.get("ExampleSection", "example"))

def get_db_details():
    return config.get("database", "db_name"), config.get("database", "db_schema"),config.get("database", "db_user"), config.get("database", "db_password"), config.get("database", "db_host")
    
def get_properties():
    
 
# Making a get request
response = requests.get('https://api.github.com')
 
# print response
# print(response)
 
# print json content
# print(response.json())

def get_url():
    return config.get("api", "api_address")+config.get("api", "api_topic")+config.get("api", "api_topic_id")

def get_data():
    url = get_url()
    response = requests.get(url)
    return response.json()

def create_dataframe(data):
    from pandas import json_normalize 
    df = json_normalize(data)
    return df

def check_if_schema_exists(schema_name):
    from sqlalchemy import create_engine
    engine = create_engine('postgresql://postgres:postgres@localhost:5432/postgres')
    query = "SELECT EXISTS(SELECT 1 FROM information_schema.schemata WHERE schema_name = '{}')".format(schema_name)
    result = engine.execute(query)
    return result.fetchone()[0]


if __name__ == "__main__":
    # print(get_url())
    # print(get_data())
    # print(create_dataframe(get_data()))
    # print(check_if_schema_exists("test"))
    print(get_db_details())


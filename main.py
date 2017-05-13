#!/usr/bin/python2
from pymongo import MongoClient
from datetime import datetime

database = "cluster0-shard-00-02-zolhc.mongodb.net:27017"
password = "fuckFacebook69"
uri = "mongodb://D2_Dev:{}@cluster0-shard-00-00-zolhc.mongodb.net:27017, " + \
	"cluster0-shard-00-01-zolhc.mongodb.net:27017,cluster0-shard-00-02-zolhc.mongodb.net:27017/" + \
	"{}?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin".format(password, database)
db = MongoClient(uri)

def main():
	

if __name__ == "__main__":
	main()

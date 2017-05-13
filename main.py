#!/usr/bin/python2
import pymongo
from datetime import datetime

database = "cluster0-shard-00-02-zolhc.mongodb.net:27017"
password = "fuckFacebook69"
uri = "mongodb://D2_Dev:{}@cluster0-shard-00-00-zolhc.mongodb.net:27017, " + \
	"cluster0-shard-00-01-zolhc.mongodb.net:27017,cluster0-shard-00-02-zolhc.mongodb.net:27017/" + \
	"{}?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin".format(password, database)
try:
	conn = pymongo.MongoClient(uri)
	# force connection on a request as the
	# connect=True parameter of MongoClient seems
	# to be useless here
	print conn.server_info()
except pymongo.errors.ServerSelectionTimeoutError as err:
	print err
except:
	print pymongo.errors
	print pymongo.errors.PyMongoError.message
	print "FAILED"

def main():
	#createTable()
	db = conn.myFirstMB
	add_country(db)
	print get_country(db)

def createTable():
	# conn.runCommand({
	# 	"create": "test"
	# })
	db = conn.test;
	print db.test.insert_one({
		"user": "mig"
	})

	print db.find()

def add_country(db):
    db.countries.insert({"name" : "Canada"})

def get_country(db):
    return db.countries.find_one()


if __name__ == "__main__":
	# main()
	print "HERE"

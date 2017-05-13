#!/usr/bin/python2
import pymongo
from datetime import datetime

# database = "cluster0-shard-00-02-zolhc.mongodb.net:27017"
# password = "fuckFacebook69"
# uri = "mongodb://D2_Dev:{}@cluster0-shard-00-00-zolhc.mongodb.net:27017, " + \
# 	"cluster0-shard-00-01-zolhc.mongodb.net:27017,cluster0-shard-00-02-zolhc.mongodb.net:27017/" + \
# 	"{}?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin".format(password, database)

client = pymongo.MongoClient('localhost', 27017)
db = client.pymongo_test
posts = db.posts
post_data = {
    'title': 'Python and MongoDB',
    'content': 'PyMongo is fun, you guys',
    'author': 'Scott'
}
result = posts.insert_one(post_data)
print('One post: {0}'.format(result.inserted_id))
post_1 = {
    'title': 'Python and MongoDB',
    'content': 'PyMongo is fun, you guys',
    'author': 'Scott'
}
post_2 = {
    'title': 'Virtual Environments',
    'content': 'Use virtual environments, you guys',
    'author': 'Scott'
}
post_3 = {
    'title': 'Learning Python',
    'content': 'Learn Python, it is easy',
    'author': 'Bill'
}
new_result = posts.insert_many([post_1, post_2, post_3])
print('Multiple posts: {0}'.format(new_result.inserted_ids))
bills_post = posts.find_one({'author': 'Bill'})
print bills_post['content']

if __name__ == "__main__":
	# main()
	print "HERE"

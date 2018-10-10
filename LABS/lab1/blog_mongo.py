from pymongo import MongoClient

uri = "mongodb://admin:lehau6997@ds125263.mlab.com:25263/lab"

#Connect to database
client = MongoClient(uri)
db = client.get_default_database()

#Connection
posts = db["posts"] #insert_one (create), find (read)

post_list = posts.find()
for p in post_list:
    print(p['title'])

#Document
#Create a document
# post = {
#     'title': 'hom nay troi am u',
#     'content': 'toi o nha lam bai tap',
#     'author': 'me',
# }
# #Insert created document
# posts.insert_one(post)

from pymongo import MongoClient

uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

#connect db
client = MongoClient(uri)

db = client.get_default_database()

#collection
posts = db['posts']

#create
post = {
    'title': 'Xin chào techkids!!',
    'content': 'Rất vui khi được học tập cùng mọi người, hy vọng sau khóa học tất cả chúng ta sẽ đạt được một kết quả ưng ý',
    'author': 'Hậu Lê' 
}

#insert

posts.insert_one(post)

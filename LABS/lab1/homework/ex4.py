from pymongo import MongoClient
from matplotlib import pyplot
uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

#connect db
client = MongoClient(uri)

db = client.get_default_database()

#collection
posts = db['customers']

#count

count_events = posts.find({"ref": "events"}).count()
count_word = posts.find({"ref": "wom"}).count()
count_ads = posts.find({"ref": "ads"}).count()


#lables

machine_names = ["Events", "Wom", "Ads"]

#draw
counts  = [count_events,count_word,count_ads]
pyplot.pie(counts, labels=machine_names, autopct="%.1f%%", explode=[ 0,0.1,0])
pyplot.title("Events, Wom, Ads \n ")
pyplot.axis('equal')
#show
pyplot.show()

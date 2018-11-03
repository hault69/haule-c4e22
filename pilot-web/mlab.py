import mongoengine

#mongodb://<dbuser>:<dbpassword>@ds211588.mlab.com:11588/c4e22-poll

host = "ds211588.mlab.com"
port = 11588
db_name = "c4e22-poll"
user_name = "admin"
password = "admin1"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())
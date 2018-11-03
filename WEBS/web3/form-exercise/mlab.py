#mongodb://<dbuser>:<dbpassword>@ds147213.mlab.com:47213/form_register
import mongoengine


host = "ds147213.mlab.com"
port = 47213
db_name = "form_register"
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
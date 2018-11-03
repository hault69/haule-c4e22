from mongoengine import Document,StringField
class Register(Document):
    firstname = StringField()
    lastname = StringField()
    email = StringField()
    yob = StringField()
    gender = StringField()
    city = StringField()
    code = StringField()
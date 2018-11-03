from poll import Poll
from random import choice
import mlab

#1 connect to database
mlab.connect()

#2  Prepare data
q = "hackathon an gi?"
opts = [
    "pizza",
    "banh my hoi an",
    "pho xao",
]
alphabet = "abcdefghijklmnopqrstuvwxyz0123456789".upper()
c =""
for _ in range(6):
    c+=choice(alphabet)
print(c)

#3 Create Document
p = Poll(question = q,options = opts, code = c )

#4 Save
p.save()
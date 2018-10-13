import pyexcel
#covert fix cung vi tri
from collections import OrderedDict
data = [
    OrderedDict({
        'name':'Quan',
        'age':22,
    }),
    OrderedDict({
        'name':'Hung',
        'age':20,
    }),
    OrderedDict({
        'name':'Ku Anh',
        'age':21,
    })
]
pyexcel.save_as(records = data,dest_file_name = "sample1.xlsx")
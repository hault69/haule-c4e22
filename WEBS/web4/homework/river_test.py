from river import River
import mlab

#1 connect
mlab.connect()

#2. read all
rivers_list = River.objects(continent = "Africa")
for p in rivers_list:
        print(p.name)
        print(p.continent)
        print(p.length)
        print("*"*20) 
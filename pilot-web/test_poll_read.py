from poll import Poll
import mlab

#1 connect
mlab.connect()

#2. read all
poll_list = Poll.objects()  #page cục bộ lớn, lazy loading dữ liệu chờ
for p in poll_list:
    print(p.question)
    print(p.options)
    print(p.code)
    print("-----------------------")
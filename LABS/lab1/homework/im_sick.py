import datetime
from gmail import GMail, Message
from random import choice
now = datetime.datetime.now()
benh = ["om","cam"]
trieu_chung = ["dau dau", "so mui"]
gmail = GMail('hautechkids@gmail.com','lehau6997')
html_template =  '''
em bị
{{benh}}
cảm thấy: 
{{trieu_chung}}
'''
b = choice(benh)
t = choice(trieu_chung)
html_content1 = html_template.replace("{{trieu_chung}}",t)
html_content = html_content1.replace("{{benh}}",b)
msg = Message('Im Sick',to='hautechkids@gmail.com',html=html_content)
if now.hour == 7:
    gmail.send(msg)
    break
else:
    print("chua den gio gui mail!!")
#có thể dùng vòng lặp while để chạy đến thời gian yêu cầu gửi mail. tuy nhiên
#trong bài này em dùng if else để cho ra kết quả trực quan!
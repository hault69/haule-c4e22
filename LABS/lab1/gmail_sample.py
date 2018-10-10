for i in range(10):
    from gmail import GMail, Message
    from random import choice
    benh = ["om","cam"]
    trieu_chung = ["dau dau", "so mui"]
    gmail = GMail('hautechkids@gmail.com','lehau6997')
    html_template =  '''
    em bi
    {{trieu_chung}}
    {{benh}}
    '''
    b = choice(benh)
    t = choice(trieu_chung)
    html_content1 = html_template.replace("{{trieu_chung}}",t)
    html_content = html_content1.replace("{{benh}}",b)
    msg = Message('C4E22 Test',to='tungnm52@wru.vn',html=html_content)
    gmail.send(msg)
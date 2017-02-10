# coding:utf-8
# 实现图文格式的服务器性能报表邮件

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

HOST = 'smtp.gmail.com'
SUBJECT = 'Test email from Python'
TO = 'testmail@qq.com'
FROM = 'mymail@gmail.com'


def addimg(src, imgid):
    fp = open(src, 'rb')
    msgImage = MIMEImage(fp.read())
    fp.close()
    msgImage.add_header('Content-ID', imgid)
    return msgImage


msg = MIMEMultipart('related')

msgtext = MIMEText('<font color=red>官方业务周平均延迟时图表：<br><img src=\'cid:weekly\'border=\'1\'><br>详细内容见附件。</font>','html','utf-8')
msg.attach(msgtext)
msg.attach(addimg('img/weeking.png','weekly')

attach = MIMEText(open('doc/week_report.xlsx', 'rb').read(), 'base64', 'utf-8')
attach['Content-Type'] = 'application/octet-stream'
attach['Content-Disposition'] = 'attachment; filename=\'业务服务质量周报（12）周.xlsx\''.
decode('utf-8').encode('gb18030')

msg.attach(attach)
msg['Subject'] = SUBJECT
msg['From'] = FROM
msg['To'] = TO
try:
    server = smtplib.SMTP()
    server.connect(HOST,'25')
    server.starttls()
    server.login('user', 'passwd')
    server.sendmail(FROM, [TO], msg.as_string())
    server.quit()
    print '邮件发送成功'
except Exception, e:
    print '失败：' + str(e)

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

msgtext = MIMEText("""
<table width='600' border='0' cellspacing='10' cellpadding='4'>
      <tr bgcolor='#CECFAD' height=20' style= 'font-size:14px'>
        <td colspan='2'>*官方性能数据  <a href='monitor.domain.com'>更多>></a></td>
      </tr>
      <tr bgcolor='#EFEBDE' height='100' style='font-size:13px'>
        <td>
         <img src='cid:io'></td><td>
         <img src='cid:key_hit'></td>
      </tr>
      <tr bgcolor='#EFEBDE' height='100' style='font-size:13px'>
         <td>
     	 <img src='cid:men'></td><td>
         <img src='cid:swap'></td>
      </tr>
    </table>""",'html','utf-8')


msg.attach(msgtext)
msg.attach(adding('img/bytes_io.png','io')
msg.attach(adding('img/os_mem.png','men')
msg.attach(adding('img/os_swap.png','swap')
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

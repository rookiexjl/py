# coding:utf-8
# gmail向qq邮箱发邮件

import smtplib
import string

HOST = 'smtp.gmail.com'
SUBJECT = 'Test email from Python'
TO = 'testmail@qq.com'
FROM = 'mymail@gmail.com'
text = 'Python rules them all!'
BODY = string.join((
	'Form: %s' % FROM,
	'To: %s' % TO,
	'Subject: %s' % SUBJECT,
	'',
	text),
	'\r\n')
server = smtplib.SMTP()
server.connect(HOST,'25')
server.starttls()
server.login('mymail#gmail.com', 'mypassword')
server.sendmail(FROM, [TO], BODY]
server.quit()



'''
发邮件:
'''
import smtplib ,time
from email.mime.text import MIMEText
SMTPServer = 'smtp.163.com'
sender = 'arsenic11@163.com'
passwd = '1234qwe'#授权密码
message = '1111111'
msg = MIMEText(message)
#标题
msg ['Subject'] = '5108'
msg ['From'] = sender
mailServer = smtplib.SMTP(SMTPServer, 25)
mailServer.login(sender, passwd)
mailServer.sendmail(sender, ['1430349989@qq.com'], msg.as_string())
mailServer.quit()


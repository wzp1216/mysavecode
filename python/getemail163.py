import imaplib 
import sys
username='wzp1216@163.com'
password='zlh*1216720328'

mail_server='imap.163.com'
i=imaplib.IMAP4_SSL(mail_server)
print( i.login(username,password))
print( i.select('INBOX'))
for msg_id in i.search(None,'ALL')[1][0].split():
    print(msg_id)
i.logout()


'''
p=poplib.POP3(mail_server)
try:
    p.user(username)
    p.pass_(password)
except   poplib.error_proto:
    print("login failed")
    sys.exit(1)

for msg_id in p.list()[1]:
    print( msg_id)
q.quit()
'''


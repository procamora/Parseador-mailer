import getpass, imaplib

M = imaplib.IMAP4_SSL("imap.gmail.com", 993)
email = 'USERNAME@gmail.com'
password = 'PASSWORD'
M.login(email, password)

M.select()
typ, data = M.search(None, 'SUBJECT', "Gmail")
for num in data[0].split():
    typ, data = M.fetch(num, '(RFC822)')
    print(('Message %s\n%s\n' % (num, data[0][1])))
M.close()
M.logout()
from email.message import EmailMessage
import ssl,smtplib

# assign sender,password,subject elements to variables
email_sender = 'Padigachris@gmail.com'
email_password = 'eivt sumy iaic okwh'

# email_receiver = 'matacap435@ubinert.com'
email_receiver = 'Chrispadiga@gmail.com'

subject = 'Dont forget to reach me today x'

body = '''
Dont forget to subsribe
'''

# create an instance of the Emailmessage using the variables
em= EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['subject'] = subject

em.set_content(body)

# create context
context =ssl.create_default_context()

# initialize smtp email sender and add context
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender,email_password)
    smtp.sendmail(email_sender,email_receiver,em.as_string())
    print('Message sent')



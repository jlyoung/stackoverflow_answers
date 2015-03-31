import smtplib

def main():
	hostname = 'smtp.gmail.com'
	port = 587
	username = 'jlyoung.gmail.test@gmail.com'
	password = 'testpassword'
	sender = 'jlyoung.gmail.test@gmail.com'
	receivers = ['jlyoung.receiver.addr@stackoverflowexample.com']
	message = '''From: J.L. Young <jlyoung.gmail.test@gmail.com>
To: JLY Receiver <jlyoung.receiver.addr@stackoverflowexample.com>
Subject: Sending e-mail from gmail

This appears to work.
Cheers!
'''
	try:
		server = smtplib.SMTP(hostname, port)
		server.set_debuglevel(1)
		server.ehlo()
		server.starttls()
		server.login(username,password)
		response = server.sendmail(sender, receivers, message)
		server.quit()
		print response
	except Exception as e:
		print e	


if __name__ == '__main__':
	main()
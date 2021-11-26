import smtplib

my_email = "smtptestemailadress@gmail.com"
password = "qseDSa123"



with smtplib.SMTP("smtp.gmail.com") as connection:
	connection.starttls()
	connection.login(user=my_email, password=password)
	connection.sendmail(
		from_addr=my_email,
		to_addrs="dawid@pluscode.io",
		msg="Subject:Hello\n\nThis is a body of an email.")
	connection.close()


import smtplib
import datetime as dt
import random

my_email = "smtptestemailadress@gmail.com"
password = "qseDSa123"

dw = dt.datetime.now().weekday()

if dw == 0:
	with open("quotes.txt", "r") as f:
		all_quotes = f.readlines()
		quote = random.choice(all_quotes)

	print(quote)


	with smtplib.SMTP("smtp.gmail.com") as connection:
		connection.starttls()
		connection.login(user=my_email, password=password)
		connection.sendmail(
			from_addr=my_email,
			to_addrs="dawid@pluscode.io",
			msg=f"Subject:Monday motivation\n\n{quote}")
		connection.close()



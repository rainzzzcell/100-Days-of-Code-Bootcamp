import random
import smtplib
import datetime as dt
import random

MY_EMAIL="glebrainz@gmail.com"
MY_PASSWORD = "QEtuo24680"

now = dt.datetime.now()
weekday= now.weekday()
if weekday == 1:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Monday motivation \n\n{quote}"
        )














# import smtplib
#
# my_email = "glebrainz@gmail.com"
# password = "nvxjjdwrbwhohvcr"
#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email,password=password)
#     connection.sendmail(from_addr=my_email, to_addrs="rain2000z@icloud.com", msg="Subject:Hello\n\nThis is the body")
#
# import datetime as dt
#
# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_week = now.weekday()
# print(day_of_week)
#
# date_of_birth=
# datetime = dt.date
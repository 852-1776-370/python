from smtplib import *
def current_directory():
    a=SMTP_SSL("smtp gmai.com",465)
    a.ehlo()
    a.starttls()
    a.login("rameshgiri76370@gmail.com",vicky69123807)
    a.sendmail("rameshgiri76370@gmail.com","giriramesh843@gmail.com","Subject: SMPT \n hi i am ramesh giri good evening")
    a.quit()

current_directory()

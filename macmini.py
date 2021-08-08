#!/usr/bin/python
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import requests
import smtplib
import time

ua = UserAgent()
URL = 'https://www.apple-nic.com/applestore/mac-shop/mac-mini/apple-mac-mini-2020-mgnr3.html'
header = {"User-Agent": ua.random }

def check_price():
    page = requests.get(URL, headers=header)
    soup = BeautifulSoup(page.content, 'html.parser')
    title = soup.find(id = 'hikashop_product_name_main').get_text()
    price = soup.find(itemprop = 'price').get_text()
    new_price = price[0:6]
    new_price = float(new_price.replace(',','.'))

    print(new_price)

    if(new_price < 11.999):
        send_mail()

def send_mail():
    send_mail = "mm3906078@gmail.com"
    recive_mail = "mg3906078@gmail.com"
    passwd = "wesdxbvyieifxzti"
    server = smtplib.SMTP('smtp.gmail.com',587)
    # stable connection
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(send_mail , passwd)
    subject = 'Mac mini'
    body = "Check link https://www.apple-nic.com/applestore/mac-shop/mac-mini/apple-mac-mini-2020-mgnr3.html"
    msg = f"Subject : {subject} \n\n {body}"
    server.sendmail(
        send_mail,
        recive_mail,
        msg
    )
    print("EMAIL SENT!!")
    server.quit()

# while(True):
#     check_price()
#     time.sleep(7200)

check_price()
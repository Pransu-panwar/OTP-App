import requests
import json
from tkinter import *
def send_sms(number,message):
    url='https://www.fast2sms.com/dev/bulk'
    params={
        'authorization':'Ldy8OWUTj4gRiHek7nVIfFvYMzp6C0EbhuD1q9lXaoGSxQNZcPDT4zwo93Pa7mrfp56iVnLykSvg0qMd',
        'sender_id':'FSTSMS',
        'message': message,
        'language':'english',
        'route':'p',
        'numbers':number
    }
    response=requests.get(url,params=params)
    dic = response.json()
    print(dic)
for i in range(2):
    print("enter the number: ")
    n=int(input())
    send_sms(n,'kyu fat gyi na XD')

    '''7895009387
    9837543115'''
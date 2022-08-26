from sys import api_version
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from django.core.mail import send_mail
# Create your views here.

def open_csv(name):
    with open("api/"+name) as file:
        content = file.readlines()
    header = content[:1]
    rows = content[1:]
    return rows

def send_email(email):
    subject = 'welcome to GFG world'
    message = f'Hi thank you for registering in geeksforgeeks.'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, email_from, recipient_list)


@api_view(['POST'])
def send_email_api(request):
    rows = open_csv("emailsheet1.csv")
    send_email("harsh.gaud@iiitg.ac.in")
    return Response({})

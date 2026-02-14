from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(requests):
    #work with database
    # transform data
    #pass data
    # http response/json response
    return HttpResponse("Welcome to the tasks management system")

def contact(requests):
    return HttpResponse("This is contact page")
def show_task(requests):
    return HttpResponse("This is show task page")
from django.shortcuts import render
from django.http import HttpResponse
from myappcli.tasks import print_hello


def test_view(request):
    print_hello.delay()  # This runs in the background
    return HttpResponse("Task sent to queue!")

from django import http
from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
import re


def index(request):
    return render(request, 'index.html')

def analyze(request):
    #Get the text
    djtext = request.POST.get('text', 'default')
    print(djtext)
    # Check checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    params ={}
    #Check which checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        djtext = analyzed
        # params = {'purpose':'Removed Punctuations', 'analyzed_text': analyzed}
        # return render(request, 'analyze.html', params)
    if newlineremover=="on":
        analyzed=""
        for char in djtext:
            if char!="\n" and char!='\r':
                analyzed =analyzed +char
        djtext = analyzed
        # params = {'purpose':'Removed Punctuations', 'analyzed_text': analyzed}
        # return render(request, 'analyze.html', params)
    if(extraspaceremover=="on"):
            analyzed = ""
            for index, char in enumerate(djtext):
                if not(djtext[index] == " " and djtext[index+1]==" "):
                    analyzed = analyzed + char
            djtext = analyzed
    if extraspaceremover != "on" and newlineremover!= "on" and removepunc!="on":
        return HttpResponse("<h2>Please select atleast one option</h2>")
    params = {'purpose':'Removed Punctuations', 'analyzed_text': analyzed}
    return render(request, 'analyze.html', params)

def capfirst(request):
    return HttpResponse("capitalize first")

def newlineremove(request):
    return HttpResponse("new line remove")

def spaceremove(request):
    return HttpResponse("space remover")

def charcount(request):
    return HttpResponse("charcount ")
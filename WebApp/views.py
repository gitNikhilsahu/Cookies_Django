from django.shortcuts import render
from django.http import HttpResponse

def SetCookie(request):
    response = HttpResponse("<h1>Hey ..... Cookie set..........!!</h1>")
    response.set_cookie('user', 'Niki')
    return response

def GetCookie(request):
    user = request.COOKIES['user']
    return HttpResponse(user + "<h1>Get Cookie Success......!!</h1>")

def DelCookie(request):
    response = HttpResponse("<h1>Hey Get Cookie delete.....!!</h1>")
    response.delete_cookie('user')
    return response

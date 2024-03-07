from django.shortcuts import render

def homePage(request):
    return render(request,"index.html")

def loginPage(request):
    return render(request,"login1.html")

def aboutusPage(request):
    return render(request,"aboutus.html")

def contactusPage(request):
    return render(request,"contactus.html")

def registrationPage(request):
    return render(request,"register.html")

def checkpackages(request):
    return render(request,"package.html")

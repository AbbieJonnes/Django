from django.shortcuts import render
from django.http import HttpResponse

# def welcome(request):
#     return HttpResponse("Welcome to our Django class")

# def about(request):
#     return HttpResponse("About us")

# def contact(request):
#     return HttpResponse("contact us page")

# def termsandconditions(request):
#     return HttpResponse("Agree to our terms and conditions to proceed")

def welcome(request):
     return render(request, 'home.html')
def contact(request):
    return render(request, 'contact.html')
def about(request):
    return render(request, 'about.html')

# def sample(request):
#     return HttpResponse('such an amazing work')

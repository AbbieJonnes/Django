from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import BlogPost
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

def post_list(request):
    posts = BlogPost.objects.all()
    return render(request,'post_list.html',{'posts':posts}) 

def post_detail(request, post_id):
    post = get_object_or_404(BlogPost, pk=post_id)
    return render(request, 'post_detail.html', {'post': post})

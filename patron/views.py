from django.shortcuts import render


# Create your views here.
def indexPageView(request):
    return render(request, 'MissingPersonsProject1/index.html')

def about(request):
    return render(request, 'MissingPersonsProject1/about.html')

def contact(request):
    return render(request, 'MissingPersonsProject1/contact.html')

def current(request):
    return render(request, 'MissingPersonsProject1/current.html')

def post1(request):
    return render(request, 'MissingPersonsProject1/post.html')

def post2(request):
    return render(request, 'MissingPersonsProject1/post2.html')

def post3(request):
    return render(request, 'MissingPersonsProject1/post3.html')

def post4(request):
    return render(request, 'MissingPersonsProject1/post4.html')
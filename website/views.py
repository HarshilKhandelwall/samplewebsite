from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

def services(request):
    return render(request, 'services.html', {})

def about(request):
    return render(request, 'about.html', {})   

def portfolio(request):
    return render(request, 'portfolio.html', {})

def single_portfolio(request):
    return render(request, 'single-portfolio.html', {})

def blog(request):
    return render(request, 'blog.html', {})

def contact(request):
    return render(request, 'contact.html', {})

def single(request):
    return render(request, 'single.html', {})
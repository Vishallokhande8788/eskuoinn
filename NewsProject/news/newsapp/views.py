from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def news(request):
    name = "News App"
    feature1 = "Live news by category"
    feature2 = "Responsive UI with Bootstrap"
    feature3 = "Easy navigation with buttons"
    techstack = "Django, Python, Bootstrap"
    deployoptions = "Vercel", "Cloudflare", "Netlify"

    my_dict = {
        'name': name,
        'feature1': feature1,
        'feature2': feature2,
        'feature3': feature3,
        'techstack': techstack,
        'deployoptions': deployoptions
    }

    return render(request, 'newsapp/home.html', context=my_dict)

def politics(request):
    name = "News App"
    feature1 = "Live news by category"
    feature2 = "Responsive UI with Bootstrap"
    feature3 = "Easy navigation with buttons"
    techstack = "Django, Python, Bootstrap"
    deployoptions = "Vercel", "Cloudflare", "Netlify"

    my_dict = {
        'name': name,
        'feature1': feature1,
        'feature2': feature2,
        'feature3': feature3,
        'techstack': techstack,
        'deployoptions': deployoptions
    }
    return render(request,'newsapp/politics.html', context=my_dict)

def sports(request):
    name = "News App"
    feature1 = "Live news by category"
    feature2 = "Responsive UI with Bootstrap"
    feature3 = "Easy navigation with buttons"
    techstack = "Django, Python, Bootstrap" 
    deployoptions = "Vercel", "Cloudflare", "Netlify"
    my_dict = {
        'name': name,
        'feature1': feature1,
        'feature2': feature2,
        'feature3': feature3,
        'techstack': techstack,
        'deployoptions': deployoptions
    }
    return render(request,'newsapp/sports.html', context=my_dict)    
def technology(request):
    name = "News App"
    feature1 = "Live news by category"
    feature2 = "Responsive UI with Bootstrap"
    feature3 = "Easy navigation with buttons"
    techstack = "Django, Python, Bootstrap"
    deployoptions = "Vercel", "Cloudflare", "Netlify"
    my_dict = {
        'name': name,
        'feature1': feature1,
        'feature2': feature2,
        'feature3': feature3,
        'techstack': techstack,
        'deployoptions': deployoptions
    }
    return render(request,'newsapp/technology.html', context=my_dict)
def weather(request):
    name = "News App"
    feature1 = "Live news by category"
    feature2 = "Responsive UI with Bootstrap"
    feature3 = "Easy navigation with buttons"
    techstack = "Django, Python, Bootstrap"
    deployoptions = "Vercel", "Cloudflare", "Netlify"
    my_dict = {
        'name': name,
        'feature1': feature1,
        'feature2': feature2,
        'feature3': feature3,
        'techstack': techstack,
        'deployoptions': deployoptions
    }
    return render(request,'newsapp/weather.html', context=my_dict)


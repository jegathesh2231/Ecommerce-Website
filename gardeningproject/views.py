from django.shortcuts import render


def home(request):
    return render(request,'index.html')


def about(request):
    return render(request,'about.html')



def service(request):
    return render(request, 'service.html')


def project(request):
    return render(request,'project.html')



def contact(request):
    return render(request, 'contact.html')


def feature(request):
    return render(request, 'feature.html')


def quote(request):
    return render(request, 'quote.html')


def team(request):
    return render(request, 'team.html')



def testimonial(request):
    return render(request, 'testimonial.html')


def error(request):
    return render(request, '404.html')

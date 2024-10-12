from django.shortcuts import render

def home(request):
    return render(request, 'vibank/pages/home.html')

def cartoes(request):
    return render(request, 'vibank/pages/cards.html')

def pjemei(request):
    return render(request, 'vibank/pages/pjemei.html')

def pessoafisica(request):
    return render(request, 'vibank/pages/pessoafisica.html')

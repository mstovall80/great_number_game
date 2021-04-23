from django.shortcuts import render, redirect
import random



def index(request):
    if 'number' not in request.session:
        request.session['number'] = random.randint(1, 10)
    return render(request, 'index.html')

def guess(request):
    print(request.POST)
    request.session['guess'] = int(request.POST['number'])
    if request.session['guess'] < request.session['number']:
        request.session['guess'] = "to low"
    elif request.session['guess'] > request.session['number']:
        request.session['guess'] = "to high"
    elif request.session['guess'] == request.session['number']:
        request.session['guess'] = "that is correct"
    return redirect('/')

def reset(request):
    request.session.flush()
    return redirect("/")




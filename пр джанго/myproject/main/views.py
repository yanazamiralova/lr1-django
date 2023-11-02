from django.shortcuts import render, redirect
from .models import Staf
from .forms import StafForm


def index(request):
    staf = Staf.objects.order_by('id')
    return render(request, 'main/index.html', {'title': 'Главная страница сайта',
                                               'staf': staf})



def order(request):
    return render(request, 'main/order.html')


def add(request):
    error = ""
    if request.method == 'POST':
        form = StafForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была неверной'

    form = StafForm()
    context = {'form': form, 'error': error}
    return render(request, 'main/add.html', context)

from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Crypto
from .forms import UpdateForm

def table(request):
    Cryptos = Crypto.objects.all()
    return render(request, 'Table.html', {'Crypto': Cryptos}) 

def update(request, id):
    form = UpdateForm(instance=Crypto)
    instance = Crypto.objects.get(id=id)

    if request.method == 'POST':
        form = UpdateForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'UpdateTable.html', {'form': form})
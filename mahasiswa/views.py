from django.shortcuts import get_object_or_404, render, redirect
from .models import Data_mahasiswa
from .forms import BiodataMhs
# Create your views here.

def index(request):
    hasil = Data_mahasiswa.objects.all()
    
    data = {
        'data':hasil,
    }
    
    return render(request, 'mahasiswa/index.html', data)


def tambahData(request):
    form = BiodataMhs(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('/')
        pass
    else:
        form = BiodataMhs()
    data = {
        'form':form,
    }
    return render(request, 'mahasiswa/tambah_data.html', data)

def editData(request, npm):
    obj = get_object_or_404(Data_mahasiswa, npm=npm)
    form = BiodataMhs(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('/')
    data ={
        'mhs':obj,
    }
    return render(request,'mahasiswa/edit_data.html', data)

def hapusData(request, npm):
    hapus = Data_mahasiswa.objects.get(npm=npm)
    hapus.delete()
    return redirect('/')
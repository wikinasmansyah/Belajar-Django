from django.shortcuts import render

def buku(request):
    judul = ["Belajar Django", "Belajar Python", "Belajar Bootstrap"]
    penulis = "Sofia Ardina"

    konteks = {
        'title' : judul,
        'penulis' : penulis,
    }
    return render(request, 'buku.html', konteks)

def penerbit(request):
    return render(request, 'penerbit.html')


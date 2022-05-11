from django.contrib import admin
from django.urls import path
from Perpustakaan.views import buku, penerbit

urlpatterns = [
    path('admin/', admin.site.urls),
    path('buku/', buku),
    path('penerbit/', penerbit),
]

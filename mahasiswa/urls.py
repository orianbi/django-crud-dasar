from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tambah_data/', views.tambahData, name='tambah_data'),
    path('edit_data/<str:npm>/', views.editData, name='edit_data'),
    path('hapus/<str:npm>/', views.hapusData, name='hapus_data'),
    
]

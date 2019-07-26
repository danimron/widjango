from django.urls import path
from .views import AnggotaListView, AnggotaDetailView

urlpatterns = [
    path('', AnggotaListView.as_view(), name='anggota'),
    path('<str:npm>', AnggotaDetailView.as_view(), name='anggota_detail')
]

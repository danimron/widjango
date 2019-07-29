from django.urls import path
from .views import ThreadCreateView, ThreadListView, ThreadDetailView


urlpatterns = [
    path('', ThreadListView.as_view(), name='thread_list'),
    path('create', ThreadCreateView.as_view(), name='thread_create'),
    path('<int:pk>', ThreadDetailView.as_view(), name='thread_detail'),
]

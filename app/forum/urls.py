from django.urls import path, include
from .views import (
    ThreadCreateView,
    ThreadListView,
    ThreadDetailView,
    ThreadUpdateView,
    ThreadDeleteView
)


urlpatterns = [
    path('', ThreadListView.as_view(), name='thread_list'),
    path('create', ThreadCreateView.as_view(), name='thread_create'),
    path('<int:pk>', ThreadDetailView.as_view(), name='thread_detail'),
    path('update/<int:pk>', ThreadUpdateView.as_view(), name='thread_update'),
    path('delete/<int:pk>', ThreadDeleteView.as_view(), name='thread_delete'),
    path('comments/', include('django_comments.urls'))
]

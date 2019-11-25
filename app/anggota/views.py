import requests
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404


class AnggotaListView(LoginRequiredMixin, ListView):
    template_name = 'anggota/anggota_list.html'
    context_object_name = 'objects'
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    himatif_list = requests.get(
        'http://api.himatif.org/data/v1/anggota').json()['response']
    ika_list = [obj for obj in himatif_list if
                obj['status'] == 'Anggota Kehormatan']

    def get_queryset(self):
        search = self.request.GET.get('search', None)
        if search:
            object_list = [obj for obj in self.ika_list if
                           search in obj['nama'].lower() or search in obj['npm'] or search in obj['angkatan']]
        else:
            object_list = self.ika_list
        return object_list


class AnggotaDetailView(LoginRequiredMixin, DetailView):
    template_name = 'anggota/anggota_detail.html'
    context_object_name = 'object'
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    def get_object(self):
        npm = self.kwargs['npm']
        obj = requests.get(
            'http://api.himatif.org/data/v1/anggota/search?type=npm&q=' + npm).json()['response'][0]
        if not obj:
            raise Http404('Anggota tidak ditemukan')
        return obj

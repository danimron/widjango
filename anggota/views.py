import requests
from django.views.generic import ListView, DetailView
from django.http import Http404


himatif_list = requests.get(
    'http://api.himatif.org/data/v1/anggota').json()['response']
ika_list = [obj for obj in himatif_list if
            obj['status'] == 'Anggota Kehormatan']


class AnggotaListView(ListView):
    template_name = 'anggota/anggota_list.html'
    context_object_name = 'objects'

    def get_queryset(self):
        search = self.request.GET.get('search', None)
        if search:
            object_list = [obj for obj in ika_list if
                           search in obj['nama'].lower() or
                           search in obj['npm'] or
                           search in obj['angkatan']]
        else:
            object_list = ika_list
        return object_list


class AnggotaDetailView(DetailView):
    template_name = 'anggota/anggota_detail.html'
    context_object_name = 'object'

    def get_object(self):
        npm = self.kwargs['npm']
        try:
            obj = [obj for obj in ika_list if obj['npm'] == npm][0]
        except:
            raise Http404('Anggota tidak ditemukan')
        return obj

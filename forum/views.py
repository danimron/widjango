from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    UpdateView,
    View
)
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Thread
from .forms import PostForm
from django.db.models import Q
from django.core.exceptions import PermissionDenied


class ThreadCreateView(LoginRequiredMixin, CreateView):
    model = Thread
    form_class = PostForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        if self.request.user.is_staff:
            form.instance.is_approved = True
        return super(ThreadCreateView, self).form_valid(form)


class ThreadListView(ListView):
    model = Thread
    paginate_by = 10

    def get_queryset(self):
        try:
            search = self.request.GET.get('search',)
        except:
            search = None
        if search:
            query = Q(title__icontains=search)
            query.add(Q(author__userprofile__nama__icontains=search), Q.OR)
            query.add(Q(author__userprofile__npm__icontains=search), Q.OR)
            thread_list = Thread.objects.filter(query)
        else:
            thread_list = Thread.objects.all()
        return thread_list


class ThreadDetailView(DetailView):
    model = Thread


class ThreadUpdateView(LoginRequiredMixin, UpdateView):
    model = Thread
    form_class = PostForm

    def dispatch(self, request, *args, **kwargs):
        if request.user != self.get_object().author:
            raise PermissionDenied
        return super(ThreadUpdateView, self).dispatch(request, *args, **kwargs)


class ThreadDeleteView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        thread = Thread.objects.get(pk=self.kwargs['pk'])
        if self.request.user == thread.author:
            thread.delete()
        else:
            raise PermissionDenied
        return redirect('thread_list')

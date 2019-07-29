from django.views.generic import CreateView, ListView, DetailView
from .models import Thread
from .forms import PostForm


class ThreadCreateView(CreateView):
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


class ThreadDetailView(DetailView):
    model = Thread

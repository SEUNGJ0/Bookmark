from .models import Bookmark
from django.views import generic
from django.urls import reverse_lazy

class BookmarkListView(generic.ListView):
    model = Bookmark
    paginate_by = 5
    template_name = 'bookmark/bookmark_list.html'

class BookmarkCreateView(generic.CreateView):
    model = Bookmark
    fields = ['site_name', 'url']
    success_url = reverse_lazy('list')
    template_name_suffix = '_create'

class BookmarkDetailView(generic.DetailView):
    model = Bookmark

class BookmarkUpdateView(generic.UpdateView):
    model = Bookmark
    fields = ['site_name', 'url']
    template_name_suffix = '_update'

class BookmarkDeleteView(generic.DeleteView):
    model = Bookmark
    success_url = reverse_lazy('list')


from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic import DetailView
from itertools import chain

from blog.models import Post

# Create your views here.

class PostListView(ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class PostDetailView(DetailView):
    model = Post
    

# TODO - Blog search class using Django Class Based View
class PostSearchView(ListView):
    template_name = 'blog/post_search_result.html'
    count = 0

    def get_context_data(self):
        request = self.request
        query = request.GET.get('blogSearch')
        # validate query
        if query is not None:
            print("------------------------------> Searching in blog_database ")
            print("------------------------------>", query)
            blog_result = Post.objects.search(query)
            
            queryset_chain = chain(blog_result)
            qs = shorted(queryset_chain, key=lambda instance: instance.pk, reversed=True)
            self.count = len(qs)
            return qs
        return Post.objects.none()


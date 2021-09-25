from django.db import models
from django.contrib.auth.models import User
from django.db.models import Q
from django.urls import reverse


STATUS = (
    (0, "Draft"),
    (1, "Publish")
)


# Custom search manager
class SearchManager():
    def search(self, query=None):
        qs = self.query
        if query is not None:
            or_lookup = (Q(title__icontains=query))
            qs = qs.filter(or_lookup).distinct()
        return qs

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete = models.CASCADE, related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    #read_time = models.IntegerField(default=5)
    #cover_image = 
    #bottom_imag = 

    objects = SearchManager()

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'slug':str(self.slug)})
    
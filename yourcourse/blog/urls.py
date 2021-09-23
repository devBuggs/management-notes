from django.urls import path



from blog.views import PostListView 

urlpatterns = [
    path('post/', PostListView.as_view(), name='blog-index'),
]
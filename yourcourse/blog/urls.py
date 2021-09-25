from django.urls import path


from blog.views import PostListView, PostDetailView, PostSearchView


app_name = 'blog'
urlpatterns = [
    path('post/', PostListView.as_view(), name='index'),
    path('post/<slug:slug>/', PostDetailView.as_view(), name='post_detail'),
    path('post/search/', PostSearchView.as_view(), name='post_search')
]
from django.urls import path

from .views import QuestionsListView, index_view


app_name = 'interviewapp'
urlpatterns = [
    path('index/', index_view, name='index'),
    path('', QuestionsListView.as_view(), name='interview-questions'),
]
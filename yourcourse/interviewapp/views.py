from django.shortcuts import render
from django.views.generic.list import ListView
from django.utils import timezone

from .models import Question

# Create your views here.
def index_view(request):
    context={
        'brand':"YourCourse.com"
    }
    return render(request, 'interviewapp/base.html', context)

class QuestionsListView(ListView):
    model = Question
    paginate_by = 4 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context



from django.shortcuts import render
from .models import Question, Answer
from django.core.paginator import Paginator


from django.http import HttpResponse 
def qa(request, *args, **kwargs):
    return HttpResponse('OK')


def new_quest(request):
    quest = Question.objects.all()
    q_new = quest.new()
    limit = request.GET.get('limit', 10)
    page = request.GET.get('page', 1)
    paginator = Paginator(q_new, limit)
    paginator.baseurl = '/qa/?page='
    page = paginator.page(page)
    return render(request, 'qa/new_quest.html', {
        q_new: page.object_list,
        paginator: paginator, page: page,
    })


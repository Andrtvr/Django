from django.shortcuts import render
from .models import Question, Answer, QuestionManager
from django.core.paginator import Paginator, EmptyPage



from django.http import HttpResponse 
def qa(request, *args, **kwargs):
    return HttpResponse('OK')


def new_quest(request):
    #quest = Question.objects.all()
    quest = QuestionManager()
    #q_new = quest.new()
    limit = request.GET.get('limit', 10)
    page = request.GET.get('page', 1)
    paginator = Paginator(quest.new(), limit)
    paginator.baseurl = '/?page='
    try:
        page = paginator.page(page)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    return render(request, 'qa/new_quest.html', {
        'quest': page.object_list,
        'paginator': paginator, 'page': page,
    })

def popular(request):
    quest = QuestionManager()
    limit = request.GET.get('limit', 10)
    page = request.GET.get('page', 1)
    paginator = Paginator(quest.popular(), limit)
    paginator.baseurl = 'popular/?page='
    try:
        page = paginator.page(page)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    return render(request, 'popular/popular.html', {
        'quest': page.object_list,
        'paginator': paginator, 'page': page,
    })

def question(request):
    return HttpResponse('123')

def qs_t(request, id='1'):
    return HttpResponse('This is qs_t %s' %id)

from django.shortcuts import render
from django.db import models

#from ask.qa.models import Question

#from .models import Question, Answer, QuestionManager
from django.core.paginator import Paginator, EmptyPage

#def popular(request, *args, **kwargs):
 #  return HttpResponse('OK')
'''

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

'''

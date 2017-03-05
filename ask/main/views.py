from django.core.paginator import Paginator
from django.db import models, connection


def main(request):
    post = Post.objects.get


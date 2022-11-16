from django.http import HttpResponse
from django.http import HttpResponseNotFound
from django.shortcuts import render
from django.core.paginator import Paginator
from . import models


def index(request, user_id: int = 0):
    if user_id <= len(models.USERS):
        user_current = models.USERS[user_id]
    else:
        user_current = models.USERS[0]

    paginator = Paginator(models.QUESTIONS, 3)

    page_number = request.GET.get('page', '1')
    page_obj = paginator.get_page(page_number)

    tags_popular = models.TAGS[:9]
    users_popular = models.USERS[1:9]

    context = {'user': user_current, 'users_popular': users_popular, 'tags_popular': tags_popular, 'page_obj': page_obj}

    return render(request, 'index.html', context=context)


def question(request, question_id: int, user_id: int = 0):
    if user_id <= len(models.USERS):
        user_current = models.USERS[user_id]
    else:
        user_current = models.USERS[0]

    if question_id <= len(models.QUESTIONS):
        question_item = models.QUESTIONS[question_id]
    else:
        return HttpResponseNotFound("Not found")

    paginator = Paginator(question_item['answers'], 3)

    page_number = request.GET.get('page', '1')
    page_obj = paginator.get_page(page_number)

    tags_popular = models.TAGS[:9]
    users_popular = models.USERS[1:9]

    context = {'user': user_current, 'users_popular': users_popular, 'tags_popular': tags_popular, 'question': question_item, 'page_obj': page_obj}

    return render(request, 'question.html', context=context)


def ask(request, user_id: int = 0):
    if user_id <= len(models.USERS):
        user_current = models.USERS[user_id]
    else:
        user_current = models.USERS[0]

    tags_popular = models.TAGS[:9]
    users_popular = models.USERS[1:9]

    context = {'user': user_current, 'users_popular': users_popular, 'tags_popular': tags_popular}

    return render(request, 'ask.html', context=context)


def settings(request, user_id: int = 0):
    if user_id <= len(models.USERS):
        user_current = models.USERS[user_id]
    else:
        user_current = models.USERS[0]

    tags_popular = models.TAGS[:9]
    users_popular = models.USERS[1:9]

    context = {'user': user_current, 'users_popular': users_popular, 'tags_popular': tags_popular}

    return render(request, 'settings.html', context=context)


def register(request, user_id: int = 0):
    if user_id <= len(models.USERS):
        user_current = models.USERS[user_id]
    else:
        user_current = models.USERS[0]

    tags_popular = models.TAGS[:9]
    users_popular = models.USERS[1:9]

    context = {'user': user_current, 'users_popular': users_popular, 'tags_popular': tags_popular}

    return render(request, 'register.html', context=context)


def login(request, user_id: int = 0):
    if user_id <= len(models.USERS):
        user_current = models.USERS[user_id]
    else:
        user_current = models.USERS[0]

    tags_popular = models.TAGS[:9]
    users_popular = models.USERS[1:9]

    context = {'user': user_current, 'users_popular': users_popular, 'tags_popular': tags_popular}

    return render(request, 'login.html', context=context)


def questions_by_tag(request, tag_id: int, user_id: int = 0):
    if user_id <= len(models.USERS):
        user_current = models.USERS[user_id]
    else:
        user_current = models.USERS[0]

    if tag_id <= len(models.TAGS):
        current_tag = models.TAGS[tag_id]
    else:
        return HttpResponseNotFound("Not found")

    questions_filtered = list(filter(lambda x: current_tag in x['tags'], models.QUESTIONS))

    paginator = Paginator(questions_filtered, 3)

    page_number = request.GET.get('page', '1')
    page_obj = paginator.get_page(page_number)

    tags_popular = models.TAGS[:9]
    users_popular = models.USERS[1:9]

    context = {'current_tag': current_tag, 'user': user_current, 'page_obj': page_obj, 'users_popular': users_popular, 'tags_popular': tags_popular}

    return render(request, 'questions_by_tag.html', context=context)

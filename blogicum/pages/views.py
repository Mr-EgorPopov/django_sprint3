from django.shortcuts import render
from django.http import HttpResponse


def about(request) -> HttpResponse:
    """Отрисовка страницы 'О проекте'"""
    template = 'pages/about.html'
    return render(request, template)


def rules(request) -> HttpResponse:
    """Отрисовка страницы 'Наши Правила'"""
    template = 'pages/rules.html'
    return render(request, template)

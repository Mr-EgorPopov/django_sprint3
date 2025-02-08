from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from blog.models import Post, Category

from constants import number_of_limit


def get_published_posts():
    """Получение опубликованных постов"""
    return Post.objects.select_related('category').filter(
        is_published=True,
        category__is_published=True,
        pub_date__lte=timezone.now()
    )


def index(request):
    """Главная страница блога"""
    template = 'blog/index.html'
    post_list = get_published_posts()[:number_of_limit]
    context = {'post_list': post_list}
    return render(request, template, context)


def post_detail(request, post_id):
    """Страница с полной публикацией из блога"""
    template_name = 'blog/detail.html'
    post = get_object_or_404(
        get_published_posts(),
        pk=post_id
    )
    context = {'post': post}
    return render(request, template_name, context)


def category_posts(request, category_slug):
    """Страница с категориями по постам"""
    template = 'blog/category.html'
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True
    )
    post_list = get_published_posts().filter(
        category__slug=category_slug
    )
    context = {'category': category, 'post_list': post_list}
    return render(request, template, context)

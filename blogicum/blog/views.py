from django.shortcuts import render, get_object_or_404

from django.utils import timezone

from blog.models import Post, Category


def index(request):
    """Главная страница блога"""
    template = 'blog/index.html'
    post_list = Post.objects.select_related('category').filter(
        is_published=True,
        category__is_published=True,
        pub_date__lte=timezone.now()
    )[:5]
    context = {'post_list': post_list}
    return render(request, template, context)


def post_detail(request, post_id):
    """Страница с полной публикацией из блога"""
    template_name = 'blog/detail.html'
    post = get_object_or_404(
        (Post.objects.filter(
            pub_date__lte=timezone.now(),
            is_published=True,
            category__is_published=True
        )
        ),
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
    post_list = Post.objects.select_related('category').filter(
        is_published=True,
        category__is_published=True,
        pub_date__lte=timezone.now(),
        category__slug=category_slug
    )
    context = {'category': category, 'post_list': post_list}
    return render(request, template, context)

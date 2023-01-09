from celery import shared_task
from datetime import datetime, timedelta
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from news.models import Post, Category

today = datetime.now()
last_week = today - timedelta(days=7)
post = Post.objects.filter(time_in__gte=last_week)
categories = set(post.values_list('PostCategory__name', flat=True))
subscribers = set(Category.objects.filter(name__in=categories).values_list('subscribers__email', flat=True))


# Еженедельная отправка писем
@shared_task
def my_job():
    # Ваша логика обработки заданий здесь...
    html_content = render_to_string(
        'daily_post.html',
        {
            'Link': settings.SITE_URL,
            'posts': post,
        }
    )
    msg = EmailMultiAlternatives(
        subject='Статьи за неделю',
        body='',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=subscribers,
    )
    msg.attach_alternative(html_content, 'text/html')
    msg.send()


    # html_content = render_to_string(
    #     'daily_post.html',
    #     {
    #         'link': settings.SITE_URL,
    #         'posts': post,
    #     }
    # )
    # msg = EmailMultiAlternatives(
    #     subject='Статьи за неделю',
    #     body='',
    #     from_email=settings.DEFAULT_FROM_EMAIL,
    #     to=subscribers,
    # )
    # msg.attach_alternative(html_content, 'text/html')
    # msg.send()


# Отправка писем при создании поста
@shared_task
def send_notifications(preview, pk, heading, subscribers, id):
    html_content = render_to_string(
        'post_created_email.html',
        {
            'text': preview,
            'Link': f'{settings.SITE_URL}/news/{pk}'
        }
    )

    msg = EmailMultiAlternatives(
        subject=heading,
        body='',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=subscribers,
    )

    msg.attach_alternative(html_content, 'text/html')
    msg.send()

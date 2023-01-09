from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.db.models.signals import m2m_changed, post_save
from django.dispatch import receiver
from django.template.loader import render_to_string
from .tasks import send_notifications
from news.models import PostCategory, Post


@receiver(post_save, sender=Post)
def notify_about_new_post(sender, instance, created, **kwargs):
    if created and instance.__class__.__name__ == 'Post':
        categories = instance.PostCategory.all()
        subscribers: list[str] = []
        for category in categories:
            subscribers += category.subscribers.all()

        subscribers = [s.email for s in subscribers]

        send_notifications.apply_async((instance.preview(), instance.pk, instance.heading, subscribers, instance.id),
                                       countdown=10)

# def send_notifications(preview, pk, heading, subscribers):
#     html_content = render_to_string(
#         'post_created_email.html',
#         {
#             'text': preview,
#             'Link': f'{settings.SITE_URL}/news/{pk}'
#         }
#     )
#
#     msg = EmailMultiAlternatives(
#         subject=heading,
#         body='',
#         from_email=settings.DEFAULT_FROM_EMAIL,
#         to=subscribers,
#     )
#
#     msg.attach_alternative(html_content, 'text/html')
#     msg.send()


# @receiver(m2m_changed, sender=PostCategory)
# def notify_about_new_post(sender, instance, **kwargs):
#     if kwargs['action'] == 'post_add':
#         # print('Сигнал')
#         categories = instance.PostCategory.all()
#         subscribers: list[str] = []
#         for category in categories:
#             subscribers += category.subscribers.all()
#
#         subscribers = [s.email for s in subscribers]
#
#         send_notifications(instance.preview(), instance.pk, instance.heading, subscribers, )

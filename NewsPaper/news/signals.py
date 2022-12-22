from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from django.template.loader import render_to_string

from news.models import PostCategory


def send_notifications(preview, pk, heading, subscribers):
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


@receiver(m2m_changed, sender=PostCategory)
def notify_about_new_post(sender, instance, **kwargs):
    if kwargs['action'] == 'post_add':
        # print('Сигнал')
        categories = instance.PostCategory.all()
        subscribers: list[str] = []
        for category in categories:
            subscribers += category.subscribers.all()

            subscribers = [s.email for s in subscribers]

            send_notifications(instance.preview(), instance.pk, instance.heading, subscribers, )

from django.apps import AppConfig
import redis
import os


class NewsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'news'

    def ready(self):
        import news.signals


red = redis.Redis(
    host=os.getenv('redis_localhost'),
    port=os.getenv('redis_port'),
    password=os.getenv('redis_password'),
)

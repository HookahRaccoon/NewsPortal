from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum
from django.urls import reverse


class Author(models.Model):
    authorUser = models.OneToOneField(User, on_delete=models.CASCADE)
    reting_author = models.SmallIntegerField(default=0)

    def __str__(self):
        return f'{self.authorUser}'

    def update_reting(self):
        postRat = self.post_set.aggregate(postReting=Sum('reting_news'))
        pRat = 0
        pRat += postRat.get('postReting')

        commentRat = self.authorUser.comment_set.aggregate(commentReting=Sum('reting'))
        cRat = 0
        cRat += commentRat.get('commentReting')

        self.reting_author = pRat * 3 + cRat
        self.save()


class Category(models.Model):
    objects = None
    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return f'{self.name}'


class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    NEWS = 'NW'
    ARTICLE = 'AR'
    CATEGORY_CHICES = [
        (NEWS, 'Новость'),
        (ARTICLE, 'Статья'),
    ]
    categoryType = models.CharField(max_length=2,
                                    choices=CATEGORY_CHICES,
                                    default=ARTICLE)
    time_in = models.DateTimeField(auto_now_add=True)
    PostCategory = models.ManyToManyField(Category, related_name='news', through='PostCategory')
    heading = models.CharField(max_length=128)
    text = models.TextField()
    reting_news = models.SmallIntegerField(default=0)

    def preview(self):
        return self.text[0:123] + '...'

    def like(self):
        self.reting_news += 1
        self.save()

    def dislike(self):
        self.reting_news -= 1
        self.save()

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])

    def __str__(self):
        return f'{self.text}'


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.category}'


class Comment(models.Model):
    commentPost = models.ForeignKey(Post, on_delete=models.CASCADE)
    commentUser = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    time_in = models.DateTimeField(auto_now_add=True)
    reting = models.SmallIntegerField(default=0)

    def like(self):
        self.reting += 1
        self.save()

    def dislike(self):
        self.reting -= 1
        self.save()

    def __str__(self):
        return f'{self.text}'

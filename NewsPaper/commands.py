from news.models import *

u1 = User.objects.create_user('Dima')
u2 = User.objects.create_user('Julia')
u3 = User.objects.create_user('Andrei')

Author.objects.create(authorUser=u1)
Author.objects.create(authorUser=u3)

Category.objects.create(name='IT')
Category.objects.create(name='AUTO')
Category.objects.create(name='SCIENCE"')
Category.objects.create(name='MAIN')

Post.objects.create(author=Author, categoryType='NW', heading='sometitle', text='somebigtext')
Post.objects.create(author=Author, categotyType='NW', heading='MyTitle', text='HelloWorld')
Post.objects.create(author=Author, categoryType='AR', heading='Article', text='Всем привет')
Post.objects.create(author=Author, categoryType='AR', heading='Problems', text='Its ok')

Comment.objects.create(commentPost=Post.objects.get(id=1), commentUser=Author.objects.get(id=1).authorUser,
                       text='anytextbyauthor')
Comment.objects.create(commentPost=Post.objects.get(id=1), commentUser=Author.objects.get(id=1).authorUser, text='Good')
Comment.objects.create(commentPost=Post.objects.get(id=2), commentUser=Author.objects.get(id=3).authorUser, text='Like')
Comment.objects.create(commentPost=Post.objects.get(id=3), commentUser=Author.objects.get(id=3).authorUser, text='cool')
Comment.objects.create(commentPost=Post.objects.get(id=4), commentUser=Author.objects.get(id=1).authorUser,
                       text='great, very good')

Comment.objects.get(id=1).like()
Comment.objects.get(id=2).like()
Comment.objects.get(id=2).like()
Comment.objects.get(id=3).dislike()
Comment.objects.get(id=3).dislike()
Comment.objects.get(id=4).like()
Comment.objects.get(id=4).dislike()

Post.objects.get(id=1).like()
Post.objects.get(id=2).dislike()
Post.objects.get(id=2).like()
Post.objects.get(id=3).like()
Post.objects.get(id=4).dislike()
Post.objects.get(id=4).like()
Post.objects.get(id=4).like()

Author.objects.get(id=1).update_reting()
Author.objects.get(id=2).update_reting()

a = Author.objects.order_by('-reting_author')[:1]
for i in a:
    i.reting_author
    i.authorUser.username

b = Post.objects.order_by('-reting_news')[:1]
for v in b:
    v.time_in
    v.author.authorUser
    v.reting_news
    v.heading
    v.preview()

c = Comment.objects.order_by('-commentPost.reting_news')[:1]
for x in c:
    x.time_in
    x.commentUser.username
    x.reting
    x.text
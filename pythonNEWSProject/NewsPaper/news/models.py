from django.contrib.auth.models import User
from django.db import models
from django.db.models import Sum
from django.urls import reverse


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    reyting_author = models.IntegerField(default=0)

    def update_rating(self):
        reytSoobsh = self.post_set.aggregate(raytingSoobsh=Sum('reyting_post'))
        rSoob = 0
        rSoob += reytSoobsh.get('raytingSoobsh')

        reytComment = self.user.comment_set.aggregate(raytingComment=Sum('reyting_comment'))
        rComm = 0
        rComm += reytComment.get('raytingComment')

        self.reyting_author = rSoob * 3 + rComm
        self.save()


class Category(models.Model):
    category_name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.category_name.title()

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    novost = 'NW'
    statia = 'AR'
    Vybor_soobsh = (
        (novost, 'Новость'),
        (statia, 'Статья'),
    )
    type_soobsh = models.CharField(max_length=2, choices=Vybor_soobsh, default=novost)
    vremia_sosdania_soobsh = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField(Category, through='PostCategory', related_name='posts')
    zagolovok = models.CharField(max_length=64)
    tekst = models.TextField()
    reyting_post = models.IntegerField(default=0)

    def like(self):
        self.reyting_post += 1
        self.save()

    def dislike(self):
        self.reyting_post -= 1
        self.save()

    def preview(self):
        return (self.tekst[:20]) + '...'

    def __str__(self):
        return f'{self.zagolovok.title()}: {self.preview()}'

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tekst_comment = models.TextField(max_length=256)
    time_in_comment = models.DateTimeField(auto_now_add=True)
    reyting_comment = models.IntegerField(default=0)

    def like(self):
        self.reyting_comment += 1
        self.save()

    def dislike(self):
        self.reyting_comment -= 1
        self.save()


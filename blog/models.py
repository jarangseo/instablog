#blog/models.py
from django.db import models
from django.conf import settings
# from django.auth.models import User -> 나중에 해주신댔음!

class Category(models.Model):
    name = models.CharField(max_length=40)

# Create your models here.
class Post(models.Model):
	#blog_post
	#처럼 각각의 모델들은 앱 단위로 관리된다 그래서 이름이 겹칠 수 없다 돈워리!
	# user = models.ForeignKey(settings.AUTH_USER_MODEL) -> 나중에 해주신댔음!
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=200, db_index=True)
    content = models.TextField()
    tags = models.ManyToManyField('Tag', blank=True)
    # categorys = models.ManyToManyField('Category')
    #category = models.ForeignKey('Category')
    #문자열로 연결할 대상을 연결하면 장고가 나중에 평가해서 관계를 맺어줌..뭔말일까..
    created_at = models.DateTimeField(auto_now_add=True)
    #auto_now_add는 처음 데이터가 생성됐을 때 그 시점의 생성일시가 자동으로 들어감
    updated_at = models.DateTimeField(auto_now=True)
    #auto_now는 정보가 들어가는 시점의 생성일시가 자동으로 들어감

    is_model_field = False

    class Meta:
    	ordering = ('-updated_at', '-pk',)

    def __str__(self):
        # return '<Post : {}'.format(self.pk)
        return '{} - {}'.format(self.pk,self.title)

class Comment(models.Model):
    post = models.ForeignKey(Post)
    content = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        # return '<Post : {}'.format(self.pk)
        return '{} of {}'.format(self.pk,self.post.pk)

class Tag(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


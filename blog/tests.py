from django.test import TestCase
from django.db import transaction
from django.db.utils import IntegrityError
from django.contrib.auth import get_user_model

from .models import Post
from .models import Category

class PostModelTest(TestCase):
	def setUp(self):
		self.user = User()
		self.user
		create_user(username='kay', password='12345678')

	def test_create_post_by_model(self):
		new_post = Post()
		new_post.title

# class PostModelTest(TestCase):
	# def add_number(self):
	# 	self.assertEqual(1,1)
		#1과 2과 같다고 단언한다 라는 뜻의 테스트케이스

	# def test_add_number(self):
	# 	result = self.add_number(10,20)
	# 	expected = 30
	# 	self.assertEqual(result, 1)

class PostModelTest(TestCase):
	def test_create_post_by_model(self):
		new_post = Post()
		new_post.title = 'hello world'
		new_post.content = 'lerem ipsum'

		with transaction.atomic()
			with self.assertRaises(IntegrityError):
				new_post.save()
		self.assertIsNone(new_post.pk)

		# self.assertTrue(isinstance(new_post.pk, int))
		#글이 제대로 저장되어있지 않으면 assertTrue를 통과하지 못한다

class PhotoModelTest(TestCase):
    def test_import_post_model(self):
        Post = None
        try:
            from blog.models import Post
        except ImportError:
            pass

        self.assertIsNotNone(Post)

    def test_save_post_by_model(self):
        '''Post 모델을 이용해 데이터를 저장하는 테스트.
        검증 방법 : 저장한 뒤 모델 매니저로 저장한 데이터를 가져와서 비교
        '''
        pass

    def test_failed_save_post_by_model(self):
        '''Post 모델을 이용해 데이터를 저장할 때 실패하는 경우에 대한 테스트
        '''
        pass

    def test_get_post_by_url(self):
        '''Django Test Client를 이용해 특정 게시물을 보는 url로 접근하는 테스트
        '''
        pass

    def test_failed_get_post_by_url(self):
        '''Django Test Client를 이용해 특정 게시물을 보지 못하고
        실패하는 경우에 대한 테스트
        '''
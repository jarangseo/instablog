#blog/forms.py

#form 은 그냥 장고에 있음
from django import forms
from django.forms import ValidationError

from .models import Post


class PostForm(forms.Form):
	title = forms.CharField(
		required=True, label='글 제목', help_text='성심성의껏 작성해주세용ㅎ'
	)
	content = forms.CharField(widget=forms.Textarea)

class PostEditForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('title', 'category', 'content', 'tags',)
		#사용할 모델필드들을 문자열로 나열
		# fileds = '__all__'
		# exclude = ('title', 'category')

	def clean_title(self):
		title = self.cleaned_data.get('title', '')
		if '바보' in title:
			raise ValidationError('바보스러운 기운이 느껴지는데?!')
		return title.strip()
		# content = self.cleaned_data.get('content')

	def clean(self):
		super(PostEditForm, self).clean()
		title = self.cleaned_data.get('title','')
		content = self.cleaned_data.get('content','')

		if '안녕' in title:
			self.add_error('title', '안녕은 이제 그만 안녕 title')
		if '안녕' in content:
			self.add_error('title', '안녕은 이제 그만 안녕 content')

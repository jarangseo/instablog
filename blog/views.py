# blog/views.py
from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.core.paginator import PageNotAnInteger
from django.core.paginator import EmptyPage
from django.contrib.auth.decorators import login_required

from .models import Post
from .models import Category
from .forms import PostEditForm


def hello(request):
    res = HttpResponse('hello world')
    return res


def hello_with_template(request):
    return render(request, 'hello.html')


def list_posts(request):
    per_page = 2
    current_page = request.GET.get('page', 1)

    all_posts = Post.objects \
            .select_related() \
            .prefetch_related() \
            .all().order_by('-pk')

    pagi = Paginator(all_posts, per_page)
    try:
        pg = pagi.page(current_page)
    except PageNotAnInteger:
        pg = pagi.page(1)
    except EmptyPage:
        pg = []

    return render(request, 'list_posts.html', {
        'posts': pg,
    })


def view_post(request, pk):
    the_post = get_object_or_404(Post, pk=pk)

    return render(request, 'view_post.html', {
        'post': the_post,
    })

@login_required
def create_post(request):
	#로그인 한 유저만 글을 작성할 수 있도록 수정해보쟈
	#로그인을 했으면 true, 안했으면 false
	# if not request.user.is_authenticated():
	# 	raise Exception('누구세요?')
	#@login_required가 있으므로 위의 두줄은 지워두 된다

    categories = Category.objects.all()

    if request.method == 'GET':
        form = PostEditForm()
    elif request.method == 'POST':
    	# request.user 에 현재 접속한 user의 정보가 들어가있음
        form = PostEditForm(request.POST)
        if form.is_valid():
        	new_post = form.save(commit=False)
        	#commit을 False로 하면 모델의 인스턴스객체만 받아내고 db에 반영은 안한다
        	new_post.user = request.user
        	new_post.save(commit=True)
        	return redirect('view_post', pk=new_post.pk)

        	#
        	#new_post = form.save()
        	#위의 한줄로 아래의 코드들을 대체
            # new_post = Post()
            # new_post.title = form.cleaned_data.get('title')
            # new_post.content = form.cleaned_data['content']

            # category_pk = request.POST.get('category')
            # category = get_object_or_404(Category, pk=category_pk)
            # new_post.category = category
            # new_post.save()
            #





    return render(request, 'create_post.html', {
        'categories': categories,
        'form': form,
    })
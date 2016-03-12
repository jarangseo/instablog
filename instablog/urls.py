"""instablog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.views import login as django_login
#django가 제공하는 login view함수를 import하기
from django.contrib.auth.views import logout as django_logout
#django가 제공하는 logout view함수를 import하기
from django.conf import settings

# from blog.views import hello
# from blog.views import hello_with_template
from blog import views as blog_views

urlpatterns = [
	# url(r'^$', hello),
	# url(r'^hello/$', hello_with_template),
	url(r'^post/create/$', blog_views.create_post, name='create_post'),
	url(r'^$', blog_views.list_posts),
	# url(r'^posts/(?P<pk>[0-9]+)/$', blog_views.view_post),
	url(
		r'^posts/(?P<pk>[0-9]+)/$',blog_views.view_post, name='view_post'
	),
	url(r'^hello/$', blog_views.hello_with_template),
	url(r'^admin/', admin.site.urls),
	# url(r'^login/$', django_login, name), 이렇게 해도되는데 아래의 방법이 더 유연한 방법이다
	# settings에 있는 것을 그대로 가져오는 것
	url(
		r'^{}$'.format(settings.LOGIN_URL[1:]),
		django_login,
		{'template_name': 'login.html'},
		name='login_url',
	),
	url(
		r'^{}$'.format(settings.LOGOUT_URL[1:]),
		django_logout,
		{'next_page': settings.LOGIN_URL},
		name='logout_url',
	),
]

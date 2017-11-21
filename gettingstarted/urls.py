from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()
from django.contrib.auth import views as auth_views

import hello.views


# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^$', hello.views.index, name='index'),
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^accounts/profile/$', hello.views.profile, name='profile'),
    url(r'^dashboard/$', hello.views.main_page, name='dashboard'),
    url(r'^dashboard/exams/$', hello.views.exams, name='exams'),
    url(r'^dashboard/exams/create/$', hello.views.create_exam, name='create-exam'),
    url(r'^dashboard/question-bank/$', hello.views.questions, name='question-bank'),
    url(r'^dashboard/candidates/$', hello.views.cadidates, name="candidates"),
    url(r'^db', hello.views.db, name='db'),
    url(r'^admin/', include(admin.site.urls))
]

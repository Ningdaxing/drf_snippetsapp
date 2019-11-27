# from django.conf.urls import url
# from snippetsapp import views
#
#第一种类型
# urlpatterns = [
#     url(r'^snippets/$', views.snippet_list),
#     url(r'^snippets/(?P<pk>[0-9]+)/$', views.snippet_detail),
# ]

#第二种类型加format=None的
# from django.conf.urls import url
# from rest_framework.urlpatterns import format_suffix_patterns
# from snippetsapp import views
#
# urlpatterns = [
#     url(r'^snippets/$', views.snippet_list),
#     url(r'^snippets/(?P<pk>[0-9]+)/$', views.snippet_detail),
# ]
#
# #加上def snippet_list(request, format=None)
# urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'html'])

#APIVIEW的
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from snippetsapp import views

urlpatterns = [
    url(r'^snippets/$', views.SnippetList.as_view(), name='snippet-list'),
    url(r'^snippets/(?P<pk>[0-9]+)/$', views.SnippetDetail.as_view(), name='snippet-detail'),
    url(r'^users/$', views.UserList.as_view(), name='user-list'),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view(), name='user-detail'),
    url(r'^snippets/(?P<pk>[0-9]+)/highlight/$', views.SnippetHighlight.as_view(), name='snippet-Higelight'),
    url(r'^$', views.api_root),
]

#加上def snippet_list(request, format=None)
urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'html'])


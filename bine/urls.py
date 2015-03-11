# -*- coding: UTF-8 -*-
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from bine import views
from bine.views import BookList, IndexView, BookDetail, UserView, \
    FriendView, SchoolView, BookNoteView, AuthView


urlpatterns = [
    url(r'^api/note/$', BookNoteView.as_view()),
    url(r'^api/note/(?P<pk>[0-9]+)/$', BookNoteView.as_view()),
    # url(r'^api/note/(?P<note_id>[0-9]+)/reply/$', BookNoteReplyList.as_view()),
    # url(r'^api/note/(?P<note_id>[0-9]+)/reply/(?P<reply_id>[0-9]+)/$', BookNoteReplyDetail.as_view()),
    # url(r'^api/note/(?P<note_id>[0-9]+)/likeit/$', BookNoteLikeItUpdate.as_view()),
    url(r'^api/book/$', BookList.as_view()),
    url(r'^api/book/(?P<pk>[0-9]+)/$', BookDetail.as_view()),
    url(r'^api/book/isbn13/(?P<isbn13>[0-9a-zA-Z]+)/$', BookDetail.as_view()),
    url(r'^api/friend/$', FriendView.as_view()),
    url(r'^api/friend/(?P<pk>[0-9]+)/$', FriendView.as_view()),
    url(r'^api/user/$', UserView.as_view()),  # duplication check
    url(r'^api/user/(?P<pk>[0-9]+)/$', UserView.as_view()),
    url(r'^api/school/', SchoolView.as_view()),

    url(r'^api/auth/refresh/$', 'rest_framework_jwt.views.refresh_jwt_token'),
    url(r'^api/auth/(?P<action>[a-z]+)/$', AuthView.as_view()),

    url(r'^.*$', IndexView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
from django.contrib import admin
from django.urls import path,include

from . import views

from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', views.PostList.as_view()),
    path('<int:pk>',views.PostDetails.as_view())
]


urlpatterns=format_suffix_patterns(urlpatterns)
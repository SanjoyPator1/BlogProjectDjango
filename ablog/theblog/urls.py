
from theblog.models import Category
from django.urls import path
from .views import HomeView, ArticleDetailView, AddPostView,UpdatePostView, DeletePostView,AddCategoryView, CategoryView, CategoryListView, LikeView,ALLDocsView

#summer try
from django.conf import settings
from django.urls import re_path, include
from django.conf.urls.static import static
from django.contrib import admin
from theblog.views import index

urlpatterns = [
    # path('index/', index, name='index'),
    path('', HomeView.as_view(), name="home"),
    path('all_docs', ALLDocsView.as_view(), name="all_docs"),
    path('article/<int:pk>', ArticleDetailView.as_view(), name="article-detail"),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('add_category/', AddCategoryView.as_view(), name='add_category'),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name='update_post'),
    path('article/<int:pk>/remove', DeletePostView.as_view(), name='delete_post'),
    path('category/<str:cats>/', CategoryView, name='category'),
    path('category-list/', CategoryListView, name='category-list'),
    path('like/<int:pk>', LikeView, name='like_post')
]

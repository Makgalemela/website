
from django.urls import path
from . import views
from .views import UserPostListView, PostListView , PostDetailView,PostCreateView,PostUpdateView, PostDeleteView


urlpatterns = [

     path('home/', PostListView.as_view(template_name = 'index/index.html') , name='index-home'),
     path('user/<str:username>', UserPostListView.as_view(template_name = 'index/user_post.html') , name='index-userpost'),
     path('post/<int:pk>/', PostDetailView.as_view(template_name='index/detail.html') , name='index-detail'),
     path('post/<int:pk>/update/', PostUpdateView.as_view() , name='index-update'),
     path('post/<int:pk>/delete/', PostDeleteView.as_view() , name='index-delete'),
     path('post/new/', PostCreateView.as_view() , name='index-create'),
     path('', views.index , name='index-base'),
     path('about/', views.about, name='index-about')
 ]
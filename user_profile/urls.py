from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home-page'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('user_profile/', views.profile_view, name='user_profile'),
    path('id_user_profile/<int:user_id>/', views.id_profile_view, name='id_user_profile'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('post/', views.PostView, name='post'),
    path('your_post/', views.YourPostView, name='your_post'),
    path('create_post/', views.create_post, name='create_post'),
    path('article_detail/<int:pk>/', views.ArticleDetailView, name='article_detail'),
    path('like/<int:pk>/', views.LikeView, name='like_post'),
    path('post/delete/<int:post_id>/', views.delete_your_post, name='delete_your_post'),
    path('post/update/<int:post_id>/', views.update_your_post, name='update_your_post'),
    path('comment/update/<int:comment_id>/', views.update_comment, name='update_comment'),
    path('comment/delete/<int:comment_id>/', views.delete_comment, name='delete_comment'),

]

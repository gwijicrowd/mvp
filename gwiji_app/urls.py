from django.urls import path, include
from django.contrib import admin
from . import views 


urlpatterns = [
    path('', views.index, name='index'),
    path('campaigns/<int:id>/', views.campaigns, name='campaigns'),
    path('user_profile/<int:id>/', views.user_profile, name='user_profile'),
    path('campaigns/<int:id>/post', views.discussion_post, name='discussion_post'),
    path('campaigns/<int:id>/process_payment', views.process_payment, name='process_payment'),
    path('login', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup', views.signup, name='signup'),
    path('browse/', views.browse, name='browse'),
    path('feeds/', views.feeds, name='feeds'),
    path('manage_campaigns/', views.manage_campaigns, name='manage_campaigns'),
    path('following/', views.following, name='following'),
    path('financials/', views.financials, name='financials'),
    path('notifications/', views.notifications, name='notifications'),
    path('profile/', views.profile, name='profile'),
    path('follow_campaign/<int:campaign_id>/', views.follow_campaign, name='follow_campaign'),
    path('discussion_post/<int:campaign_id>/', views.discussion_post, name='discussion_post'),
    path('like_post/<int:post_id>/', views.like_post, name='like_post'),
    path('comment/<int:post_id>/', views.comment, name='comment'),
    path('save_profile/', views.save_profile, name='save_profile'),
    path('post/', views.post, name='post'),
    path('browse/post', views.post, name='browse_post'),
    path('following/post', views.post, name='following_post'),
    path('manage_campaigns/post', views.post, name='manage_campaigns_post'),
    path('financials/post', views.post, name='financials_post'),
    path('notifications/post', views.post, name='notifications_post'),
    path('profile/post', views.post, name='profile_post'),
    path('manage_campaigns/create_campaign', views.create_campaign, name='create_campaign'),
    path('company/', views.company, name='company'),
    path('verify_id', views.verify_id, name='verify_id'),
    
    
]
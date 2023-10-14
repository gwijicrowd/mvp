from django.urls import path, include
from django.contrib import admin
from . import views 


urlpatterns = [
    path('', views.index, name='index'),
    path('campaigns/<int:id>/', views.campaigns, name='campaigns'),
    path('campaigns/<int:id>/post', views.discussion_post, name='discussion_post'),
    path('campaigns/<int:id>/process_payment', views.process_payment, name='process_payment'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
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
    path('manage_campaigns/create_campaign/', views.create_campaign, name='create_campaign'),
    path('company/', views.company, name='company'),
    
    
]
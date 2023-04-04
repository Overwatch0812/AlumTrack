from django.urls import path
from . import views


urlpatterns=[
    path('',views.home,name='home'),
    path('logout',views.logout,name='logout'),
    path('events',views.events,name='events'),
    path('blog',views.blog,name='blog'),
    path('contact',views.contact,name='contact'),
    path('findalumni',views.findalumni,name='findalumni'),
    path('searchalumni',views.searchalumni,name='searchalumni'),
    path('profile',views.profile,name='profile'),
    path('edit_profile',views.edit_profile,name='edit_profile'),
    path('userdetail/<int:id>',views.userdetail,name='userdetail'),
]
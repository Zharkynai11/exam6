"""exam6 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from accounts.views import *
from webapp.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('accounts.urls', 'accounts')),
    path('login', login_view, name='login'),
    path('logout', logout_view, name='logout'),
    path('', PostListView.as_view(), name='index'),
    path('post/<int:pk>',PostDetailView.as_view(),name='post_detail'),
    path('post_delete/<int:pk>',delete_post_view,name='post_delete'),
    path('<int:pk>/update', PostUpdateView.as_view(), name='post_update'),
    path('post_create',create_post_view, name= 'post_create'),
    path('users', UserListView.as_view(), name='user_list'),
    path('user/<int:pk>',UserDetailView.as_view(),name='user_detail'),
    path('<int:pk>/update_user', UserUpdateView.as_view(), name='user_update'),
    #path('', login_view,name = 'login'),
    #path('login', login_view)
    #path('', include('webapp.urls', 'webapp')),
    ]

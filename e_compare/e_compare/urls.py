"""e_compare URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from blog import views as e_compare_views
from accounts.views import (login_view, register_view,logout_view)
urlpatterns = [
    url(r'^admin/', admin.site.urls),

	#user urls
	
# 	url(r'^accounts/login/$', e_compare_views.login),
# 	url(r'^accounts/logout/$', e_compare_views.logout),
# 	url(r'^accounts/auth/$', e_compare_views.auth_view),
# 	url(r'^accounts/loggedin/$', e_compare_views.loggedin),
# 	url(r'^accounts/invalid/$', e_compare_views.invalid_login),
    url(r'^login/', login_view,name='login'),
    url(r'^logout/', logout_view,name='logout'),
    url(r'^register/', register_view,name='register'),




]

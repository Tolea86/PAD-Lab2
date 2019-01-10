"""django_mongo URL Configuration

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
from django.conf.urls import url, include
from django.contrib import admin

from users.urls import router as user_router
from posts.urls import router as post_router
from posts.urls import user_posts

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^api/v1/', include(user_router.urls)),
    url(r'^api/v1/', include(post_router.urls)),
    url(r'^api/v1/', include(user_posts.urls)),
]

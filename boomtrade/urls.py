"""boomtrade URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import login, logout
from django.views.generic.base import TemplateView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/', login, name='login'),
    url(r'^logout/', logout, name='logout'),
    url(r'^', include('main.urls'), name='main'),
    url(r'^guestbook/', include('guestbook.urls'), name='guestbook'),
    url(r'^news/', include('news.urls'), name='news'),
    url(r'^imagepool/', include('imagepool.urls'), name='imagepool'),
    url(r'^categories/', include('categories.urls'), name='categories'),
    url(r'^goods/', include('goods.urls'), name='goods'),
    url(r'^blog/', include('blog.urls'), name='blog'),
    url(r'^about/', TemplateView.as_view(template_name='static_pages/about.html'), name='about'),
    url(r'^howtobuy/', TemplateView.as_view(template_name='static_pages/how_to_buy.html'), name='howtobuy'),
    url(r'^contacts/', TemplateView.as_view(template_name='static_pages/contacts.html'), name='contacts'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

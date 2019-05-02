"""django_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.urls import path
from . import views
from django.conf.urls import url
from .views import HelloView

urlpatterns = [
    #### 関数による書き方 ####
    # path('', views.index, name="index"),
    # path('<int:id>/<nickname>/', views.index, name="index"),
    # path('my_name_is_<nickname>.I_am_<int:age>_years_old.', views.index, name='index'),
    # path('', views.index, name="index"),
 #   path('next', views.next, name="次のページへ"),
 #   path('', views.index2, name="index12"), # name="ここが{% urlの後の%}に効いてくる"
 #   path('form', views.form, name="form"),
    #### class による書き方 ####
    url(r"",HelloView.as_view(),name="index"),
]

from django.conf.urls import url

from lyricfy_app import views

urlpatterns = [
    url(r'^Inici/$', views.Home, name="home"),
    url(r'^Registre/$', views.Register.as_view(), name="registre"),
]

from django.conf.urls import url
from . import views

app_name = 'blogg'

urlpatterns = [
        url(r'^$', views.index, name = "index"),
        url(r'^signup$', views.signup, name = "signup"),
        url(r'^logout$', views.logout_user, name = "logout"),
        url(r'^login$', views.login_user, name = "login"),
        url(r'^newpost$', views.add_post, name = "add_post"),
        url(r'^viewposts$', views.view_posts, name = "view_posts"),
]

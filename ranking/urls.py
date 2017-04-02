from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    url(r'^joueur/(?P<joueur_id>[0-9]+)/$', views.detail_joueur, name='joueur'),
    url(r'^annuler/(?P<match_id>[0-9]+)/$', views.annuler_match, name='annuler'),
    url(r'^traiter_match/$', views.traiter_match, name='traiter_match'),
    url(r'^login/$', auth_views.login, {'template_name':'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'^recalculate/$', views.recalculate, name='recalculate'),
    url(r'^matchs/$', views.all_matchs, name='matchs'),
    url(r'^$', views.index, name='index'),
]

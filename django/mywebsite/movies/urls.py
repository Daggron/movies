from django.conf.urls import url
from .import views
app_name='movie'
urlpatterns=[
    url(r'^$',views.IndexView.as_view(),name='index'),

    url(r'^register/$',views.UserFormView.as_view(),name='register'),

    url(r'^(?P<pk>[0-9]+)/$', views.DetailsView.as_view(), name='detail'),

    url(r'movies/add/$', views.add_Movies.as_view(), name='movies_add'),

    url(r'movies/(?P<pk>[0-9]+)/$', views.Update_Movies.as_view(), name='movies_update'),

    url(r'movies/(?P<pk>[0-9]+)/delete/$', views.Delete_Movies.as_view(), name='movies_del'),
]
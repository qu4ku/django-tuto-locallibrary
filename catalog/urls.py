from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    # Class view
    url(r'^books/$', views.BookListView.as_view(), name='books'),
]
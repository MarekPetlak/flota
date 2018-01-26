from django.conf.urls import url
from . import views

app_name = 'cars'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name="index"),
    url(r'^car/(?P<pk>\d+)$', views.DetailView.as_view(), name="car-detail"),
    url(r'^add$', views.CreateView.as_view(), name="car-add"),
    url(r'^car/update/(?P<pk>\d+)$', views.UpdateView.as_view(), name="car-update"),
    url(r'^car/delete/(?P<pk>\d+)$', views.DetailView.as_view(), name="car-delete"),

    url(r'^capacity/$', views.capacity_index, name="capacities-index"),
    url(r'^capacity/add$', views.capacity_add, name="capacity-add"),


    url(r'^register/$', views.UserFormView.as_view(), name='register'),
    #url(r'^login/$', views.login_user, name='login'),
    #url(r'^logout/$', views.logout_user, name='logout'),


]
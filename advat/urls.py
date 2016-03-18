from advat import views
from django.conf.urls import url
from django.views.generic import TemplateView


urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='pages/home.html'), name="home"),
    url(r'^about/$', TemplateView.as_view(template_name='pages/about.html'), name="about"),



    url(r'^post/$', views.post, name='post'),
    url(r'^profile/(?P<shop>[\w-]+)/$', views.archive, name="profile"),
     url(r'^post/profile/(?P<shop>[\w-]+)/$', views.archive),

    url(r'^api/$', views.ApiList.as_view()),
    url('^api/category/(?P<category>.+)/$', views.CategoryList.as_view()),
    url('^api/location/(?P<location>.+)/$', views.LocationList.as_view()),
    url('^api/(?P<location>.+)/(?P<category>.+)/$', views.LocationCategoryList.as_view()),

]

from django.conf.urls import url
from . import views
from .views import *
from django.conf import settings
from django.conf.urls.static  import static


urlpatterns= [
   url('^$',views.signup, name='signup'),
   url('^index$', views.index, name='index'),
   url('^upload/', views.upload, name='upload'),
   url(r'^update_profile/', views.update_profile, name='update_profile'),
   url(r'^accounts/profile/', views.profile, name='profile')


  



]

if settings.DEBUG:
   urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
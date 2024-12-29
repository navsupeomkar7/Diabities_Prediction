from django.urls import path,include
from . import views

urlpatterns = [
#    path('',views.index, name='index'),
#    path('about',views.About, name='about'),
#    path('i',views.contactus,name='contactus'),
#    path('ii',views.about,name='about')

path('',views.index,name='index'),
path('register/',views.register, name='register'),
path('login_view/',views.login_view,name='login_view'),
path('about/',views.about,name='about'),
path('contact/',views.contact,name='contact'),
path('predict/',views.predict,name='predict'),
path('result',views.result,name='result'),
path('logout1',views.logout1,name='logout1'),

]

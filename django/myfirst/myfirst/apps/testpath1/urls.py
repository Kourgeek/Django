from django.urls import path

from . import views

urlpatterns = [
	path('',views.index,name='index'),
	path('testnum1',views.testnum1, name='test')
]
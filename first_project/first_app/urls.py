from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='views1'),
    path('about',views.about_me,name='about_me'),
    path('<age>',views.age_page,name='about_age'),
    path('<name>/<int:age>',views.intro,name='intro')
]
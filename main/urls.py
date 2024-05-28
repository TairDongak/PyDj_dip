from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('content', views.content, name='content'),
    path('about-site', views.about, name='about'),
    path('testing', views.test, name='testing'),

#Глава 1

    path('vvod', views.vvod, name='vvod'),
    path('install', views.install, name='install'),
    path('projects', views.projects, name='projects'),
    path('prilozh', views.prilo, name='prilozh'),
    path('first', views.first, name='first'),

#Глава 2    

    path('2.1', views.zapros, name='zapros'),
    path('2.2', views.path, name='path'),
    path('2.3', views.imagine, name='imagine'),
    path('2.4', views.parametrs, name='parametrs'),
    path('2.5', views.talker, name='talker'),

#Глава 3

    path('3.1', views.template, name='template'),
    path('3.2', views.data_template, name='data_template'),
    path('3.3', views.static_files, name='static_files'),
    path('3.4', views.template_view, name='template_view'),
    path('3.5', views.config, name='config'),
    path('3.6', views.rasshir, name='rasshir'),

#Глава 4

    path('4.1', views.forms, name='forms'),
    path('4.2', views.types, name='types'),
    path('4.3', views.poles, name='poles'),
    path('4.4', views.valid, name='valid'),
    path('4.5', views.dsettings, name='dsettings'),
    path('4.6', views.stylepole, name='stylepole'),

#Глава 5

    path('5.1', views.modmigr, name='modmigr'),
    path('5.2', views.typepole, name='typepole'),
    path('5.3', views.crud, name='crud'),
    path('5.4', views.objmodel, name='objmodel'),
    path('5.5', views.reddel, name='reddel'),
    path('5.6', views.onetomany, name='onetomany'),
    path('5.7', views.manytomany, name='manytomany'),
    path('5.8', views.onetoone, name='onetoone'),
    
    
]

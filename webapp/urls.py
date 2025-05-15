"""URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [


    path('', views.home, name="home"),
    path('adminlogin/', views.adminlogin, name="adminlogin"), 
    path('adminhome/', views.adminhomedef, name="adminhome"),
    path('adminlogout/', views.adminlogoutdef, name="adminlogout"),
    path('signup/', views.signup, name="signup"),
    path('loginaction/', views.loginaction, name="loginaction"),
    path('userlogout/', views.userlogout, name="slogout"),
    path('userhome/', views.userhome, name="shome"),
    path('viewcomments/', views.viewcomments, name="viewcomments"),
    path('postcomments/', views.postcomments, name="postcomments"),
    path('search/', views.search, name="search"),
    path('viewpprofile/', views.viewpprofile, name="viewpprofile"),
    path('trainingpage/', views.trainingpage, name="trainingpage"),
    path('testing/', views.testing, name="testing"),
    

    path('nbtrain/', views.nbtrain, name="nbtrain"),
    path('svmtrain/', views.svmtrain, name="svmtrain"),
    path('rftrain/', views.rftrain, name="rftrain"),
    path('nntrain/', views.nntrain, name="nntrain"),
    
    path('accuracyview/', views.accuracyview, name="accuracyview"),
    path('viewgraph/', views.viewgraph, name="viewgraph"),
    
    
    


    
]

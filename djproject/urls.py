"""djproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.db import router
from django.urls import path,include
from testapp import views
# from django.conf.urls import url,include
from rest_framework import routers
router=routers.DefaultRouter()
router.register('mdlviewset',views.Mdlviewset)
# from rest_framework.authtoken import views as VIEWS
# from rest_framework_jwt.views import obtain_jwt_token,refresh_jwt_token,verif
# y_jwt_token 
# from rest_framework_jwt import views as Jviews
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/<id>', views.f1),
    path('hello/', views.f1),
    path('udt/<id>', views.updt),
    path('frm/', views.f2),
    path('deletee/<id>', views.dlt),
    path('base/', views.mybase),
    path('accounts/', include('django.contrib.auth.urls')),
    # path('cbv/', views.CBV_View.as_view()),
    path('cbv3/<id>', views.CBV3_View.as_view()),
    path('cbv3/', views.CBV3_View.as_view()),
    path('cbv4/', views.CBV4.as_view()),
    path('api-auth/', include('rest_framework.urls')),
    # path('rest/<id>', views.Rest.as_view()),
    path('rest/', views.Rest.as_view()),
    path('apiview/', views.TestApi.as_view()),
    path('mdl/', include(router.urls)),
    path('Myapi/', views.Myapi.as_view()),
    path('listapi/', views.listapi.as_view()),
    path('createapi/', views.createapi.as_view()),
    path('retrieve/<id>', views.retrieve.as_view()),
    path('update/<id>', views.updateapi.as_view()),
    path('destroy/<id>', views.destroy.as_view()),
    path('allcls/', views.Allcls.as_view()),
    path('allcls2/<id>', views.Allcls2.as_view()),
    # path('getapitoken/', VIEWS.obtain_auth_token),
    # path('getjwttoken/', obtain_jwt_token),
    # path('refreshjwt/', refresh_jwt_token),
    # path('verifyjwt/', verify_jwt_token),
    

]

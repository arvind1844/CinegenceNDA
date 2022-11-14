"""CinegenceDoc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django import views
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from CinegenceDoc import settings
from doc import views

urlpatterns = [
   
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('staff/',views.staff,name='staff'),
    path('visitor/',views.visitor,name='visitor'),
    path('client/',views.client,name='client'),
    path('image_upload_staff/<int:id>', views.image_upload_staff, name='image_upload_staff'),
    path('image_upload_client/<int:id>', views.image_upload_client, name='image_upload_client'),
    path('image_upload_visitor/<int:id>', views.image_upload_visitor, name='image_upload_visitor'),
    path('pdf_staff/<int:id>',views.pdf_staff,name='pdf_staff'),
    path('pdf_client/<int:id>',views.pdf_client,name='pdf_client'),
    path('pdf_visitor/<int:id>',views.pdf_visitor,name='pdf_visitor'),
    path('pdf_upload_staff/',views.pdf_upload_staff,name='pdf_upload_staff'),
    path('pdf_upload_client/',views.pdf_upload_client,name='pdf_upload_client'),
    path('pdf_upload_visitor/',views.pdf_upload_visitor,name='pdf_upload_visitor'),
    

]+ static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
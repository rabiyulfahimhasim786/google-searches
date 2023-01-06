from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('uploads/', views.simple_upload, name='simple_upload'),
    path('formupload/', views.model_form_upload, name='model_form_upload'),
    path('fileuploading/', views.uploadings, name='uploadings'),
    path('form/', views.form_upload, name='form_upload'),
    path('csv/', views.csvs, name='csvs'),
    path('csv/<int:id>/',views.delete_document,name='delete_document'),
    #path('new/', views.newest, name='newest'),
]

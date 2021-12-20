from django.urls import path
from . import views

app_name = 'firstapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('post_list', views.post_list, name='post_list'),
    path('post/<int:pk>', views.post_detail, name='post_detail'),
    path('post/new', views.post_new, name='post_new'),
    path('post/modify/<int:pk>', views.post_modify, name='post_modify'),
    path('post/delete/<int:pk>', views.post_delete, name='post_delete'),
    path('view_stock', views.view_stock, name='view_stock'),
    path('lh_notice', views.lh_notice, name='lh_notice'),
    path('fileupload/', views.fileupload, name="fileupload"),
]
from django.urls import path
from . import views


urlpatterns = [
    path
    ('<int:category_id>/', views.posts_by_category, name='posts_by_category'),
    path('comment/<int:pk>/edit/', views.comment_edit, name='comment-edit'),
     path('comment/<int:pk>/delete/', views.comment_delete, name='comment-delete')
    
]

from django.urls import path
from forum import views

app_name = 'forum'

urlpatterns = [
    # ... your URL patterns ...
    path('', views.all_threads, name='all_threads'),
    path('new_thread/', views.new_thread, name='new_thread'),
    path('thread/<int:thread_id>/', views.thread_detail, name='thread_detail'),
    path('thread/<int:thread_id>/new_post/', views.new_post, name='new_post'),
]

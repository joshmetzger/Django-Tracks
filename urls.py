from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='music_home'),
    path('create/', views.create_track, name='create_track'),
    path('view_tracks/', views.view_tracks, name='view_tracks'),
    path('track_details/<int:pk>', views.track_details, name='track_details'),

    path('delete/<int:pk>', views.delete_track, name='delete_track'),

    path('confirmDelete/<int:pk>', views.confirm_delete, name='confirm_delete'),
    path('test_API/', views.test_API, name='test_API'),
    path('beautiful_soup/', views.beautiful_soup, name='beautiful_soup'),
    path('add_favorite/', views.add_fav_track, name='add_fav_track'),
    path('favorites/', views.favorites, name='favorites'),

]
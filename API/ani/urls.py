from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from .views import PhotoView, SongView, UserView

router = DefaultRouter()
router.register(r'photos', PhotoView, basename='photo')
router.register(r'songs', SongView, basename='song')
router.register(r'user', UserView, basename='user_api')

urlpatterns = [
    path('', include(router.urls)),
    path('api-token-auth/', views.obtain_auth_token, name='api-token-auth')
]

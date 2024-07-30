from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SongViewSet, UserRegistrationView, CustomTokenObtainPairView, index, manifest
from django.conf import settings
from django.conf.urls.static import static


router = DefaultRouter()
router.register(r'songs', SongViewSet, basename='song')
from django.conf.urls.static import static

urlpatterns = [
    path('',index, ),
    path('api/', include(router.urls)),
    path('api/auth/register/', UserRegistrationView.as_view(), name='user-register'),
    path('api/auth/login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('manifest.json', manifest,name='manifest'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

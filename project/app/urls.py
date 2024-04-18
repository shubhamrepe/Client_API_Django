from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClientViewSet, ProjectViewSet, UserViewSet


router = DefaultRouter()


router.register(r'clients', ClientViewSet, basename='clients')


router.register(r'projects', ProjectViewSet, basename='projects')


router.register(r'users', UserViewSet, basename='users')


urlpatterns = [
    path('', include(router.urls)), 
]

urlpatterns.append(
    path('clients/<int:client_id>/projects/', ProjectViewSet.as_view({'post': 'create'}), name='project-create'),
)

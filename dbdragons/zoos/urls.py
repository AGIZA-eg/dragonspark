from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'add-dragon', DragonAddedViewSet)
router.register(r'rmv-dragon', DragonRemovedViewSet)
router.register(r'dragon-location-updated', DragonLocationUpdatedViewSet)
router.register(r'dragon-fed', DragonFedViewSet)
router.register(r'maintenance', MaintenancePerformedViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', StaffLoginView.as_view(), name='staff-login'),
    path('logout/', StaffLogoutView.as_view(), name='staff-logout'),
    path('dragon-schedule/', DragonScheduleView.as_view(), name='dragon-schedule'),
]
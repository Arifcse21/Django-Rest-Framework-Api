from rest_framework import routers
from .api import InfoViewSet

router = routers.DefaultRouter()
router.register('api/totka', InfoViewSet, 'totka')

urlpatterns = router.urls
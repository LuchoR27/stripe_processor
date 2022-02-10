from rest_framework.routers import DefaultRouter
from middleware_api.views import ChargeViewSet

router = DefaultRouter()
router.register(r'charge', ChargeViewSet, basename='charge')

urlpatterns = router.urls

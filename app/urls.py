from rest_framework.routers import DefaultRouter

from app.views import MouseViewSet

router = DefaultRouter()

router.register('mouse', MouseViewSet, 'mouse')

urlpatterns = router.urls

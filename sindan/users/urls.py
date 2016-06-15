from django.conf.urls import url
from django.conf.urls import include
from rest_framework import routers

from .api import UserViewSet

router = routers.SimpleRouter()
router.register(r'users', UserViewSet)

urlpatterns = router.urls

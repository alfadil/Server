from rest_framework import routers

from sindan.users.api import UserViewSet

router = routers.SimpleRouter()
router.register(r'users', UserViewSet)

from rest_framework.routers import DefaultRouter

from blog.views import *

router = DefaultRouter()
router.register('', PostView, basename='staff')

urlpatterns = [
]

urlpatterns += router.urls

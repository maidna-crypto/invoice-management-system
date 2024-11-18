from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import InvoiceViewSet

router = DefaultRouter()
router.register(r'invoices', InvoiceViewSet)

# urlpatterns = [
#     path('',include(router.urls)) ]
urlpatterns = router.urls
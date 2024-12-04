from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from app1.views import UserViewSet, BookViewSet, BorrowRequestViewSet, BorrowHistoryViewSet
from drf_yasg import openapi
from rest_framework import permissions
from drf_yasg.views import get_schema_view

# Define Swagger schema view
schema_view = get_schema_view(
   openapi.Info(
      title="Library Management System",
      default_version='v1',
      description="This is the API documentation for the Library Management System.",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="bijwerohit9@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

# Set up the router for API views
router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'books', BookViewSet)
router.register(r'borrow-requests', BorrowRequestViewSet)
router.register(r'history', BorrowHistoryViewSet)

# Define the URL patterns
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger-ui'),  # Add Swagger UI URL
]

from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from app1.views import UserViewSet, BookViewSet, BorrowRequestViewSet, BorrowHistoryViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'books', BookViewSet)
router.register(r'borrow-requests', BorrowRequestViewSet)
router.register(r'history', BorrowHistoryViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]

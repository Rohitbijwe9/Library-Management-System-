from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from django.db.models import Q
from .models import User, Book, BorrowRequest, BorrowHistory
from .serializer import UserSerializer, BookSerializer, BorrowRequestSerializer, BorrowHistorySerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

class BorrowRequestViewSet(viewsets.ModelViewSet):
    queryset = BorrowRequest.objects.all()
    serializer_class = BorrowRequestSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        data = request.data
        book = Book.objects.get(id=data['book'])

        # Check overlapping dates
        overlapping_request = BorrowRequest.objects.filter(
            Q(book=book),
            Q(status='approved'),
            Q(borrow_date__lte=data['return_date']),
            Q(return_date__gte=data['borrow_date']),
        ).exists()

        if overlapping_request:
            return Response({'error': 'Book already borrowed during this period'}, status=status.HTTP_400_BAD_REQUEST)

        # Create BorrowRequest
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

class BorrowHistoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = BorrowHistory.objects.all()
    serializer_class = BorrowHistorySerializer
    permission_classes = [permissions.IsAuthenticated]

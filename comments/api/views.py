from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework import status

from ..models import Comments
from ..serializers import CommentsSerializer

class CommentsViewSet(viewsets.ModelViewSet):

	queryset = Comments.objects.all()
	serializer_class = CommentsSerializer
	filter_backends = (
		DjangoFilterBackend,
		SearchFilter,
	)
	filter_fields = ('comment',)
	search_fields = ('comment',)

	def create(self, request, *args, **kwargs):
	    serializer = self.get_serializer(data=request.data)
	    serializer.is_valid(raise_exception=True)
	    serializer.save(created_by=request.user)
	    return Response(serializer.data, status=status.HTTP_201_CREATED,)
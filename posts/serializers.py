from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Posts
from user.serializers import UserSerializer
from comments.serializers import CommentsSerializer
from comments.serializers import CommentsSerializerSimple

class PostsSerializer(serializers.ModelSerializer):
	comments = CommentsSerializerSimple(many=True, read_only=True)

	class Meta:
		model = Posts
		fields = (
			'id',
			'title',
			'description',
			'content',

			'comments',
			'created_at',
			'updated_at',
			'created_by',
			'updated_by',
		)

class PostsSerializerSimple(serializers.ModelSerializer):
	class Meta:
		model = Posts
		fields = (
			'id',
			'title',
			'description',
			'content',

			'created_by',
		)
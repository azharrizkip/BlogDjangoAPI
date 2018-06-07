from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Comments
from posts.models import Posts
from user.serializers import UserSerializer
from rest_framework_recursive.fields import RecursiveField

class CommentsSerializer(serializers.ModelSerializer):
	post = RecursiveField('posts.serializers.PostsSerializerSimple', read_only=True)
	post_id = serializers.IntegerField(write_only=True, required=False, allow_null=True)

	class Meta:
		model = Comments
		fields = (
			'id',
			'comment',

			'post_id',
			'post',
			'created_at',
			'updated_at',
			'created_by',
			'updated_by',
		)

class CommentsSerializerSimple(serializers.ModelSerializer):
	class Meta:
		model = Comments
		fields = (
			'id',
			'comment',

			'created_by',
		)
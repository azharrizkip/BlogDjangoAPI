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
			'created_by',
		)

	def create(self, validated_data):
	    created_by_id = validated_data.get("created_by_id")
	    validated_data.pop("created_by_id", None)

	    post = Posts(**validated_data)

	    user = User.objects.filter(id=created_by_id).first()
	    post.created_by = user
	    post.save()

	    return post

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
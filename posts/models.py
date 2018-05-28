from django.db import models
from django.contrib.auth.models import User

class Posts(models.Model):

	class Meta:
		db_table = "posts"

	# main fields
	title = models.CharField(max_length=128)
	description = models.CharField(max_length=128)
	content = models.TextField(blank=True, default="")

	#relation fields
	created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

	def __str__(self):
		return self.title
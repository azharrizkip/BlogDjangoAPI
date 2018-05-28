from django.db import models
from django.contrib.auth.models import User

class Comments(models.Model):

	class Meta:
		db_table = "comments"

	# main fields
	comment = models.TextField(blank=False)

	#relation fields
	post = models.ForeignKey(
		'posts.Posts', 
		on_delete=models.CASCADE, 
		null=True,
		related_name="comments"
	)
	created_by = models.ForeignKey(
		User, 
		on_delete=models.CASCADE, 
		null=True
	)

	def __str__(self):
		return self.comment
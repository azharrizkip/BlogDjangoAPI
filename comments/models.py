from django.db import models
from django.contrib.auth.models import User

class Comments(models.Model):

	class Meta:
		db_table = "comments"

	# main fields
	comment = models.TextField(blank=False)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

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
	updated_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        db_column="updated_by_id",
        null=True,
        blank=True,
        related_name='comments_updated_by'
    )

	def __str__(self):
		return self.comment
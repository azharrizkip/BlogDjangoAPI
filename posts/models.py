from django.db import models
from django.contrib.auth.models import User

class Posts(models.Model):

	class Meta:
		db_table = "posts"

	# main fields
	title = models.CharField(max_length=128)
	description = models.CharField(max_length=128)
	content = models.TextField(blank=True, default="")
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	#relation fields
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
        related_name='posts_updated_by'
    )


	def __str__(self):
		return self.title
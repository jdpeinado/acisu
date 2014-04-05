from django.db import models


class AuditedModel(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	class Meta:
		abstract = True


class Post(AuditedModel):
	title = models.CharField(max_length=70, unique=True)
	content = models.TextField()
	tag = models.CharField(max_length=20)
	slug = models.SlugField(max_length=70, blank=True)

	def save(self, *args, **kwargs):
		self.slug = self.title.lower().replace(' ', '_')
		super(Post, self).save(*args, **kwargs)

	def __unicode__(self):
		return self.title
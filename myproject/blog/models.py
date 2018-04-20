from django.db import models
from django.conf import settings
from django.urls import reverse

# Create your models here.
class Post(models.Model):

	user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
	title = models.CharField(max_length=120)
	image = models.ImageField(blank=True, upload_to='records') #records is folder name
	content = models.TextField()
	draft = models.BooleanField(default=False)
	updated = models.DateField(auto_now=True, auto_now_add=False)
	slug = models.SlugField(max_length=120, unique=True)
	published = models.DateField(auto_now=False, auto_now_add=True)

	def __str__(self):
		return "{}, time {}".format(self.title, self.published)

	def get_absolute_url(self):
		return reverse('post-detail',kwargs={'pk':self.pk})




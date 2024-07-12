from django.db import models
from django.utils.text import slugify


#Category
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image_url = models.URLField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, blank=True)  # Allow blank slugs(this make it more efficient)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if not self.slug:  # Only generate slug if it's not already set da
            self.slug = slugify(self.title)  # Use slugify to create a slug from title
            original_slug = self.slug
            counter = 1
            while Post.objects.filter(slug=self.slug).exists(): #this is the one said to you
                self.slug = f"{original_slug}-{counter}"
                counter += 1
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


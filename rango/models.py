from django.db import models
from django.template.defaultfilters import slugify


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=128, unique=True, null=False)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)

    # The `slug` is the human-readable end of the URL for the Category.
    # Like in `google.com/docs/use-of-urls``, "use-of-urls" is the slug.
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name_plural = "categories"

    # Overriding the save function to update the slug whenever the name
    # of the category is updated.
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Page(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title

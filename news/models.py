from django.db import models
from cms.models import CMSPlugin

class NewsCategory(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'News categories'

class News(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    teaser = models.CharField(max_length=200)
    body = models.TextField()
    category = models.ForeignKey(NewsCategory, on_delete=models.CASCADE)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = self.slug or slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'News'

class NewsPluginModel(CMSPlugin):

    ROW_OPTIONS = (
            (12, '1 item'),
            (6,  '2 items'),
            (4,  '3 items'),
            (3,  '4 items'),
        )

    title = models.CharField(max_length=200)

    category = models.ForeignKey(
        NewsCategory, blank=True, on_delete=models.CASCADE
    )

    items_to_show = models.IntegerField(default=3)

    items_per_row = models.IntegerField(default=3, choices=ROW_OPTIONS)

    def __str__(self):
        return self.category.name

    def __unicode__(self):
        return self.category.name

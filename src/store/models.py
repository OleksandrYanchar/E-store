from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=250, db_index=True)
    slug = models.SlugField(max_length=250, unique=True)

    class Meta:
        verbose_name_plural = "categiries"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("list-category", args=[self.slug])


class Product(models.Model):
    category = models.ForeignKey(
        Category, related_name="category", on_delete=models.CASCADE, null=True
    )
    title = models.CharField(max_length=250)
    brand = models.CharField(max_length=250, default="un-branded")
    description = models.TextField(blank=True)
    slug = models.SlugField(max_length=250)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    image = models.ImageField(upload_to="images/")

    class Meta:
        verbose_name_plural = "products"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("poduct-info", args=[self.slug])

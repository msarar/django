from django.db import models
from django.urls import reverse

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length = 120)
    description = models.TextField(blank = True, null = True)
    price = models.DecimalField(decimal_places = 2, max_digits = 10000)
    summary = models.TextField(default = "this cool", blank = False, null = False)
    featured = models.BooleanField(default = False)

    def get_absolute_url (self):
        return f"/products/{self.id}/"
        # return reverse('products:product-detail', kwargs = {"id":self.id})

    def get_absolute_update_url (self):
        return f"/products/{self.id}/update"
        # return reverse('products:product-delete', kwargs = {"id":self.id})

    def get_absolute_delete_url (self):
        return f"/products/{self.id}/delete"
        # return reverse('products:product-update', kwargs = {"id":self.id})

from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.

class List(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    name_list = models.CharField(max_length=120, null=False, blank=False, unique=True)
    created_at = models.DateTimeField(auto_created=datetime.now())
    updated_at = models.DateTimeField(auto_now=True)
    note = models.TextField()
    
    class Meta:
        verbose_name_plural = "لیست های خرید"
    
    @property
    def get_items(self):
        items = self.item_set.all()
        return items
    
    def __str__(self) -> str:
        return self.name_list

    
class Item(models.Model):
    list = models.ForeignKey(List, on_delete=models.CASCADE, null=False, blank=False)
    item_name = models.CharField(max_length=120, blank=False, null=False)
    item_price = models.IntegerField()
    item_quantity = models.IntegerField()
    
    def __str__(self) -> str:
        return self.item_name
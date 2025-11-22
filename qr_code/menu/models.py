from django.db import models

class FoodItems(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='food_images/', blank=True)
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    

class Order(models.Model):
    table_no = models.IntegerField()
    food_list = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return f"Table {self.table_no} - {self.created_at.strftime('%H:%M:%S')}"
    
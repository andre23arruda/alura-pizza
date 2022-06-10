from django.db import models


class Dish(models.Model):
    created_at = models.DateField(auto_now_add=True)
    name = models.CharField(max_length=150)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=8)
    image = models.ImageField(upload_to='uploads/restaurant/dishes/%Y/%m/%d/', null=True)

    class Meta:
        verbose_name = 'Dish'
        verbose_name_plural = 'Dishes'

    def __str__(self):
        return f'{ self.description[:20] }...'
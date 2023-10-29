from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=254)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=254)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(null=True, blank=True)
    brand = models.CharField(max_length=254)
    sku = models.CharField(max_length=50)
    description = models.TextField(max_length=400)
    colour = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    type = models.CharField(max_length=50, choices=[('Glasses', 'Glasses'),
                                                    ('Sunglasses',
                                                    'Sunglasses')])
    material = models.CharField(max_length=50, choices=[('Acetate', 'Acetate'),
                                                        ('Metal', 'Metal'),
                                                        ('Titanium',
                                                         'Titanium')])
    shape = models.CharField(max_length=50)
    size = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True,
                                 blank=True)

    def __str__(self):
        return self.name


from django.db import models
from users.models import CustomUser

# Model for property posts
class PropertyPost(models.Model):
    PROPERTY_CHOICES = [
        ('House', 'HOUSE'),
        ('Guest Wing', 'GUEST WING'),
        ('Quarters', 'QUARTERS'),
        ('Hostel', 'HOSTEL'),
        ('Flat', 'FLAT'),
    ]

    property_type = models.CharField(max_length=20, choices=PROPERTY_CHOICES, default='House')
    city = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    bedrooms = models.PositiveIntegerField()
    bathrooms = models.PositiveIntegerField()
    toilets = models.PositiveIntegerField()
    electricity = models.BooleanField(default=True)
    water = models.BooleanField(default=True)
    description = models.TextField()
    verified = models.BooleanField(default=False)
    date_posted = models.DateTimeField(auto_now_add=True)
    posted_by = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE)
    available = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.property_type} in {self.location}'


# Model for property images
class PropertyImages(models.Model):
    property = models.ForeignKey(PropertyPost, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='property_images/')

    def __str__(self):
        return f'Image for {self.property}'
from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.name

class Order(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    design = models.CharField(max_length=100)
    amount = models.IntegerField(default=500)
    paid = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    message = models.TextField()
    
    def __str__(self):
        return self.name

class Gallery(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='gallery/')
    
    def __str__(self):
        return self.title

class Service(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='service_images/', null=True, blank=True)

    def __str__(self):
        return self.title


class Order(models.Model):
 name = models.CharField(max_length=100)
phone = models.CharField(max_length=15)
design = models.CharField(max_length=100)
amount = models.IntegerField(default=500)
status = models.CharField(
        max_length=20,
        choices=[
            ('pending', 'Pending'),
            ('paid', 'Paid'),
            ('completed', 'Completed'),
        ],
        default='pending'
    )
created_at = models.DateTimeField(auto_now_add=True)

def __str__(self):
        return f"{self.name} - {self.design}"
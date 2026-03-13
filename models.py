from django.db import models

class Lead(models.Model):

    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    source = models.CharField(max_length=100)

    STATUS_CHOICES = [
        ('New', 'New'),
        ('Contacted', 'Contacted'),
        ('Interested', 'Interested'),
        ('Not Interested', 'Not Interested')
    ]

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='New')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Issue(models.Model):
    CATEGORY_CHOICES = [
        ('water_leak',   'Water Leak'),
        ('electricity',  'Electricity Fault'),
        ('pothole',      'Pothole'),
        ('waste',        'Waste Collection'),
        ('water_outage', 'Water Outage'),
        ('other',        'Other'),
    ]
    STATUS_CHOICES = [
        ('pending',     'Pending'),
        ('in_progress', 'In Progress'),
        ('resolved',    'Resolved'),
    ]

    user        = models.ForeignKey(User, on_delete=models.CASCADE)
    title       = models.CharField(max_length=200)
    category    = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    description = models.TextField()
    location    = models.CharField(max_length=255)
    image       = models.ImageField(upload_to='issues/', blank=True, null=True)
    status      = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"#{self.pk} - {self.get_category_display()} - {self.user.username}"

    class Meta:
        ordering = ['-created_at']


class Profile(models.Model):
    user         = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20, blank=True)
    suburb       = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.user.username}'s profile"

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
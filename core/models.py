from django.db import models
from django.contrib.auth.models import User


class BetaSignup(models.Model):
    name = models.CharField(max_length=200, verbose_name='სახელი')
    business_name = models.CharField(max_length=200, verbose_name='ბიზნესის სახელი')
    contact = models.CharField(max_length=200, verbose_name='ტელეფონი ან Email')
    business_type = models.CharField(max_length=200, verbose_name='ბიზნესის ტიპი')
    message = models.TextField(blank=True, verbose_name='შეტყობინება')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.business_name} — {self.name}"

    class Meta:
        verbose_name = 'Beta რეგისტრაცია'
        verbose_name_plural = 'Beta რეგისტრაციები'
        ordering = ['-created_at']


class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name='სათაური')
    content = models.TextField(verbose_name='კონტენტი')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='ავტორი')
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='posts/', blank=True, null=True, verbose_name='სურათი')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'პოსტი'
        verbose_name_plural = 'პოსტები'
        ordering = ['-created_at']
from django.db import models


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

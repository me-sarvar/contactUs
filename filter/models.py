from django.db import models


# Create your models here.
class BlockedEmails(models.Model):
    email = models.EmailField(unique=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name_plural = 'Blocked Emails'


class BlockedIPs(models.Model):
    ip_address = models.GenericIPAddressField(unique=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.ip_address

    class Meta:
        verbose_name_plural = 'Blocked IPs'


class BlockedWords(models.Model):
    word = models.CharField(max_length=50, unique=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.word

    class Meta:
        verbose_name_plural = 'Blocked Words'
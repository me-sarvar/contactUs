from django.contrib import admin
from .models import BlockedEmails, BlockedIPs, BlockedWords

# Register your models here.
admin.site.register(BlockedEmails)
admin.site.register(BlockedIPs)
admin.site.register(BlockedWords)
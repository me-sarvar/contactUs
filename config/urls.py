from django.contrib import admin
from django.urls import path, include
from inbox.views import contact, message_list, message_detail, add_spam_word, homePage, guestPage, adminPage
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView
from django.conf import settings

admin.site.site_header = "Test Header"
urlpatterns = [
    # path('', homePage, name="index"),
    path('', RedirectView.as_view(url='/admin')),
    path('admin', admin.site.urls),
    path('contact/', contact, name='contact'),
    path('messages/', message_list, name="message_list"),
    path('message_detail/<pk>/', message_detail, name="message_detail"),
    path('add-spam-word/<pk>/', add_spam_word, name="add_spam_word"),
    # path('guest_page', guestPage, name='guestPage'),
    # path('adminPage', adminPage, name='adminPage'),
]

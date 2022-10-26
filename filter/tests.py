from django.test import TestCase
from .models import BlockedEmails
from .utils import email_check


# Create your tests here.
class BlockedEmailsTestCase(TestCase):
    def setUp(self):
        BlockedEmails.objects.create(email='test@mail.ru')
        BlockedEmails.objects.create(email='test@mail.com')

    def test_blocked_emails(self):
        """ Email block test """
        email_1 = BlockedEmails.objects.get(email='test@mail.ru')
        email_2 = BlockedEmails.objects.get(email='test@mail.com')

        self.assertTrue(email_check(email_1))
        self.assertTrue(email_check(email_2))
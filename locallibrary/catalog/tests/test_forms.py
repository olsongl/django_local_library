import datetime
from django.test import TestCase
from catalog.forms import RenewBookForm

class RenewBookFormTest(TestCase):
    def test_label_and_help_text(self):
        form = RenewBookForm()
        self.assertTrue(form.fields['renewal_date'].label in [None, 'renewal date'])
        self.assertEqual(form.fields['renewal_date'].help_text, 'Enter a date between now and 4 weeks (default 3).')

    def test_past_date_invalid(self):
        date = datetime.date.today() - datetime.timedelta(days=1)
        form = RenewBookForm(data={'renewal_date': date})
        self.assertFalse(form.is_valid())

    def test_too_far_future_invalid(self):
        date = datetime.date.today() + datetime.timedelta(weeks=5)
        form = RenewBookForm(data={'renewal_date': date})
        self.assertFalse(form.is_valid())

    def test_today_valid(self):
        date = datetime.date.today()
        form = RenewBookForm(data={'renewal_date': date})
        self.assertTrue(form.is_valid())

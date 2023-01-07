from django.test import TestCase
from .forms import ItemsForm
# Create your tests here.


class TestItemsForm(TestCase):

    def test_item_name_is_requered(self):
        form = ItemsForm({'name': ""})
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())
        self.assertEqual(form.errors['name'][0], "This field is required.")

    def test_done_field_is_not_requered(self):
        form = ItemsForm({'name': "test items form"})
        self.assertTrue(form.is_valid())

    def test_fields_are_explicit_in_form_metaclass(self):
        form = ItemsForm()
        self.assertEqual(form.Meta.fields, ['name', 'done'])

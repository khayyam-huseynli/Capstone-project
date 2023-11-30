from django.test import TestCase
from restaurant.models import Menu

class MenuViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(title="doner", price=20, inventory=10)
        Menu.objects.create(title="shawrma", price=20, inventory=10)
            
    def test_getall(self):
        items = Menu.objects.all()
        self.assertEqual(items.count(), 2)
from django.test import TestCase
from restaurant.models import Menu

class MenuTest(TestCase):
    def instance(self):
        item = Menu.objects.create(title="IceCream", price=80, inventory=100)
        self.assertEqual(str(item), "IceCream : 80")

class MenuViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(title="doner", price=20, inventory=10)
        Menu.objects.create(title="shawrma", price=20, inventory=10)
        
    
    def test_getall(self):
        items = Menu.objects.all()
        self.assertEqual(items.count(), 2)
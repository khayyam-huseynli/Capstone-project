from django.test import TestCase
from restaurant.models import Menu

class MenuTest(TestCase):
    def instance(self):
        item = Menu.objects.create(title="IceCream", price=80, inventory=100)
        self.assertEqual(str(item), "IceCream : 80")

from django.test import TestCase
from .models import Menu
from .serializers import MenuSerializer


class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="IceCream",price=80,inventory=10)
        self.assertEqual(str(item),"IceCream : 80")

class MenuViewTest(TestCase):
    def setUp(self):
        self.item = Menu.objects.create(id=1,title="IceCream",price=80.00,inventory=20)
        self.test_data = [
            {'id': 1,'title':"IceCream",'price':'80.00','inventory':20}
        ]
    
    def test_getall(self):
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus,many=True)
        serialized_data = serializer.data
        self.assertEqual(serialized_data,self.test_data)
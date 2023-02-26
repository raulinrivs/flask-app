import unittest
from car_registration.models import Car, Owner


class TestModels(unittest.TestCase):
    
    def setUp(self):
        person_1 = Owner(id=1, name='Mateus')
        person_2 = Owner(id=2, name='Raulino')
        car_1 = Car(id=1, color='gray', car_type='hatch', owner_id=1)
        car_1 = Car(id=2, color='yellow', car_type='sedan', owner_id=1)
        car_1 = Car(id=3, color='blue', car_type='convertible', owner_id=1)
        return super().setUp()
        
    def test_car(self):
        self.assertEqual(self.person_1.id, self.car_1.owner_id)
        self.assertEqual(self.person_1.id, self.car_2.owner_id)
        self.assertEqual(self.person_1.id, self.car_3.owner_id)

    def test_person(self):
        self.assertEqual(self.person_1.name, 'Mateus')
    
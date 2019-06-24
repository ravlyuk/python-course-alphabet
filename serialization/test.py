from serialization.homework import *
import unittest


class TestCar(unittest.TestCase):

    def setUp(self):
        self.auto1 = Car(price=350000, mileage=50, producer="BENTLEY", type="Sports Car", number=8964604765756)
        self.auto2 = Car(price=550000, mileage=100, producer="Bugatti", type="Sports Car", number=7413216153498)

    def test_auto1_change_number_success(self):
        self.auto1.change_car_number(uuid.uuid4())
        self.assertIsInstance(self.auto1.number, uuid.UUID)

    def test_auto1_change_number_fail(self):
        self.auto1.change_car_number(000000)
        self.assertNotIsInstance(self.auto1.number, uuid.UUID)

    def test_auto_equality_success(self):
        self.assertTrue(self.auto1 < self.auto2)

    def test_auto_equality_fail(self):
        self.assertFalse(self.auto1 > self.auto2)

    def test_auto1_serelisation_to_json(self):
        expected_result = {
            '__class__': 'Car',
            '__module__': 'serialization.homework',
            'price': 350000,
            'mileage': 50,
            'producer': 'BENTLEY',
            'type': 'Sports Car',
            'number': 8964604765756}
        self.assertEqual(object_to_json(self.auto1), expected_result)

    def test_auto1_serelisation_to_file(self):
        file_name_auto1 = 'auto1_serialization.json'
        object_to_file(auto1, file_name_auto1)
        with open(file_name_auto1, 'r') as file:
            data = file.readlines()
            self.assertTrue(data)

    def test_auto1_deserelisation_without_file(self):
        file_name_auto1 = 'auto1_serialization.json'
        with open(file_name_auto1, 'r') as file:
            check_serelisation_file = json.load(file, object_hook=json_hook)
        self.assertIsInstance(check_serelisation_file, object)

    def test_auto2_repr(self):
        expected_result = """{'price': self.auto2.price, 'type': self.auto2.type, 'producer': self.auto2.producer,
                               'number': self.auto2.number, 'mileage': self.auto2.mileage}"""

        self.assertEqual(repr(self.auto2), expected_result)


class TestGarage(unittest.TestCase):

    def setUp(self):
        self.auto1 = Car(price=350000, mileage=50, producer="BENTLEY", type="Sports Car", number=8964604765756)
        self.auto2 = Car(price=550000, mileage=100, producer="Bugatti", type="Sports Car", number=7413216153498)
        self.garage1 = Garage('Kiev', 3, [self.auto1], number=57856780347956)
        self.garage2 = Garage('Uzin', 4, [self.auto1, self.auto2], number=1649817605649)

    def test_add_car_into_garage_success(self):
        expected_result = 2
        self.garage1.add_car_into_garage(auto2)
        self.assertEqual(self.garage1.places, expected_result)
        self.assertIn(self.auto1, self.garage1.cars[0])

    def test_add_car_into_garage_fail(self):
        expected_result = 3
        self.garage2.add_car_into_garage(self.auto1)
        self.assertEqual(self.garage2.places, expected_result)
        self.assertNotIn(self.auto2, self.garage2.cars)

    def test_remove_car_from_garage_success(self):
        expected_result = 3
        self.garage1.remove(self.auto2)
        self.assertEqual(self.garage1.places, expected_result)
        self.assertNotIn(self.auto2, self.garage1.cars)

    def test_free_places_for_garage_success(self):
        expected_result = 4
        self.assertEqual(self.garage2.places, expected_result)

    def test_serilisation_garage2_to_json(self):
        expected_result = """{'__class__': 'Garage', '__module__': 'serialization.homework', 'town': 'Uzin',
       'places': 4, 'owner': None, 'number': 1649817605649,
       'cars': [[{'__class__': 'Car', '__module__':
           'serialization.homework', 'price': 350000, 'mileage': 50, 'producer': 'BENTLEY',
                  'type': 'Sports Car',
                  'number': 8964604765756},
                 {'__class__': 'Car', '__module__': 'serialization.homework', 'price': 550000,
                  'mileage': 100, 'producer': 'Bugatti', 'type': 'Sports Car',
                  'number': 7413216153498}]]}"""

        self.assertEqual(str(object_to_json(self.garage2)), expected_result)

    def test_garage1_serelisation_to_file(self):
        file_name_garage1 = 'garage1_serialization.json'
        object_to_file(garage1, file_name_garage1)
        with open(file_name_garage1, 'r') as file:
            data = file.readlines()
            self.assertTrue(data)

    def test_garage1_deserelisation_without_file(self):
        file_name_garage1 = 'garage1_serialization.json'
        with open(file_name_garage1, 'r') as file:
            check_serelisation_file = json.load(file, object_hook=json_hook)
        self.assertIsInstance(check_serelisation_file, object)

    def test_garage2_repr(self):
        expected_result = """{'town': 'Uzin', 'places': 4, 'owner': None, 'number': 1649817605649, 
        'cars': [[{'price':
           350000,
       'type': 'Sports Car',
       'producer': 'BENTLEY',
       'number': 8964604765756,
       'mileage': 50},
      {
          'price': 550000,
          'type': 'Sports Car',
          'producer': 'Bugatti',
          'number': 7413216153498,
          'mileage': 100}]]}"""
        self.assertEqual(repr(self.garage2), expected_result)


class TestCesar(unittest.TestCase):

    def setUp(self):
        self.auto1 = Car(price=350000, mileage=50, producer="BENTLEY", type="Sports Car", number=8964604765756)
        self.auto2 = Car(price=550000, mileage=100, producer="Bugatti", type="Sports Car", number=7413216153498)
        self.garage1 = Garage('Kiev', 3, [self.auto1], number=57856780347956)
        self.garage2 = Garage('Uzin', 4, [self.auto1, self.auto2], number=1649817605649)
        self.cesar1 = Cesar("Zelelensy", [self.garage1], register_id=6513219811321803)
        self.cesar2 = Cesar("Poroshenko", [self.garage2], register_id=8403201656131135)

    def test__repr__for_cesar1(self):
        expected_result = """{'name': 'Zelelensy', 'garages': [[{'town': 'Kiev', 'places': 3, 'owner': None, 'number': 57856780347956, 'cars': [[{'price': 350000, 'type': 'Sports Car', 'producer': 'BENTLEY', 'number': 8964604765756, 'mileage': 50}]]}]], 'register_id': 6513219811321803}"""
        self.assertEqual(repr(self.cesar1), expected_result)

    def test_garages_count_method_for_cesar_success(self):
        expected_result_1 = 1
        expected_result_2 = 1
        self.assertEqual(self.cesar1.garages_count(), expected_result_1)
        self.assertEqual(self.cesar2.garages_count(), expected_result_2)

    def test_auto1_count_method_for_cesar_success(self):
        expected_result = 1
        self.assertEqual(self.cesar1.cars_count(), expected_result)

    def test_serilisation_cesar1_to_json(self):
        expected_result = str({'__class__': 'Cesar', '__module__': 'serialization.homework', 'name': 'Zelelensy',
                               'register_id': 6513219811321803,
                               'garages': [[{'__class__': 'Garage', '__module__': 'serialization.homework',
                                             'town': 'Kiev', 'places': 3, 'owner': None, 'number': 57856780347956,
                                             'cars': [[{'__class__': 'Car',
                                                        '__module__': 'serialization.homework', 'price': 350000,
                                                        'mileage': 50, 'producer': 'BENTLEY', 'type': 'Sports Car',
                                                        'number': 8964604765756}]]}]]}
                              )

        self.assertEqual(str(object_to_json(self.cesar1)), expected_result)

    def test_cesar2_serelisation_to_file(self):
        file_name_cesar2 = 'cesar2_serialization.json'
        object_to_file(cesar2, file_name_cesar2)
        with open(file_name_cesar2, 'r') as file:
            data = file.readlines()
            self.assertTrue(data)

    def test_cesar2_deserelisation_without_file(self):
        file_name_cesar2 = 'cesar2_serialization.json'
        with open(file_name_cesar2, 'r') as file:
            check_serelisation_file = json.load(file, object_hook=json_hook)
        self.assertIsInstance(check_serelisation_file, object)

    def test_cesar2_repr(self):
        expected_result = str({'name': 'Poroshenko', 'garages': [[{'town': 'Uzin', 'places': 4, 'owner': None,
                                                                   'number': 1649817605649, 'cars': [
                [{'price': 350000, 'type': 'Sports Car', 'producer': 'BENTLEY', 'number': 8964604765756, 'mileage': 50},
                 {'price': 550000, 'type': 'Sports Car', 'producer': 'Bugatti', 'number': 7413216153498,
                  'mileage': 100}]]}]], 'register_id': 8403201656131135})
        self.assertEqual(repr(self.cesar2), expected_result)


if __name__ == "__main__":
    unittest.main()

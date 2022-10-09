'''
class example to create an inventory and keep track of capacity(quantities)
cool usage of dictionary. 
'''

class Inventory:
   
    def __init__(self, max_capacity):
        self.max_capacity = max_capacity
        self.invitems={}
        self.count = 0

    def add_item(self, name, price, quantity):
        if name in self.invitems:
            return False
    
        if self.count + quantity> self.max_capacity:
            return False
        self.count += quantity
        self.invitems[name] = {'name':name, 'price':price, 'quantity':quantity}           
        return True
           

    def delete_item(self, name):
        if name not in self.invitems:
            return False
        else:
            self.count -= self.invitems[name]['quantity']
            del self.invitems[name]
            return True

    def get_items_in_price_range(self, min_price, max_price):
        lst =[]
        for k, v in self.invitems.items():
            if min_price <=v['price'] <=max_price:
                lst.append(k)

        return  lst

    def get_most_stocked_item(self):
        largest_quantity = 0
        iname_for_largets_quantity = None


        for item in self.invitems.values():
            quantity = item['quantity']
            product_name = item['Name']
            
            if quantity > largest_quantity:
                iname_for_largets_quantity = product_name
                largest_quantity = quantity

        return iname_for_largets_quantity

    # cant use the method below because the test designed so that it expects only one items as an output.
    # def get_most_stocked_item(self):
    #     #print(self.invitems)
    #     m = max([v['quantity'] for v in self.invitems.values()],default=0)
    #     r = [k for k,v in self.invitems.items() if v['quantity'] == m]
    #     return r[0] if len(r) > 0 else None

import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        inventory = Inventory(0)
        self.assertFalse(inventory.add_item('Chocolate', 4.99, 1))

    def test_case_2(self):
        inventory = Inventory(3)
        self.assertFalse(inventory.add_item('Chocolate', 4.99, 4))

    def test_case_3(self):
        inventory = Inventory(3)
        self.assertTrue(inventory.add_item('Chocolate', 4.99, 1))
        self.assertTrue(inventory.add_item('Butter', 4.99, 1))
        self.assertFalse(inventory.add_item('Butter', 4.99, 1))
        self.assertFalse(inventory.add_item('Bread', 4.99, 2))

    def test_case_4(self):
        inventory = Inventory(4)
        self.assertTrue(inventory.add_item('Chocolate', 4.99, 1))
        self.assertTrue(inventory.add_item('Butter', 4.99, 1))
        self.assertTrue(inventory.add_item('Bread', 4.99, 2))
        self.assertEqual('Bread', inventory.get_most_stocked_item())

    def test_case_5(self):
        inventory = Inventory(4)
        self.assertTrue(inventory.add_item('Chocolate', 4.99, 4))
        self.assertTrue(inventory.delete_item('Chocolate'))
        self.assertFalse(inventory.delete_item('Chocolate'))
        self.assertFalse(inventory.delete_item('Bread'))
        
        self.assertTrue(inventory.add_item('Chocolate', 4.99, 2))
        self.assertTrue(inventory.add_item('Bread', 4.99, 2))
        self.assertIn(inventory.get_most_stocked_item(), ('Chocolate', 'Bread'))

    def test_case_6(self):
        inventory = Inventory(5)
        self.assertIsNone(inventory.get_most_stocked_item())
        self.assertEqual([], inventory.get_items_in_price_range(1, 10))

    def test_case_7(self):
        inventory = Inventory(5)
        self.assertTrue(inventory.add_item('Chocolate', 4.99, 1))
        self.assertTrue(inventory.add_item('Bread', 3.99, 1))
        self.assertTrue(inventory.add_item('Milk', 5.99, 3))
        self.assertEqual(sorted(['Chocolate', 'Milk', 'Bread']), sorted(inventory.get_items_in_price_range(1, 10)))

    def test_case_8(self):
        max_capacity = 4
        inventory = Inventory(max_capacity)
        self.assertEqual(inventory.add_item('Chocolate', 4.99, 1), True)
        self.assertEqual(inventory.add_item('Cereal', 6.99, 1), True)
        self.assertEqual(inventory.add_item('Milk', 3.99, 2), True)
        self.assertEqual(inventory.add_item('Butter', 2.99, 1), False)
        self.assertEqual(inventory.delete_item('Bread'), False)
        self.assertEqual(inventory.delete_item('Cereal'), True)
        self.assertEqual(inventory.get_items_in_price_range(4.50, 6.50), ['Chocolate'])


if __name__ == '__main__':
    unittest.main()
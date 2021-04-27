import unittest
from src import clicker

def to_start_position():
    clicker.dollar_now = clicker.dollar.curr_price()
    clicker.time_for_req = 0 
    for clicker.improvement in clicker.list_of_improvement:
        clicker.improvement.quantity = 0
    clicker.user.score = 0
    clicker.user.rps = 0

class ClickerTest(unittest.TestCase):
    def auto_clicks(self):
        clicker.user.updateTotalrps(list_of_improvement)
        self.assertEqual(clicker.score, 0)
        for clicker.improvement in clicker.list_of_improvement:
            for i in 100:
                if clicker.improvement != clicker.dvorec:
                    clicker.improvement.quantity = i
                    self.asserEqual(clicker.user.rps, clicker.improvement.base_cost * i)
                    to_start_position()

    def check_cost(self):
        for clicker.improvement in clicker.list_of_improvement:
            for i in 100:
                if clicker.improvement != clicker.dvorec:
                    clicker.improvement.quantity = i
                    self.asserEqual(clicker.improvement.getTotalCost(), int(self.base_cost * self.increase_per_purchase**(i)))
                    to_start_position()

class FastClickerTest(unittest.TestCase):
    clicker.run()

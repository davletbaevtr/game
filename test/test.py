import unittest
from src import clicker

def to_start_position():
    clicker.time_for_req = 0 
    for clicker.improvement in clicker.list_of_improvement:
        clicker.improvement.quantity = 0
    clicker.user.score = 0
    clicker.user.rps = 0

class ClickerTest(unittest.TestCase):
    def test_auto_clicks(self):
        clicker.user.updateTotalrps()
        self.assertEqual(clicker.user.score, 0)
        for clicker.improvement in clicker.list_of_improvement:
            for i in range(100):
                if clicker.improvement != clicker.dvorec:
                    clicker.improvement.quantity = i
                    clicker.user.updateTotalrps()
                    rps_from_improvement = clicker.improvement.base_cost * i
                    self.assertEqual(clicker.user.rps, rps_from_improvement)
                    to_start_position()

    def test_check_cost(self):
        for clicker.improvement in clicker.list_of_improvement:
            for i in range(100):
                if clicker.improvement != clicker.dvorec:
                    clicker.improvement.quantity = i
                    cost_of_improvement = int(clicker.improvement.base_cost * clicker.improvement.increase_per_purchase**(i))
                    self.assertEqual(clicker.improvement.getTotalCost(), cost_of_improvement)
                    to_start_position()

if __name__ == '__main__':
    unittest.main()

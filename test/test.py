import unittest
import clicker

def to_start_position():
    clicker.dollar_now = clicker.dollar.curr_price()
    clicker.time_for_req = 0 
    for clicker.improvement in clicker.list_of_improvement:
        clicker.improvement.quantity = 0
    clicker.user.score = 0
    clicker.user.rps = 0

class ClickerTest(unittest.TestCase):
    def test_auto_clicks(self):
        clicker.user.updateTotalrps(clicker.list_of_improvement)
        self.assertEqual(clicker.user.score, 0)
        for clicker.improvement in clicker.list_of_improvement:
            for i in range(100):
                if clicker.improvement != clicker.dvorec:
                    clicker.improvement.quantity = i
                    clicker.user.updateTotalrps(clicker.list_of_improvement)
                    self.assertEqual(clicker.user.rps, clicker.improvement.base_cost * i)
                    to_start_position()

    def test_check_cost(self):
        for clicker.improvement in clicker.list_of_improvement:
            for i in range(100):
                if clicker.improvement != clicker.dvorec:
                    clicker.improvement.quantity = i
                    self.assertEqual(clicker.improvement.getTotalCost(), int(clicker.improvement.base_cost * clicker.improvement.increase_per_purchase**(i)))
                    to_start_position()

if __name__ == '__main__':
    unittest.main()

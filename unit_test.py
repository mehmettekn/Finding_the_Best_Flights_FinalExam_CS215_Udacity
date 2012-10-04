import unittest
from finding_the_best_flights import*
from all_flights import all_flights

class Testfindingthebestflights(unittest.TestCase):

    def test1(self):
        flights = find_best_flights(all_flights, 'Mt Magnet', 'Fitzroy Crossing')
        assert flights == [314, 803, 348, 530, 112]

    def test2(self):
        flights = find_best_flights(all_flights, 'Leonora', 'Fitzroy Crossing')
        assert flights == None

    def test3(self):
        flights = find_best_flights(all_flights, 'Meekatharra', 'Wiluna')
        assert flights == [391, 459]

if __name__ == '__main__':
    try: unittest.main()
    except SystemExit: pass

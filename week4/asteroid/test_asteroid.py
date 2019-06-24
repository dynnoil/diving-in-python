import json
import unittest
from unittest.mock import patch

from asteroid import Asteroid


class TestAsteroid(unittest.TestCase):

    def setUp(self):
        self.asteriod = Asteroid(2099942)

    def mocked_get_data(self):
        with open('week4/test/2099942.json') as f:
            return json.loads(f.read())

    @patch('asteroid.Asteroid.get_data', mocked_get_data)
    def test_name(self):
        self.assertEqual(
            self.asteriod.name, '99942 Apophis (2004 MN4)'
        )

    @patch('asteroid.Asteroid.get_data', mocked_get_data)
    def test_diameter(self):
        self.assertEqual(self.asteriod.diameter, 682)

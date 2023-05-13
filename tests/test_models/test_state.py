#!/usr/bin/python3
""" Testing State Module """
import os
from models.state import State
from tests.test_models.test_base_model import test_basemodel


class test_state(test_basemodel):
    """ state test class"""

    def __init__(self, *args, **kwargs):
        """ state test class init"""
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """ test state name attr"""
        new = self.value()
        self.assertEqual(type(new.name), str if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                         type(None))

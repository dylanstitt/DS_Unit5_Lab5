# Dylan Stitt
# Unit 5 Lab 5
# Positional List

# Implementation & testing of the PositionalList class

from PositionalList import PositionalList
from TEST_CODE import *
import os

'''
Testing details can be found in TEST_CODE.py

ENSURE ALL TESTS PASS BEFORE SUBMITTING

IF COLORAMA NOT FOUND - ENTER INTO TERMINAL:
pip install colorama
'''

def main():

    PL = PositionalList()

    # TEST 1 - Test PDB Creation
    # BEFORE TESTING: implement PL definition and inherit PDB
    TEST_new_PL(PL, PositionalList)

    # TEST 2 - Test DoublyNode
    # BEFORE TESTING: implement nested Position class init & get_value
    TEST_position(PositionalList)

    # TEST 3 - Test make_position & validate
    # BEFORE TESTING: implement PL __make_position, __validate
    TEST_make_position_validate(PL, PositionalList)

    # TEST 4 - Inherited insert_between
    # BEFORE TESTING: implement PL __insert_between
    TEST_insert_between(PL, PositionalList)

    PL = PositionalList()

    # TEST 5 - Test adding nodes
    # BEFORE TESTING: implement PL add(first, last, before, after), __str__, __len__
    TEST_add_nodes(PL, PositionalList)

    # TEST 6 - Test iterator method
    # BEFORE TESTING: implement PL __iter__
    TEST_iterator(PL)

    # TEST 7 - Test getting positions
    # BEFORE TESTING: implement PL getters(first, last, before, after)
    TEST_get_positions(PL, PositionalList)

    # TEST 8 - Test eq and ne
    # BEFORE TESTING: implement Position __eq__ and __ne__
    TEST_position_equality(PL)

    # TEST 9 - Test replace
    # BEFORE TESTING: implement PL replace
    TEST_replace(PL)

    # TEST 10 - Test delete
    # BEFORE TESTING: implement PL delete
    TEST_delete(PL, PositionalList)


if __name__ == "__main__":
    os.system("cls")
    main()

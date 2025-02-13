##### Global color variables #####
from colorama import Fore

R = Fore.RED
G = Fore.GREEN
B = Fore.BLUE
W = Fore.RESET
P = Fore.CYAN

'''IF COLORAMA NOT FOUND - ENTER INTO TERMINAL:
pip install colorama'''


##################################

def result(flag):
    if flag:
        return f"{G}PASSED{W}"

    return f"{R}FAILED{W}"


def test_sequence(PL, forw_sequ):
    h = PL.header
    t = PL.trailer
    try:
        walk = h
        for el in forw_sequ:
            if el != walk.value:
                return False

            walk = walk.next

        rev_sequ = forw_sequ[::-1]
        walk = t
        for el in rev_sequ:
            if el != walk.value:
                return False

            walk = walk.prev

        return True

    except:
        return False


def TEST_new_PL(PL, class_ref):
    print("~" * 50)
    print(f"{P}TEST CATEGORY: PL initialization{W}\n")

    temp_node = class_ref().DoublyNode("temp")

    test = type(PL.header) == type(temp_node)
    print(f"Header sentinel is type DoublyNode: {result(test)}")

    test = type(PL.trailer) == type(temp_node)
    print(f"Trailer sentinel is type DoublyNode: {result(test)}\n")

    test = PL.header.next == PL.trailer
    print(f"Header next is Trailer: {result(test)}")

    test = PL.trailer.prev == PL.header
    print(f"Trailer prev is Header: {result(test)}\n")

    test = PL._PositionalDoublyBase__size == 0
    print(f"Size attribute initialized to zero: {result(test)}")

    print("~" * 50, "\n\n")


def TEST_position(class_ref):
    print("~" * 50)
    print(f"{P}TEST CATEGORY: Nested Position Class{W}\n")

    temp_PL = class_ref()
    h = temp_PL.header
    temp_pos = temp_PL.Position(temp_PL, h)

    test = temp_pos._Position__member_of == temp_PL
    print(f"member_of attribute stores a PositionalList object: {result(test)}")

    test = temp_pos._Position__node == h
    print(f"node attribute stores a DoublyNode object: {result(test)}")

    test = temp_pos.get_value() == None
    print(f"get_value method returns node contents: {result(test)}")

    print("~" * 50, "\n\n")


def TEST_make_position_validate(PL, class_ref):
    print("~" * 50)
    print(f"{P}TEST CATEGORY: Make Position and Validate Utilities{W}\n")

    temp_PL = class_ref()
    test_node = temp_PL.header

    pos = PL._PositionalList__make_position(test_node)

    test = type(pos) == class_ref.Position
    print(f"make_position method returns Position object: {result(test)}")

    test = pos._Position__node == test_node
    print(f"New position contains a node object: {result(test)}")

    pos1 = PL._PositionalList__make_position(PL.header)
    pos2 = PL._PositionalList__make_position(PL.trailer)
    test = pos1 == pos2 == None
    print(f"make_position returns none when node given is sentinel: {result(test)}\n")

    node = PL._PositionalList__validate(pos)
    test = node is test_node
    print(f"validate returns node object from valid position: {result(test)}")

    temp_pos = temp_PL._PositionalList__make_position(PL.header)
    try:
        node = PL._PositionalList__validate(temp_pos)
        print(f"validate raises exception if position is not in this list: {result(False)}")
    except:
        print(f"validate raises exception if position is not in this list: {result(True)}")

    try:
        node = PL._PositionalList__validate("X")
        print(f"validate raises exception if argument is not type Position: {result(False)}")
    except:
        print(f"validate raises exception if argument is not type Position: {result(True)}")

    print("~" * 50, "\n\n")


def TEST_insert_between(PL, class_ref):
    print("~" * 50)
    print(f"{P}TEST CATEGORY: Inherited insert_between{W}\n")

    pos = PL._PositionalList__insert_between("X", PL.header, PL.trailer)

    test = type(pos) == class_ref.Position
    print(f"insert_between method returns Position object: {result(test)}")

    temp_node = class_ref().DoublyNode("temp")
    test = type(pos._Position__node) == type(temp_node)
    print(f"New position contains a node object: {result(test)}")

    print("~" * 50, "\n\n")


def TEST_add_nodes(PL, class_ref):
    print("~" * 50)
    print(f"{P}TEST CATEGORY: Adding Nodes{W}\n")

    test_PL = class_ref()
    test_pos = test_PL.add_first("X")

    print(f"\n{P} ~~~ add_first() ~~~{W}")
    pos1 = PL.add_first("A")
    print(f"{B}A node was added: {PL}{W}\n")

    test = type(pos1) == class_ref.Position
    print(f"add_first method returns Position object: {result(test)}")

    test = len(PL) == 1
    print(f"add_first increases PL size: {result(test)}")

    pos2 = PL.add_first("B")
    print(f"\n{B}Another node was added: {PL}{W}\n")

    test = test_sequence(PL, [None, "B", "A", None])
    print(f"Node pointers are correct: {result(test)}")

    print(f"\n\n{P} ~~~ add_last() ~~~{W}")
    pos3 = PL.add_last("C")
    print(f"{B}Another node was added: {PL}{W}\n")

    test = type(pos3) == class_ref.Position
    print(f"add_last method returns Position object: {result(test)}")

    test = len(PL) == 3
    print(f"add_last increases PL size: {result(test)}")

    pos4 = PL.add_last("D")
    print(f"\n{B}Another node was added: {PL}{W}\n")

    test = test_sequence(PL, [None, "B", "A", "C", "D", None])
    print(f"Node pointers are correct: {result(test)}")

    print(f"\n\n{P} ~~~ add_before() ~~~{W}")
    pos5 = PL.add_before("E", pos1)
    print(f"{B}Another node was added: {PL}{W}\n")

    test = type(pos5) == class_ref.Position
    print(f"add_before method returns Position object: {result(test)}")

    test = len(PL) == 5
    print(f"add_before increases PL size: {result(test)}")

    pos6 = PL.add_before("F", pos4)
    print(f"\n{B}Another node was added: {PL}{W}\n")

    test = test_sequence(PL, [None, "B", "E", "A", "C", "F", "D", None])
    print(f"Node pointers are correct: {result(test)}")

    try:
        PL.add_before("F", test_pos)
        print(f"add_before validates incoming position: {result(False)}")
    except:
        print(f"add_before validates incoming position: {result(True)}")

    print(f"\n\n{P} ~~~ add_after() ~~~{W}")
    pos7 = PL.add_after("G", pos1)
    print(f"{B}Another node was added: {PL}{W}\n")

    test = type(pos7) == class_ref.Position
    print(f"add_after method returns Position object: {result(test)}")

    test = len(PL) == 7
    print(f"add_after increases PL size: {result(test)}")

    pos8 = PL.add_after("H", pos2)
    print(f"\n{B}Another node was added: {PL}{W}\n")

    test = test_sequence(PL, [None, "B", "H", "E", "A", "G", "C", "F", "D", None])
    print(f"Node pointers are correct: {result(test)}")

    try:
        PL.add_after("F", test_pos)
        print(f"add_after validates incoming position: {result(False)}")
    except:
        print(f"add_after validates incoming position: {result(True)}")

    print("~" * 50, "\n\n")


def TEST_iterator(PL):
    print("~" * 50)
    print(f"{P}TEST CATEGORY: Iterator Method{W}\n")

    sequence = ["B", "H", "E", "A", "G", "C", "F", "D"]
    test_seq = True
    test_type = True
    print(f"{B}Contents of the PL:")
    for i, node in enumerate(PL):
        if type(node) != type(sequence[i]):
            test_type = False
            break
        if node != sequence[i]:
            test = False
            break
        print(" ", node)

    print(f"{W}\nLoop yields correct sequence: {result(test_seq)}")

    print(f"Loop yields node/position value: {result(test_type)}")

    print("~" * 50, "\n\n")


def TEST_get_positions(PL, class_ref):
    print("~" * 50)
    print(f"{P}TEST CATEGORY: Getter Methods{W}\n")

    test_PL = class_ref()
    test_pos = test_PL.add_first("X")

    print(f"\n{B}Current PL: {PL}{W}\n")

    print(f"\n{P} ~~~ first() ~~~{W}")

    pos1 = PL.first()

    test = type(pos1) == class_ref.Position
    print(f"first() returns position object: {result(test)}")

    test = len(PL) == 8
    print(f"first() does not impact size: {result(test)}")

    test = pos1.get_value() == "B"
    print(f"Position contains correct node: {result(test)}")

    print(f"\n{P} ~~~ last() ~~~{W}")

    pos8 = PL.last()

    test = type(pos8) == class_ref.Position
    print(f"last() returns position object: {result(test)}")

    test = len(PL) == 8
    print(f"last() does not impact size: {result(test)}")

    test = pos8.get_value() == "D"
    print(f"Position contains correct node: {result(test)}")

    print(f"\n{P} ~~~ before() ~~~{W}")

    pos7 = PL.before(pos8)

    test = type(pos7) == class_ref.Position
    print(f"before() returns position object: {result(test)}")

    test = len(PL) == 8
    print(f"before() does not impact size: {result(test)}")

    test = pos7.get_value() == "F"
    print(f"Position contains correct node: {result(test)}")

    pos0 = PL.before(pos1)
    test = pos0 == None
    print(f"Returns None if position predecessor is header: {result(test)}")

    try:
        PL.before(test_pos)
        print(f"before validates incoming position: {result(False)}")
    except:
        print(f"before validates incoming position: {result(True)}")

    print(f"\n{P} ~~~ after() ~~~{W}")

    pos2 = PL.after(pos1)

    test = type(pos2) == class_ref.Position
    print(f"after() returns position object: {result(test)}")

    test = len(PL) == 8
    print(f"after() does not impact size: {result(test)}")

    test = pos2.get_value() == "H"
    print(f"Position contains correct node: {result(test)}")

    pos0 = PL.after(pos8)
    test = pos0 == None
    print(f"Returns None if position successor is trailer: {result(test)}")
    try:
        PL.after(test_pos)
        print(f"after validates incoming position: {result(False)}")
    except:
        print(f"after validates incoming position: {result(True)}")

    test = test_sequence(PL, [None, "B", "H", "E", "A", "G", "C", "F", "D", None])
    print(f"\nGetter methods do not change node sequence: {result(test)}")

    print("~" * 50, "\n\n")


def TEST_position_equality(PL):
    print("~" * 50)
    print(f"{P}TEST CATEGORY: Position object equality{W}\n")

    pos1 = PL.first()
    pos2 = PL.first()

    test = pos1 is not pos2 and pos1._Position__node is pos2._Position__node
    print(f"Positon getters return different object containing the same node: {result(test)}")

    test = pos1 == pos2
    print(f"\nTwo different position objects can be equal: {result(test)}")

    test = not (pos1 != pos2)
    print(f"Two different position objects can be not equal: {result(test)}")

    print("~" * 50, "\n\n")


def TEST_replace(PL):
    print("~" * 50)
    print(f"{P}TEST CATEGORY: Replacing Nodes{W}\n")

    print(f"\n{B}Current PL: {PL}{W}\n")

    pos = PL.before(PL.before(PL.before(PL.last())))
    print(f"{B}Node to be replaced: |{pos.get_value()}|{W}\n")

    print(pos)
    print(type(pos))
    old_value = PL.replace(pos, "⭐ ")

    print(f"{B}A Node was replaced: {PL}{W}\n")

    test = pos.get_value() == "⭐ "
    print(f"Position object was updated: {result(test)}")

    test = old_value == "G"
    print(f"The original position node value was returned: {result(test)}")

    print("~" * 50, "\n\n")


def TEST_delete(PL, class_ref):
    print("~" * 50)
    print(f"{P}TEST CATEGORY: Replacing Nodes{W}\n")

    test_PL = class_ref()
    test_pos = test_PL.add_first("X")

    print(f"\n{B}Current PL: {PL}{W}\n")

    pos = PL.before(PL.before(PL.before(PL.last())))
    print(f"{B}Node to be deleted: |{pos.get_value()}|{W}\n")

    val = PL.delete(pos)
    print(f"{B}A node was deleted: {PL}{W}\n")

    test = val == "⭐ "
    print(f"Delete returns the node value: {result(test)}")

    test = len(PL) == 7
    print(f"Delete decreases PL size: {result(test)}")

    test = test_sequence(PL, [None, "B", "H", "E", "A", "C", "F", "D", None])
    print(f"Next and Prev of deleted node are joined: {result(test)}")

    try:
        PL.delete(test_pos)
        print(f"Delete validates incoming position: {result(False)}")
    except:
        print(f"Delete validates incoming position: {result(True)}")

    try:
        PL.delete(pos)
        print(f"Cannot delete an already deleted node object: {result(False)}")
    except:
        print(f"Cannot delete an already deleted node object: {result(True)}")

    for i in range(len(PL)):
        PL.delete(PL.first())

    print(f"\n{B}The list was emptied: {PL}{W}\n")

    test = len(PL) == 0 and test_sequence(PL, [None, None])
    print(f"List was emptied successfully: {result(test)}")

    print("~" * 50, "\n\n")

import unittest


class List(list):
    # Class functions that begin with double underscore __ are called special functions in Python.
    # Now That I know this - Because I want to overload one function from list yet have the rest:
    # Must Inherit List in order to Have all other functionality(HW REQUIREMENT)
    def __init__(self, pylist):  # To Create Our List we Must Give it A Proper Python List
        # Will Use This When List must act as Original List
        super().__init__(pylist)

    def __getitem__(self, index):
        try:
            # In mathematics, a tuple is a finite ordered list (sequence) of elements. An n-tuple is a sequence (or
            # ordered list) of n elements, where n is a non-negative integer.
            if isinstance(index, tuple):
                derivativelist = super(List, self).__getitem__(index[0])
                # If Consists of more than one, Must Implement a Special get item(Overload)
                # We Will Work via Slice Logic - Start With First List and slice according to index tuple Why Does this
                # Work - Index is a Tuple so index[0] is the first number that we give inside [] if not 1 digit
                # Now It's Simple, Keep Slicing Until I get to what i need from the tuple and keep updating the der list
                # Last - When no more to slice - Return the List
                for i in index[1:]:
                    derivativelist = derivativelist[i]
                return derivativelist
            else:
                # Original Python List Return
                return super().__getitem__(index)
        except:
            # Wrapped in Try and Catch for additional error catching
            return "Error Catched"


class Testing(unittest.TestCase):

    def test_nonpythonlist(self):
        # Exactly as Given by EREL
        testlist = List([
            [[1, 2, 3, 33], [4, 5, 6, 66]],
            [[7, 8, 9, 99], [10, 11, 12, 122]],
            [[13, 14, 15, 155], [16, 17, 18, 188]],
        ])
        # Regular Call + Usage
        self.assertEqual(testlist[0, 1, 3], 66)
        self.assertEqual(testlist[0], [[1, 2, 3, 33], [4, 5, 6, 66]])
        self.assertEqual(testlist[1, 1], [10, 11, 12, 122])
        self.assertEqual(testlist[1, 0], [7, 8, 9, 99])
        # Bad Tests (Too Many Indexes, Not Valid Index....)

        self.assertEqual(testlist[3,4,2], "Error Catched")
        self.assertEqual(testlist['a'], "Error Catched")
        self.assertEqual(testlist[3,2,'a'], "Error Catched")




if __name__ == "__main__":
    # Exactly as Given by EREL
    testlist = List([
        [[1, 2, 3, 33], [4, 5, 6, 66]],
        [[7, 8, 9, 99], [10, 11, 12, 122]],
        [[13, 14, 15, 155], [16, 17, 18, 188]],
    ])
    print(testlist[0])

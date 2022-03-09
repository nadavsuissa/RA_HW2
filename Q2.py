import unittest


# Help From https://www.delftstack.com/howto/python/class-decorator-in-python/
class lastcall:

    # Build and Assign
    def __init__(self, decfunc):
        # returned output
        self.prevanswer = ""
        # prev argument call
        self.prevcall = ""
        temp = {}
        # Our Func call
        self.func = decfunc

    # For example, we have function A, and we want to add functionalities without modifying them permanently. We can
    # use a decorator as a class by using the __call__ method.
    def __call__(self, *args, **kwargs):
        # Code before the function call || Check That Inputted Diff Args So we Have Diff Output
        funcarg = str(str(args) + str(kwargs))  # Func Argument Checking( Stringfy the parameters and comp)
        # Obviusly same Arguments so Will Return like expected that this has been executed
        if funcarg == self.prevcall:
            # Like Asked in HW to Return
            answerforprint = str(self.prevanswer)
            return "I already told you that the answer is " + answerforprint + "!"

        self.prevcall = funcarg
        # Code after the function call
        # Exec Func and save Output
        self.prevanswer = self.func(*args, **kwargs)  # Our Given Func Called and Result passed to - prevanswer
        return self.prevanswer  # Final Return



class Testing(unittest.TestCase):

    def test_nonpythonlist(self):
        # Exactly as Given by EREL
        @lastcall
        def f(x: int):
            return x ** 2

        # Regular Call + Usage + Bad Call
        self.assertEqual(f(2), 4)  # Good
        self.assertEqual(f(4), 16)  # Good
        self.assertEqual(f(4), "I already told you that the answer is 16!")  # Good
        self.assertEqual(f(4), "I already told you that the answer is 16!")  # Good
        self.assertEqual(f(2), 4)  # Good


@lastcall
def f(x: int):
    return x ** 2


if __name__ == "__main__":
    print(f(4))
    print(f(4))
    print(f(4))

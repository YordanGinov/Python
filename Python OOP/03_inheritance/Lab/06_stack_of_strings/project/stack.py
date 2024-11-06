class Stack():
    def __init__(self, *args) -> None:
        self.data = [str(el) for el in args]

    def push(self, element: str) -> None:
        self.data.append(str(element))

    def pop(self) -> str:
        return self.data.pop()

    def top(self) -> str:
        return self.data[-1]

    def is_empty(self) -> bool:
        return not any(self.data)

    def __str__(self) -> str:
        return "[" + ", ".join(reversed(self.data)) + "]"

stack = Stack()
stack.push("apple")
stack.push("carrot")
print(str(stack))
print(stack.pop())
print(stack.top())
stack.push("cucumber")
print(str(stack))
print(stack.is_empty())

# # test zero
# import unittest
#
#
# class StackTests(unittest.TestCase):
#     def test_zero(self):
#         stack = Stack()
#         stack.push("apple")
#         stack.push("carrot")
#         self.assertEqual(str(stack), '[carrot, apple]')
#         self.assertEqual(stack.pop(), 'carrot')
#         self.assertEqual(stack.top(), 'apple')
#         stack.push("cucumber")
#         self.assertEqual(str(stack), '[cucumber, apple]')
#         self.assertEqual(stack.is_empty(), False)
#
#
# if __name__ == '__main__':
#     unittest.main()
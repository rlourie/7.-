class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)


def reverse(open_bracket_func):
    if open_bracket_func == ')':
        return '('
    else:
        return chr(ord(open_bracket_func) - 2)


def checker(open_br, check_str):
    My_Stack = Stack()
    for bracket in check_str:
        if bracket in open_br:
            My_Stack.push(bracket)
        elif My_Stack.is_empty() == False and My_Stack.peek() == reverse(bracket):
            My_Stack.pop()
        else:
            print("No correct")
            return

    if My_Stack.is_empty():
        print("Correct")
    else:
        print("No correct")


if __name__ == '__main__':
    check = '[[{())}]'
    open_bracket = ['(', '{', '[']
    checker(open_bracket, check)

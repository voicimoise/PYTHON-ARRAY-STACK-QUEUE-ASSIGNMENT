
class Stack:
    def __init__(self, max_size):
        self.stack = []
        self.max_size = max_size

    def push(self, item):
        if self.isFull():
            print("Stack is Full")
        else:
            self.stack.append(item)
            print(item, "pushed into stack")

    def pop(self):
        if self.isEmpty():
            print("Stack is Empty")
        else:
            print("Popped:", self.stack.pop())

    def peek(self):
        if self.isEmpty():
            print("Stack is Empty")
        else:
            print("Top element:", self.stack[-1])

    def isEmpty(self):
        return len(self.stack) == 0

    def isFull(self):
        return len(self.stack) == self.max_size

    def size(self):
        return len(self.stack)

# Main Program

s = Stack(5)

while True:
    print("\n--- STACK MENU ---")
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Is Empty")
    print("5. Is Full")
    print("6. Size")
    print("7. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        item = input("Enter element: ")
        s.push(item)

    elif choice == "2":
        s.pop()

    elif choice == "3":
        s.peek()

    elif choice == "4":
        print("Is Empty:", s.isEmpty())

    elif choice == "5":
        print("Is Full:", s.isFull())

    elif choice == "6":
        print("Stack Size:", s.size())

    elif choice == "7":
        print("Program Ended")
        break

    else:
        print("Invalid Choice")
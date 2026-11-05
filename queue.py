
class Queue:
    def __init__(self, max_size):
        self.queue = []
        self.max_size = max_size

    def enqueue(self, item):
        if self.isFull():
            print("Queue is Full")
        else:
            self.queue.append(item)
            print(item, "added to queue")

    def dequeue(self):
        if self.isEmpty():
            print("Queue is Empty")
        else:
            print("Dequeued:", self.queue.pop(0))

    def peek(self):
        if self.isEmpty():
            print("Queue is Empty")
        else:
            print("Front element:", self.queue[0])

    def isEmpty(self):
        return len(self.queue) == 0

    def isFull(self):
        return len(self.queue) == self.max_size

    def size(self):
        return len(self.queue)

# Main Program

q = Queue(5)

while True:
    print("\n--- QUEUE MENU ---")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Peek")
    print("4. Is Empty")
    print("5. Is Full")
    print("6. Size")
    print("7. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        item = input("Enter element: ")
        q.enqueue(item)

    elif choice == "2":
        q.dequeue()

    elif choice == "3":
        q.peek()

    elif choice == "4":
        print("Is Empty:", q.isEmpty())

    elif choice == "5":
        print("Is Full:", q.isFull())

    elif choice == "6":
        print("Queue Size:", q.size())

    elif choice == "7":
        print("Program Ended")
        break

    else:
        print("Invalid Choice")
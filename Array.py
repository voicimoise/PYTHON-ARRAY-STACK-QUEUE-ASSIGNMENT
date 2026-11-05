
# ARRAY OPERATIONS IN PYTHON

arr = [25, 10, 45, 30, 15]

while True:
    print("\n====== ARRAY OPERATIONS ======")
    print("1. List Elements")
    print("2. Search Element")
    print("3. Insert Element")
    print("4. Sort Array")
    print("5. Delete Element")
    print("6. Exit")

    choice = int(input("Enter your choice (1-6): "))

    if choice == 1:
        print("Array Elements:", arr)

    elif choice == 2:
        element = int(input("Enter element to search: "))

        if element in arr:
            print("Element found at index:", arr.index(element))
        else:
            print("Element not found!")

    elif choice == 3:
        element = int(input("Enter element to insert: "))
        arr.append(element)
        print("Element inserted successfully!")
        print("Updated Array:", arr)

    elif choice == 4:
        arr.sort()
        print("Sorted Array:", arr)

    elif choice == 5:
        element = int(input("Enter element to delete: "))

        if element in arr:
            arr.remove(element)
            print("Element deleted successfully!")
            print("Updated Array:", arr)
        else:
            print("Element not found!")

    elif choice == 6:
        print("Exiting Array Operations. Goodbye!")
        break

    else:
        print("Invalid choice! Please select between 1 and 6.")

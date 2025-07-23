import json


class Queue:
    def __init__(self, initialvalue=None):
        if initialvalue is None:
            self.__valuelist = []
        else:
            self.__valuelist = list(initialvalue)

    def insert(self, value):
        self.__valuelist.append(value)

    def pop(self):
        if self.is_empty():
            print("Erorr")
            return None
        return self.__valuelist.pop(0)

    def gettervaluelist(self):
        return self.__valuelist.copy()

    def is_empty(self):
        if not self.__valuelist:
            return True
        else:
            return False


class QueueOutOfRangeException(Exception):
    pass


class QueueName(Queue):
    QueueByName = {}

    def __init__(self, name, length=5):
        super().__init__()
        self.__length = length
        self.__name = name
        QueueName.QueueByName[name] = self

    def insert(self, value):
        if len(self.gettervaluelist()) >= self.__length:
            raise QueueOutOfRangeException(f"Queue {self.__name} is Full")
        super().insert(value)

    @classmethod
    def getQueueByName(cls, name):
        return cls.QueueByName[name]

    @classmethod
    def save(cls, file):
        valueData = {}
        for name, queue in cls.QueueByName.items():
            valueData[name] = {"values": queue.gettervaluelist()}
        with open(file, "w") as f:
            json.dump(valueData, f, indent=4)

    @classmethod
    def load(cls, file):
        with open(file, "r") as f:
            data = json.load(f)
        for name, info in data.items():
            q = cls(name)
            for value in info["values"]:
                q.insert(value)


def main():
    num_queues = int(input("How many queues do you want to create? "))

    for _ in range(num_queues):
        name = input("Enter queue name: ")
        length = int(input(f"Enter max size for queue '{name}': "))
        queue = QueueName(name, length)

    while True:
        print("\nChoose an option:")
        print("1 - Add elements to a queue")
        print("2 - Remove elements from a queue")
        print("3 - Check if a queue is empty")
        print("4 - Show queue contents")
        print("5 - Save queues")
        print("6 - Load queues")
        print("7 - Exit")

        try:
            choice = int(input("Enter option number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == 1:
            qname = input("Enter the queue name to add elements: ")
            if qname not in QueueName.QueueByName:
                print("Queue not found.")
                continue
            queue = QueueName.getQueueByName(qname)
            num_elements = int(
                input(f"How many elements do you want to add to queue '{qname}'? ")
            )
            for i in range(num_elements):
                value = input(f"Enter element #{i+1}: ")
                try:
                    value = int(value)
                except ValueError:
                    pass
                try:
                    queue.insert(value)
                except QueueOutOfRangeException as e:
                    print("Error:", e)

        elif choice == 2:

            qname = input("Enter the queue name to remove elements from: ")

            if qname not in QueueName.QueueByName:
                print("Queue not found")

                continue

            queue = QueueName.getQueueByName(qname)

            if queue.is_empty():
                print(f"Queue {qname} is already empty")

                continue

            queue.pop()

            print("Popped")

        elif choice == 3:
            qname = input("Enter the queue name to check if empty: ")
            if qname not in QueueName.QueueByName:
                print("Queue not foun.")
                continue
            queue = QueueName.getQueueByName(qname)
            if queue.is_empty():
                print(f"Queue {qname} is empty")
            else:
                print(f"Queue {qname} has elements")

        elif choice == 4:
            print("\nQueue contents:")
            for name in QueueName.QueueByName:
                queue = QueueName.getQueueByName(name)
                print(f"{name}: {queue.gettervaluelist()}")

        elif choice == 5:
            QueueName.save("queues.json")
            QueueName.save("queues.txt")
            print("Queues saved to queues.json and queues.txt")

        elif choice == 6:
            QueueName.QueueByName.clear()
            QueueName.load("queues.json")
            QueueName.load("queues.txt")
            print("Queues loaded from 'queues.json' and queues.txt")

        elif choice == 7:
            print("Program finished")
            break

        else:
            print("Invalid option, please try again")


if __name__ == "__main__":
    main()

# import pickle
# import pprint
#
#
# class Queue:
#     def __init__(self, initialvalue=None):
#         if initialvalue is None:
#             self.__valuelist = []
#         else:
#             self.__valuelist = list(initialvalue)
#
#     def insert(self, value):
#         self.__valuelist.append(value)
#
#     def pop(self):
#         if self.is_empty():
#             print("Erorr")
#             return None
#         return self.__valuelist.pop(0)
#
#     def gettervaluelist(self):
#         return self.__valuelist.copy()
#
#     def is_empty(self):
#         if not self.__valuelist:
#             return True
#         else:
#             return False
#
#
# class QueueOutOfRangeException(Exception):
#     pass
#
#
# class QueueName(Queue):
#     QueueByName = {}
#
#     def __init__(self, name, length=5):
#         super().__init__()
#         self.__length = length
#         self.__name = name
#         QueueName.QueueByName[name] = self
#
#     def insert(self, value):
#         if len(self.gettervaluelist()) >= self.__length:
#             raise QueueOutOfRangeException(f"Queue {self.__name} is Full")
#         super().insert(value)
#
#     def getname(self):
#         return self.__name
#
#     def __str__(self):
#         return f"Queue {self.__name} : {self.gettervaluelist()}"
#
#     @classmethod
#     def getQueueByName(cls, name):
#         return cls.QueueByName[name]
#
#     @classmethod
#     def save(cls, file):
#         with open(file, "wb") as f:
#             pickle.dump(cls.QueueByName, f)
#
#     @classmethod
#     def load(cls, file):
#         with open(file, "rb") as f:
#             cls.QueueByName = pickle.load(f)
#         for name, queue in cls.QueueByName.items():
#             print(f"{queue.getname()} : {queue.gettervaluelist()}")
#
#
# def mainQueue():
#     q1 = QueueName("abdo", length=5)
#     q1.insert(10)
#     q1.insert(23)
#     q1.insert(30)
#     q1.insert(2)
#     q1.insert(183)
#
#     try:
#         q1.insert(999)
#     except QueueOutOfRangeException as e:
#         print(e)
#
#     QueueName.save("file.txt")
#
#     QueueName.load("file.txt")
#
#     q_loaded = QueueName.getQueueByName("abdo")
#     print(q_loaded)
#
#     q2 = QueueName.getQueueByName("abdo")
#     print(q2)
#
#
# if __name__ == "__main__":
#     mainQueue()

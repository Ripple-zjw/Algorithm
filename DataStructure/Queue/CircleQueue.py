class CircleQueue:
    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.__k = k
        self.__head = -1
        self.__tail = -1
        self.__data = [None] * self.__k

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        if self.isEmpty():
            self.__head = 0
        self.__tail = (self.__tail + 1) % self.__k
        self.__data[self.__tail] = value
        return True

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        if self.__head == self.__tail:
            self.__head, self.__tail = -1, -1
            return True
        self.__head = (self.__head + 1) % self.__k
        return True

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        if self.isEmpty():
            return -1
        return self.__data[self.__head]

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        if self.isEmpty():
            return -1
        return self.__data[self.__tail]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        return self.__head == -1

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        return (self.__tail + 1) % self.__k == self.__head

class Queue:
    def __init__(self, capacity):
        self.front = self.size = 0
        self.rear = capacity - 1
        self.capacity = capacity
        self.Q = [None]*capacity
    #  Queue is full when size is equal to the capacity


    def isFull(self):
        return self.size == self.capacity

    #  Queue is full when size is equal to the zero

    def isEmpty(self):
        return self.size == 0

    def EnQueue(self, element):
        if self.isFull():
            print("Queue is Full ")
            return
        else:
            self.rear = (self.rear + 1) % self.capacity
            self.Q[self.rear] = element
            self.size += 1
            print("Enqueued  to queue is {}:".format(element))

    def DeQueue(self):
        if self.isEmpty():
            print("The Queue is empty nothing to delete:")
            return
        else:
            self.front = (self.front + 1) % self.capacity
            self.size -= 1

    # Function to get front of queue
    def que_front(self):
        if self.isEmpty():
            print("Queue is empty")
        # temp = self.front
        # print("front of the queue is{}:".format(temp))
        print("front of the queue is :", self.Q[self.front])

    # Function to get rear of queue
    def que_rear(self):
        if self.isEmpty():
            print("Queue is empty")

        print("Rear of the Queue is :", self.Q[self.rear])

    def print(self):
        idx = self.front
        while True:
            print(self.Q[idx])  # Print the element at the current index
            idx = (idx + 1) % self.capacity  # Update index using circular buffer
            if idx == (self.rear + 1) % self.capacity:  # Check if we have reached the end of the queue
                break







def main():
    queue = Queue(30)
    queue.EnQueue(3)
    queue.EnQueue(7)
    queue.EnQueue(10)
    queue.EnQueue(11)
    queue.DeQueue()
    queue.que_front()
    queue.que_rear()
    queue.print()

if __name__ == "__main__":
    main()





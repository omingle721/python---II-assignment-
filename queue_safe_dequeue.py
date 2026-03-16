from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, item):
        self.queue.append(item)
        print(item, "added to queue")

    def safe_dequeue(self):
        if len(self.queue) == 0:
            print("Queue is empty, cannot dequeue.")
        else:
            return self.queue.popleft()


# Create queue object
q = Queue()

# Add elements
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

# Remove elements
print("Dequeued:", q.safe_dequeue())
print("Dequeued:", q.safe_dequeue())
print("Dequeued:", q.safe_dequeue())

# Try removing from empty queue
print("Dequeued:", q.safe_dequeue())
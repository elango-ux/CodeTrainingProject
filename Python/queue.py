#queue
# it import deque class from  collections
from collections import deque
#now wrap this with deque object pass emty list as argument
queue = deque([])
# deque object has similar method append 
queue.append(1)
queue.append(2)
queue.append(3)
# to remove first item in the list but this method is used deque object not list
queue.popleft()
queue.popleft()
queue.popleft()
print(queue)
#check queue is empty
if not queue:
    print("empty")
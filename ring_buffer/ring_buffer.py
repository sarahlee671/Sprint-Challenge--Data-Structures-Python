class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    #set the new item to the current item
    self.storage[self.current] = item
    # if the current value is less than the capacity, add it to the list, otherwise set current to 0
    if self.current < self.capacity -1:
      self.current += 1
    else:
      self.current = 0

  def get(self):
    list = []
    for element in self.storage:
      if element is not None:
        list.append(element)
    return list

class BinarySearchTree:
  def __init__(self, value): 
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    if self.value is None:
      self.value = value

    else:
      if value < self.value:
        if not self.left:
          self.left = BinarySearchTree(value)
        else:
          self.left.insert(value)
      else:
        if not self.right:
          self.right = BinarySearchTree(value)
        else:
          self.right.insert(value)

  def contains(self, target):
    if self.value == target:
      return True
    else:
      if target < self.value:
        if not self.left:
          return False
        else:
          return self.left.contains(target)
      else:
        if not self.right:
          return False
        else:
          return self.right.contains(target)
        
  def get_max(self):
    if not self:
      return None
    max_value = self.value
    current = self
    while current:
      if current.value > max_value:
        max_value = current.value
      current = current.right
    return max_value

  def for_each(self, cb):
    cb(self.value) 
    if self.left:
      self.left.for_each(cb)
    if self.right:
      self.right.for_each(cb)
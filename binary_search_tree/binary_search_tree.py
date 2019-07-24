class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    if value <= self.value:
      if self.left:
        self.left.insert(value)
      else:
        self.left = BinarySearchTree(value)
    elif value > self.value:
      if self.right:
        self.right.insert(value)
      else:
        self.right = BinarySearchTree(value)

  def contains(self, target):
    if self.value == target:
      return True
    elif self.value > target:
      if self.left:
        return self.left.contains(target)
      else:
        return False
    elif self.value < target:
      if self.right:
        return self.right.contains(target)
      else:
        return False
    pass

  def get_max(self):
    if self.right:
      return self.right.get_max()
    else:
      return self.value
    pass

  def for_each(self, cb):
    cb(self.value)
    if self.left:
      self.left.for_each(cb)
    if self.right:
      self.right.for_each(cb)
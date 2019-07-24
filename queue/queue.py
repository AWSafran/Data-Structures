class List_Node:
  def __init__(self, value):
    self.value = value
    self.next = None

  def get_value(self):
    return self.value

  def get_next(self):
    return self.next

  def set_next(self, node):
    self.next = node

class Linked_List:
  def __init__(self):
    self.head = None
    self.tail = None
    self.length = 0

  def add_item(self, item):
    item = List_Node(item)
    if not self.head:
      self.head = item
      self.tail = item
    else:
      self.tail.set_next(item)
      self.tail = item
    self.length += 1

  def take_first(self):
    if not self.head is None:
      item = self.head
      self.head = item.get_next()
      self.length -= 1
      return item.get_value()
    else:
      return None

  def get_length(self):
    return self.length
    

class Queue:
  def __init__(self):
    self.size = 0
    # what data structure should we
    # use to store queue elements?
    # Linked List
    self.storage = Linked_List()

  def enqueue(self, item):
    self.storage.add_item(item)
  
  def dequeue(self):
    return self.storage.take_first()

  def len(self):
    return self.storage.get_length()

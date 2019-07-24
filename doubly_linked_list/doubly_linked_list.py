"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
  def __init__(self, value, prev=None, next=None):
    self.value = value
    self.prev = prev
    self.next = next

  """Wrap the given value in a ListNode and insert it
  after this node. Note that this node could already
  have a next node it is point to."""
  def insert_after(self, value):
    current_next = self.next
    self.next = ListNode(value, self, current_next)
    if current_next:
      current_next.prev = self.next

  """Wrap the given value in a ListNode and insert it
  before this node. Note that this node could already
  have a previous node it is point to."""
  def insert_before(self, value):
    current_prev = self.prev
    self.prev = ListNode(value, current_prev, self)
    if current_prev:
      current_prev.next = self.prev

  """Rearranges this ListNode's previous and next pointers
  accordingly, effectively deleting this ListNode."""
  def delete(self):
    if self.prev:
      self.prev.next = self.next
    if self.next:
      self.next.prev = self.prev

  def get_value(self):
    return self.value

  def get_next(self):
    return self.next

  def get_previous(self):
    return self.prev

"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class DoublyLinkedList:
  def __init__(self, node=None):
    self.head = node
    self.tail = node
    self.length = 1 if node is not None else 0

  def __len__(self):
    self.length = 0
    if self.head:
      current = self.head
      while current:
        self.length += 1
        current = current.next
    return self.length

  def add_to_head(self, value):

    if self.head:
      self.head.insert_before(value)
      self.head = self.head.get_previous()
      self.length += 1
    else:
      new_node = ListNode(value)
      self.head = new_node
      self.tail = new_node
      self.length = 1

  def remove_from_head(self):
    if self.head == self.tail:
      value = self.head.value
      self.head = None
      self.tail = None
      self.length = 0
      return value
    if self.head:
      value = self.head.get_value()
      next = self.head.get_next()
      self.head.delete()
      self.head = next
      self.length -= 1
      return value
    else:
      return None

  def add_to_tail(self, value):
    if self.tail:
      self.tail.insert_after(value) 
      self.tail = self.tail.get_next()
    else:
      node = ListNode(value)
      self.head = node
      self.tail = node
    self.length += 1

  def remove_from_tail(self):
    if self.head == self.tail:
      value = self.tail.value
      self.head = None
      self.tail = None
      self.length = 0
      return value

    if self.tail:
      value = self.tail.get_value()
      prev = self.tail.get_previous()
      self.tail.delete()
      self.tail = prev
      self.length -= 1
      return value
    else:
      return None

  def move_to_front(self, node):
    value = node.get_value()
    node.delete()
    self.head.insert_before(value)
    self.head = self.head.get_previous()

  def move_to_end(self, node):
    if node == self.head:
      node = self.remove_from_head()
      self.add_to_tail(node)
    elif self.tail == self.head or node == self.tail:
      pass # Do nothing, it's already at the end
    else:
      node.delete()
      self.add_to_tail(node.value)


  def delete(self, node):
    if node.get_previous() is None and node.get_next() is None:
      self.length = 0
      self.head = None
      self.tail = None
    elif node.get_previous() is None:
      self.remove_from_head()
    elif node.get_next() is None:
      self.remove_from_tail()
    elif node.get_next() and node.get_previous():
      node.delete()
      self.length -= 1
    
  def get_max(self):
    if self.head is None:
      return None
    else:
      current = self.head
      max = current.get_value()
      while current:
        if current.get_value() > max:
          max = current.get_value()
        current = current.get_next()

      return max

    


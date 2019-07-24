class Heap:
  def __init__(self):
    self.storage = []

  def insert(self, value):
    self.storage.append(value)
    self._bubble_up(len(self.storage) - 1)

  def delete(self):
    value = self.get_max()
    self._sift_down(0) #move first item to end
    del self.storage[-1] #remove the last item (formerly first item)
    return value
    
  def get_max(self):
    return self.storage[0]

  def get_size(self):
    return len(self.storage)

  def _bubble_up(self, index):
    while index != 0:
      parent_index = (index - 1) // 2
      if self.storage[parent_index] >= self.storage[index]:
        break
      else:
        self.storage[parent_index], self.storage[index] = self.storage[index], self.storage[parent_index]
        index = parent_index

  def _sift_down(self, index):

    if (index * 2 + 1) >= len(self.storage): #If both children are outside the range of the array, they don't exist in the tree
      #Now that we have our number without any children, we want to put it on the end to make it easier to delete
      #This means swapping with last item in array. Because we do this, it needs to bubble back up
      self.storage[index], self.storage[-1] = self.storage[-1], self.storage[index]
      return
    elif (index * 2 + 1) == len(self.storage) - 1: # If the first child is the last element in array, it's the only child
       big_child_index = index * 2 + 1
    else: # both children in array, need to compare them
      child_one = self.storage[index * 2 + 1]
      child_two = self.storage[index * 2 + 2]
      if child_one > child_two:
        big_child_index = index * 2 + 1
      else:
        big_child_index = index * 2 + 2
    self.storage[index], self.storage[big_child_index] = self.storage[big_child_index], self.storage[index]
    self._sift_down(big_child_index)
      

from doubly_linked_list import DoublyLinkedList

class TextBuffer:

    def __init__(self, init=None):
        self.contents = DoublyLinkedList()

        if init:
            for char in init:
                self.contents.add_to_tail(char)

    def __str__(self):
        s = ""
        current = self.contents.head
        while current:
            s += current.value
            current = current.next
        return s
    def append(self, string_to_add):
        for char in string_to_add:
            self.contents.add_to_tail(char)

    def prepend(self, string_to_add):
        for char in reversed(string_to_add):
            self.contents.add_to_head(char)
        pass

    def delete_front(self, chars_to_remove):
        for i in range(0, chars_to_remove):
            self.contents.remove_from_head()
        

    def delete_back(self, chars_to_remove):
        for i in range(0, chars_to_remove):
            self.contents.remove_from_tail()
    
    """
    Join other_buffer to self
    The input buffer gets concatenated to the end of this buffer 
    The tail of the concatenated buffer will be the tail of the other buffer 
    The head of the concatenated buffer will be the head of this buffer 
    """

    def join(self, other_buffer):
        # we might want to check that other_buffer is indeed a text buffer 
        # set self list tail's next node to be the head of the other buffer 
        
        # set other_buffer head's prev node to be the tail of this buffer
        other_buffer.contents.head.prev = self.contents.tail
        self.contents.tail.next = other_buffer.contents.head

        # effectively making them both the same buffer now that they've been combined
        self.contents.tail = other_buffer.contents.tail
        other_buffer.contents.head = self.contents.head
        
        pass

    def join_string(self, string_to_join):
        for char in string_to_join:
            self.contents.add_to_tail(char)


if __name__ == '__main__':
    text = TextBuffer("Super")
    print(text)

    text.join_string("califragilisticexpealidocious")

    text.append(" is ")
    text.join(TextBuffer("weird."))

    print(text)

    text.delete_back(6)
    print(text)

    text.prepend("Hey! ")
    print(text)

    text.delete_front(4)
    print(text)
def rearrangeLinkedList(head, k):
    smalestHead = None
    smakestTail = None
    eqHead = None
    eqTail = None
    greHead = None
    greTail = None

    node = head

    while node is not None:
        if node.value < k:
            smalestHead,smakestTail = growList(smalestHead,smakestTail,node)
        elif node.value > k:
            greHead,greTail = growList(greHead,greTail,node)			
        else:
            eqHead,eqTail = growList(eqHead,eqTail,node)
            
        prevNode = node
        node = node.next
        prevNode.next = None
        
    firstHead, firstTail = connectLinkedLists(smalestHead,smakestTail,eqHead,eqTail)
    finalHead, _ = connectLinkedLists(firstHead, firstTail,greHead,greTail)

    return finalHead

def growList(head,tail,node):
	newHead = head
	newTail = node
	
	if newHead is None:
		newHead = node		
	if tail is not None:
		tail.next = node
		
	return (newHead, newTail)

def connectLinkedLists(headOne, tailOne, headTwo, tailTwo):
	newHead = headTwo if headOne is None else headOne
	newTail = tailOne if tailTwo is None else tailTwo
	
	if tailOne is not None:
		tailOne.next = headTwo
	
	return (newHead, newTail)
	

# This is the class of the input linked list.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


import unittest


def linkedListToArray(head):
    array = []
    current = head
    while current is not None:
        array.append(current.value)
        current = current.next
    return array


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        head = LinkedList(3)
        head.next = LinkedList(0)
        head.next.next = LinkedList(5)
        head.next.next.next = LinkedList(2)
        head.next.next.next.next = LinkedList(1)
        head.next.next.next.next.next = LinkedList(4)
        result = rearrangeLinkedList(head, 3)
        array = linkedListToArray(result)

        expected = [0, 2, 1, 3, 5, 4]
        self.assertEqual(expected, array)

if __name__ == "__main__":
    unittest.main()
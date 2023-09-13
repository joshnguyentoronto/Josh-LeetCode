'''
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.


Example 1:
Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output:  [null,null,null,null,-3,null,0,-2]

Explanation
    MinStack minStack = new MinStack();
    minStack.push(-2);
    minStack.push(0);
    minStack.push(-3);
    minStack.getMin(); // return -3
    minStack.pop();
    minStack.top();    // return 0
    minStack.getMin(); // return -2
'''


###

# The easy part is push, pop, top
# The HARD part is getMin()
# Also using LinkedList take more memory but it's faster than array in push or pop operation

###
class LinkedList:
    def __init__(self):
        self.head = None

class Node:
    def __init__(self, value, nxt):
        self.val = value
        self.next = nxt

class MinStack:
    def __init__(self):
        self.stack = None
        self.minStack = None

    def push(self, val):
        if not self.stack:
            node = Node(val, None)
            self.stack = LinkedList()
            self.stack.head = node
        else:
            node = Node(val, self.stack.head)
            self.stack.head = node

            # Track minimum # everytime we push or pop
        if not self.minStack or not self.minStack.head:
            minNode = Node(val, None)
            self.minStack = LinkedList()
            self.minStack.head = minNode
        else:
            minimum = min(val, self.minStack.head.val)
            minNode = Node( minimum, self.minStack.head )
            self.minStack.head = minNode
        return

    def pop(self):
        node = self.stack.head
        self.stack.head = self.stack.head.next
        node = None
        # Track minimum # everytime we push or pop
        minNode = self.minStack.head
        self.minStack.head = self.minStack.head.next
        minNode = None
        return

    def top(self):
        return self.stack.head.val

    def getMin(self):
        return self.minStack.head.val


class LinkedList(object):

    class Node(object):

        def __init__(self, data = None , prv = None , nxt = None ):
            self._type_error(prv);
            self._type_error(nxt);
            
            self.data = data;
            self.prv = prv;
            self.nxt = nxt;
    
        @staticmethod
        def _type_error(obj):
            if not obj is None and not isinstance(obj, LinkedList.Node):
                raise TypeError;

    def __init__(self):        
        self.nil = LinkedList.Node();
        self.nil.nxt = self.nil; 
        self.nil.prv = self.nil; 

    def delete(self, node):
        """ Delete the given node from linked list, if contains it. """
        
        LinkedList.Node._type_error(node);

        if node in self:
            node.prv.nxt = node.nxt;        
            node.nxt.prv = node.prv;
        else:
            raise ValueError; 
            


    def insert(self, node):
        """ Insert the given node into the head of this linked list. """
        
        LinkedList.Node._type_error(node);

        node.nxt = self.nil.nxt;
        self.nil.nxt.prv = node;

        node.prv = self.nil;
        self.nil.nxt = node;


    def search(self, data):
        """ Return first node in linked list with the given data. """
        
        node = self.nil.nxt;
    
        while node is not self.nil and node.data != data:
            node = node.nxt;

        return node;

    def __contains__(self, node):
        item = self.nil.nxt;

        while item is not self.nil:
            
            if item is node:
                return True;

            item = item.nxt;
        
        return False;

    def is_empty(self):
        """ Returns true if linked list is empty, false otherwise."""
        return self.nil.nxt is self.nil;

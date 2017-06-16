import node

# Check to see if list is circular
# Method takes head
def has_cycle(head):
    # Dictionary to keep track of nodes that have been seen
    seen = {}

    if head == None:
        return False

    current_node = head
    default = None

    while current_node != None:
        # If you have already seen the Node, it is circular
        # and True should be returned
        if seen.get(current_node,default) != None:
            return True
        # If the node has not been seen, place it in the dictionary
        seen[current_node] = True

        # get next_node
        current_node = current_node.next
    # If you get through the entire list, it is not circular
    # Return false
    return False

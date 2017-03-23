#You are given a node that is the beginning of a 
#linked list. This list always contains a tail and a loop.
#Your objective is to determine the length of the loop.
# Use the `next' attribute to get the following node
#node.next

#my code
def loop_size(node):
    found = 0
    visited_nodes = 0
    while not found:
        try:
            found = node.visited
        except AttributeError:
            visited_nodes += 1
            node.visited = visited_nodes
        node = node.next
    return visited_nodes - found + 1

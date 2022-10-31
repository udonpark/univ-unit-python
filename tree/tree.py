class Node:
    def __init__(self, key):
        """
        Node class to store each element.
        :param key: string to store
        """
        self.key = key
        self.left = None
        self.right = None
        # self.rightsum = 0
        # self.leftsum = 0
        self.total = 0  # I have made a new variable to store how many total nodes are below a certain node.

    def get_total(self):
        """
        useful when finding how many items of text list is already lexicographically greater later on.
        :return: number of nodes stored in its branch
        """
        return self.total  # this returns total number of nodes below.


class Tree:
    def __init__(self, *args):
        """
        Tree class. I have referred to some of the codes in Task 2.
        :param args: list of strings to input
        """
        self.node = None
        self.height = -1

        if len(args) == 1:
            for i in args[0]:
                self.insert(i)

    def insert(self, key):
        tree = self.node
        newnode = Node(key)

        if tree is None:  # if no item, then instantiate new node in that part of the tree
            self.node = newnode
            self.node.left = Tree()
            self.node.right = Tree()

        elif key < tree.key:  # if key is lexicographically smaller, add it at left
            self.node.left.insert(key)
            self.node.total += 1  # increment total when new item added below it

        elif key > tree.key:  # if bigger, connect it to the right
            self.node.right.insert(key)
            self.node.total += 1

        elif key == tree.key:  # although it does not in Task 2, Task 1 could contain duplicate items. in that case,
            # I will add it to right to balance it after.
            self.node.right.insert(key)
            self.node.total += 1


def lex_pos(text: list, queries: list) -> list:
    """
    Documentation:
    I will have to minimize as much time required by storing the comparison of all items in the first iteration.
    In order to keep complexity in O(N+M) when N and M are sum of all characters, string comparisons for each item
    are to be done only once.
    Only once and their orders has to be reliably stored, that is why I use Tree structure. I will use AVL Tree instead
    of Binary Search Tree. This is because it only takes O(1) to rebalance after each insertion. And when traversing,


    :param text:list of strings
    :param queries: list of strings to compare
    :return: list containing integer, each representing number of strings lexicographically greater than each one in
    queries
    """
    tree = Tree(text)
    node = tree.node
    lst = []
    if queries is None:  # if the input is empty, return list of none
        return lst
    for item in queries:
        lst.append(nodes_greater(node, item))  # add to each list


def nodes_greater(node: Node, query: str) -> int:
    """
    A helper function to find number of nodes greater than that.
    It uses efficinetly the characteristics of AVL tree, to return how many items are greater.
    Since string comparison uses O(N) complexity worst case for N characters, we can't be using list every time.
    """
    if node is None:  # A recursion. if empty, no item that is smaller than that.
        return 0
    elif node.key > query:  # if query is less than that node, that means all items greater than node would fill the
        # requirement, hence adding right.get_total(). furthermore, it calls recursively nodes_greater of node left
        # to see how many would fill the condition in its branches
        return nodes_greater(node.left, query) + node.right.get_total() + 1
    else:  # if not, we must still recursively search to obtain integer
        return nodes_greater(node.right, query)


text = ["aaa", "bab", "aba", "baa", "baa", "aab", "bab"]
queries = ["", "a", "b", "aab"]
print(lex_pos(text, queries))

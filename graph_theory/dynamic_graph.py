# I have used heapq instead of minheap
import heapq

class Graph:
    """
    Graph class. This is from Ed which was given as a base code
    """
    class WeightedEdge:
        def __init__(self, dest, weight):
            """
            initializes information of edge which are weighted
            :param dest: destination index
            :param weight: weight, distance for travel
            """
            self.dest = dest
            self.weight = weight

    def __init__(self, n):
        """
        initializes Graph, with its space for adjacency list
        :param n: number of vertices added
        """
        self.adj_list = [[] for _ in range(n)]
        self.num_vertices = n

    def add_directed_edge(self, source, dest, weight):
        """
        Adds and registers an edge to a graph
        :param source: integer, the start index
        :param dest: integer, the target index
        :param weight: integer, showing the weight/distance
        :return: None
        """
        self.adj_list[source].append(Graph.WeightedEdge(dest, weight))

    def __len__(self):
        """
        A method that I added to find out the length
        :return: an integer, the length of the adjacency list
        """
        return len(self.adj_list)


class Graph2:
    """
    Graph 2 class, which is to be used in Task 2. Very similar structure to Graph but allows better
    and easier extension of the code
    """
    class WeightedEdge:
        def __init__(self, dest, weight):
            """
            initializes information of edge which are weighted
            :param dest: destination index
            :param weight: weight, distance for travel
            """
            # self.source = source
            self.dest = dest
            self.weight = weight

    def __init__(self, n):
        """
        initializes Graph, with its space for adjacency list
        :param n: number of vertices added
        """
        self.adj_list = [[] for _ in range(n)]
        self.num_vertices = n

    def add_directed_edge(self, index, source, weight):
        """
        Adds and registers an edge to a graph
        :param source: integer, the start index
        :param index: integer, the target index
        :param weight: integer, showing the weight/distance
        :return: None
        """
        self.adj_list[source].append(Graph2.WeightedEdge(Vertex(index), weight))

    def __len__(self):
        """
        finds the length
        :return: integer n, length of the list
        """
        return len(self.adj_list)


class Vertex:  
    def __init__(self, index):
        """
        class that stores information on vertex
        :param index: integer showing the index of the vertex
        """
        self.index = index
        # self.word = word
        self.discovered = False
        self.visited = False
        self.edges = []


# usage example
# g = Graph(4)
# g.add_directed_edge(0, 1, 5)
# g.add_directed_edge(0, 2, 10)

# print neighbours of 0
# for edge in g.adj_list[0]:
#     print(edge.dest, edge.weight)


# Assumption that there is no duplicate in list of words, as specified

class WordGraph:
    """
    Word Graph class which is responsible for holding graph of the given data
    """
    def __init__(self, words):
        """
        Constructor which initializes which stores input in required data structure
        :param words: list of strings, words to store in the WordGraph
        :complexity: Not required, constructor complexity is negligible according to the nature of this assignment
        """
        n = len(words)
        self.words = words
        self.g = Graph(n)  # declare self.g as Graph
        for i in range(n):
            word = words[i]
            for j in range(n):  # go on a loop to see its in adjacent Word Ladders
                if i == j:
                    continue  # to not consider itself
                count = 0  # only connect if they differ by one character
                for k in range(len(word)):
                    if word[k] != words[j][k]:  # checks character by character
                        count += 1
                if count == 1:  # if condition of word ladders are met
                    self.g.add_directed_edge(i, j, 1)  # initialize and add into adjacency list

        # Below is the declaration for TASK 2. I have used ord to find the alphabetical distance.
        self.g2 = Graph(n)
        for i in range(n):
            word = words[i]
            for j in range(n):
                if i == j:
                    continue  # to not consider itself
                count = 0  # only connect if they differ by one character
                char_difference = 0
                for k in range(len(word)):
                    if word[k] != words[j][k]:
                        count += 1
                        # Takes absolute value of the alphabetical distance
                        char_difference = abs(ord(word[k]) - ord(words[j][k]))
                if count == 1:
                    self.g2.add_directed_edge(i, j, char_difference)  # initialize and add into adjacency list

    def create_matrix(self):
        """
        A helper method which helps create the Adjacency Matrix which helps me perform Floyd-Warshall
        :complexity: O(N^2) where N is the number of words stored
        :return: a tuple containing integer showing length of the matrix, and a 2-dimensional list with n x n.
        """
        n = len(self.g)
        matrix = [[float('inf')] * n for _ in range(n)]  # initialize matrix to infinity
        for i in range(n):
            matrix[i][i] = 0  # set diagonal to 0

        for i in range(n):
            # for j in range(len(self.g.adj_list[i])):
            for j in self.g.adj_list[i]:
                if len(self.g.adj_list[i]) != 0:
                    matrix[i][j.dest] = 1  # Converts adjacency list into Matrix!

        return n, matrix


    """
    def locate_target(self, target_words):
        index_lst = []
        for item in target_words:
            for index in range(len(self.words)):
                if item == self.words[index]:
                    index_lst.append(index)
        return index_lst
    """

    def best_start_word(self, target_words):
        """
        A method required for task1. It performs Floyd-Warshall algorithm and finds optimal
        start word, for which finding word ladders to all the targets is as easy as possible.
        :param target_words: a nonempty list of indices of words in the graph.
        :return:  an integer, which is the index of the word in the graph which produces
        the overall shortest word ladders to each of the words in target_words. Returns -1 if such does not exist.
        :complexity: O(N^3) where N is the number of words in the instance of a WordGraph. this is due to
        3 nested loops and there is no way to end the loop earlier due to the nature of this algorithm.
        """
        n, matrix = self.create_matrix()  # gets matrix using the helperm, following Single Responsibility Principal
        # and to make smoother debugging
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if matrix[i][j] > matrix[i][k] + matrix[k][j]:
                        matrix[i][j] = matrix[j][k] + matrix[k][j]  # performed floyd warshall

        distance_lst = []  # stores the longest distance from a source to any distance, for all sources
        for i in range(n):
            longest_distance = 0
            for j in range(n):
                if j in target_words and matrix[i][j] > longest_distance and matrix[i][j] != float('inf'):
                    longest_distance = matrix[i][j]  # longest distance excluding infinity
            distance_lst.append(longest_distance)

        print(distance_lst)  # You may delete this line if it is disturbing. However, this was useful to see that
        # this algorithm works
        min_index = -1
        min_value = float('inf')

        if len(distance_lst) == 1 and len(self.g.adj_list[target_words[0]]) == 0:
            min_index = target_words[0]  # target is yourself if length is 0 and fulfills condition

        for i in range(len(distance_lst)):
            # if distance_lst[i] == 0 and min_index == -1:
            #     min_index = i   # if longest is 0, it should not return -1 but instead consider 0
            if min_value > distance_lst[i] != 0:  # exclude 0 as it means the item is isolated
                min_index = i
                min_value = distance_lst[i]

        return min_index

    def reachable(self, source):
        """
        A helper method for Task 2, which returns a tuple showing the weight and destination accordingly
        :param source:
        :return: A tuple, containing an integer for weight of the edge and an integer showing the index for the
        destination
        :complexity: O(N) where N is the number of words stored in this class. this is becasue the loop is
        done n times without any nested loops.
        """
        lst = []
        for vertex in self.g2.adj_list[source]:
            lst.append([vertex.weight, vertex.dest])
        return lst


    """
    def constrained_ladder(self, start, target, constraint_words):
        n = len(self.g2)
        distance = [float('inf')] * n
        distance[start] = 0
        full_distance = [float('inf')] * n
        full_distance[start] = 0

        history = []
        visited = [0] * n
        visited[start] = 1
        fully_visited = [0] * n
        fully_visited[start] = 0

        constraint_filled = [0] * len(constraint_words)  # boolean list for detour words

        new_start = start
        while new_start != target and (0 in constraint_filled):  # until it reaches the target, keep iterating
            discovered = []
            visited = [0] * n
            distance = [float('inf')] * n
            distance[new_start] = 0
            # list pack contain: (distance/weight, destination)
            for pack in self.reachable(new_start):
                heapq.heappush(discovered, pack)

            while len(discovered) > 0:
                w, v = heapq.heappop(discovered)  # w, v are source and destination
                # take out using priority queue
                for i in range(len(constraint_words)):
                    if constraint_words[i] == v:
                        constraint_filled[i] = 1  # if constraint is met, then turn it into true

                if visited[v]:
                    continue
                visited[v] = 1
                history.append(v)
                distance[v] = w

                for pack in self.reachable(new_start):
                    if not visited[pack[1]]:
                        heapq.heappush(discovered, [pack[0] + distance[v], pack[1]])

            min_value = float('inf')
            min_index = 0
            for i in range(len(distance)):
                if min_value > distance[i] and i != start:
                    min_index = i
                    min_value = distance[i]  # find lowest distance path
            new_start = min_index
            print(new_start)
            print(history)

        return distance
        """
    def constrained_ladder(self, start, target, constraint_words):
        """
        This is Task 2, a function that returns the list of indices of vertices (in order) corresponding to words
        representing the word ladder which
            • starts with start
            • ends with end
            • contains at least one word from constraint_words (it may contain more than one, and
            the word can appear at any point in the word ladder, including the first or last word)
            • has the minimum alphabetic distance out of all word ladders which satisfy the first
            three conditions.

        This is done by Djikstra Algorithm, and although incomplete below are the codes.
        :param start: integer, index of starting vertex
        :param target: integer, index of the target vertex to reach
        :param constraint_words: list of indices, which at least one must appear during the word ladder
        :return:  the list of integers, indices of vertices (in order) corresponding to words
        representing the word ladder. Returns None if not found.
        :complexty:
        Currently, my complexity is O(W log W) where W represents the number of words in WordGraph, and
        This is because I have used priority queue with heapq, so some of complexity taken
        for the initial O(W^2) has been reduced. We have minimizes the number of the iteration by considering the
        most smallest vertex when picking from the list of vertices.
        """
        """
        There was another way to efficiently implement this Task 2, by taking another layer of the graph.
        Such that we only conclude that the path is acceptable when it has passed through one of the constraint_word
        and is sent to the another layer, with weight 0.
        This is an idea introduced by Studio in week 10 by Sir, but I did not have an ability to make it work
        within the complexity.
        """
        n = len(self.g2)
        distance = [float('inf')] * n
        distance[start] = 0  # stores all distances, and sets the starting to 0
        history = []
        discovered = []  # to be queued
        visited = [0] * n
        visited[start] = 1  # set list showing visited
        constraint_filled = [0] * n  # boolean list for all detour words that have been met
        for i in range(len(constraint_words)):
            if constraint_words[i] == start:
                constraint_filled[i] = 1  # We can count starting point as a constraint being met!

        # tuples pack contain: (distance/weight, destination)
        for pack in self.reachable(start):
            heapq.heappush(discovered, pack)

        while len(discovered) > 0:
            w, v = heapq.heappop(discovered)  # w, v are source and destination
            if visited[v]:
                continue
            visited[v] = 1
            history.append(v)
            distance[v] = w

            # for i in range(len(constraint_words)):
            #     if constraint_words[i] == v:
            #         constraint_filled[i] = 1  # if constraint is met, then turn it into true

            for pack in self.reachable(start):
                if not visited[pack[1]]:
                    heapq.heappush(discovered, [pack[0] + distance[v], pack[1]])
        print(history)  # history shows travel history
        print(distance)  # distance list taken
        output = []
        for i in range(len(distance)):
            if ((i in constraint_words) or (i == target)) and distance[i] != float('inf'):
                # if detour is found in distance, or the destination is the target itself
                constraint_filled[i] = 1  # if constraint is met, then turn it into true
                output.append(i)
        if 1 in constraint_filled:  # that means all constraints are met
            return output  # return shortest distance

        else:  # if constraints are not met or target is not found
            return None


words = ["aaa", "aad", "dad", "daa", "aca", "acc", "aab", "abb"]
g = WordGraph(words)
print(g.best_start_word([2,7,5]))
# should print 0
print(g.best_start_word([6,2]))
# should print 1
print(g.best_start_word([0,4,5]))
# should print 4

# print(g.constrained_ladder(0, 3, ["aaa"]))

words = ["aaa","bbb","bab","aaf","aaz","baz","caa","cac","dac","dad","ead","eae","bae","abf","bbf"]
start = 0
end = 3
detour = [3]

g2 = WordGraph(words)
print(g2.constrained_ladder(start, end, detour))
# this should return [3]

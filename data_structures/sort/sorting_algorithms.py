import random
import string
import timeit
import matplotlib.pyplot as plt



def aux(integer: int, base: int, n: int) -> int:
    """
    A helper function to take in 3 integers to find the value of nth digit in base of base.
    e.g., aux(12345, 10, 4) returns 4th digit from right, which is 2.
    :complexity: O(1) since they are all althmetic operations
    """
    return integer // (base ** n) % base


def counting_sort(lst: list, base: int, n: int) -> list:
    """
    This is a counting_sort function that helps num_rad_sort().
    :param lst: a list of non-negative integers
    :param base: an integer showing the base of the radix sort
    :param n: an integer showing the digit to find out
    :return: returns a sorted list of integers of the input lst.
    :complexity: O(N+K) where N is the number of elements in lst and K is the range of the largest element and
    smallest element
    :SPACE_COMPLEXITY: Space complexity is also O(N+K) where N is the number of elements in lst and K is the range of
    largest element and smallest element. If K is large, so the range of values are, e.g., 0-1000000, we must note that
    it takes up a lot of space.
    """
    # For the implementation of counting_sort, I did refer to my own attempt at Tutorial questions in week 3
    # the size of the count array would be base, e.g., base 10 has 10 spaces for 0-9
    count_array = [0] * base
    for item in lst:
        count_array[aux(item, base, n)] += 1
    # count array is created

    rank_array = [0] * base
    for i in range(1, base):
        rank_array[i] = count_array[i - 1] + rank_array[i - 1]
    # rank array is now made, containing a cumulative and actual position of the sorted

    output = [0] * len(lst)
    for item in lst:
        output[rank_array[aux(item, base, n)]] = item
        rank_array[aux(item, base, n)] += 1  # increment rank to avoid duplicates
    # output array is complete and sorted
    return output


def num_rad_sort(nums: list, b: int) -> list:
    """
    :param nums: unsorted list of non-negative integers
    :param b: integer with value >= 2
    :return: it outputs a list of integers, nums sorted in ascending numerical order
    :complexity: O((n+b)*logbM) where n is the length of nums, b is the value of b and M
    is the maximum numerical value in nums.
    this is because, logbM decides how many times it has to perform iteration in while loop.
    if b = 10, M is 123, it has to cover for 3 digits in decimal form, hence repeating the counting sort(O(n+b))
    3 times.
    """
    if not nums:
        return nums  # return an empty string if an empty string is input

    m = nums[0]
    for item in nums:
        if item > m:
            m = item
    # find maximum m, maximum value in the list. I could use max() but I prefer this way.
    counter = 0
    while m > (b ** counter):  # keep looping while it does't exceed the maximum value
        nums = counting_sort(nums, b, counter)
        counter += 1
    # now nums is fully sorted
    return nums


"""
Here are my attempts at Question 2.
"""


def base_timer(num_list: list, base_list: list) -> list:
    """
    A timer to find the runtime of radix sort
    :param num_list: list of non-negative integers to sort
    :param base_list: list of integers, all with values >= 0, sorted in ascending order
    :return: a list of time taken to perform sorting num_rad_sort on each element
    :complexity: Since complexities are excused for this task 2, I will ignore on the documenting of it
    """
    time_list = [0] * len(base_list)  # initialize time_list to record time
    for i in range(len(base_list)):
        start_time = timeit.default_timer()
        num_rad_sort(num_list, base_list[i])
        time = timeit.default_timer() - start_time
        time_list[i] = time  # test for each element i, by using imported timeit function
    return time_list


# here are the codes I ran. Documentations are in the explanation.pdf.
"""
random.seed("FIT2004S22021")
data1 = [random.randint(0, 2**25) for _ in range(2**15)]
data2 = [random.randint(0, 2**25) for _ in range(2**16)]
bases1 = [2**i for i in range(1, 23)]
bases2 = [2*10**6 + (5*10**5)*i for i in range(1, 10)]


y1 = base_timer(data1, bases1)
y2 = base_timer(data2, bases1)

plt.plot([i for i in range(1, 23)], y1, label="y1")
plt.plot([i for i in range(1, 23)], y2, label="y2")
plt.xlabel('Bases (Log2)')
plt.ylabel('Time taken /s')
plt.title('Graphs using bases1')
plt.legend()
plt.show()


y3 = base_timer(data1, bases2)
y4 = base_timer(data2, bases2)

plt.plot(bases2, y3, label='y3')
plt.plot(bases2, y4, label='y4')
plt.xlabel('Bases')
plt.ylabel('Time taken /s')
plt.title('Graphs using bases2')

plt.legend()
plt.show()
"""
# I have referred to :https://www.w3resource.com/graphics/matplotlib/basic/matplotlib-basic-exercise-5.php
# For the plotting of two graphs

"""
Below are my attempts on Question 3
"""


def aux_str(word: string, col: int) -> int:
    """
    A helper function that converts input strings a-z to 1-26 accordingly.
    The reason I did not use 0-25, is because in my implementation I wanted to use 0 to represent
    space, " " an empty character.
    :param word: the string to consider
    :param col: orders function to consider col-th character in word
    :return: corresponding integers 0-26
    :complexity: O(1), since they are arithmetic/simple operations whose complexities are constant
    """
    if word[col] == " ":
        return 0
    else:
        return ord(word[col]) - 96  # use ord to convert characters to numerical values in ascii


def str_counting_sort(lst: list, base: int, col: int, m: int) -> list:
    """
    For this sorting, I have referred to RaxisSort_String_LengthTrick.pdf from Mr Ian Week 4.
    A helper function to perform counting sort on given list of strings.
    SORTING FROM RIGHT SIDE OF THE STRING.
    :param lst: list of strings, SORTED IN ASCENDING ORDER OF LENGTH OF STRINGS
    :param base: an integer that represents base, this is usually 27 since we consider 26 characters + " "
    :param col: integer showing the index of the string from right side.
    :param m: the length of the longest string in lst
    :return: returns sorted list of lst alphabetically, in ascending order
        e.g.
    cat
    catt
    aaaaa
        # will be iterated from right-most character, index string[-1], this is similar to padding method

    :complexity: O(NM) where n is the number of strings in the list and M is the length of the longest string.
    There is an efficient algorithm that makes it O(N) where N is the sum of all string lengths by exiting loop
    where an empty character is found, but in this case it is not.
    My complexity here, is O(NM) since each column is iterated same number of time, because even empty strings
    are counted and it depends on the length of the longest string.
    :BEST_CASE_COMPLEXITY: in the best case scenario, it complexity would be O(N).
    In the worst case all length of strings are same(M) so it will be O(NM), but in the best case
    one element has M but all other strings have length of 1. In that case, 1 will be small compared to M,
    and it can be reduced down to O(N).
    """
    count_array = [0] * base
    for item in lst:
        if len(item) <= (m - col):  # if the string is " " , treat it as 0 before "a" which is 1
            count_array[0] += 1
        else:
            count_array[aux_str(item, m - col)] += 1
    # Most of the codes are based on counting_sort in Q1. I modified
    # crucial parts to be able to apply to strings.
    # There maybe more efficient codes, but I would like to do this way to keep consistency and
    # deepen my understanding

    rank_array = [0] * base
    for i in range(1, base):
        rank_array[i] = count_array[i - 1] + rank_array[i - 1]
    # similar to rank array in Q1

    output = [0] * len(lst)
    for item in lst:
        if len(item) <= (m - col):
            output[rank_array[0]] = item
            rank_array[0] += 1  # those with " " character at col, will be treated first, with the stability
        else:
            output[rank_array[aux_str(item, m - col)]] = item
            rank_array[aux_str(item, m - col)] += 1
    return output


def sort_by_length(lst: list, m: int) -> list:
    """
    This is a helper function again, to sort list of strings by its length.
    I used methodology of counting sort.
    The reason for this is that there was a need to pre-process by sorting from shortest to largest,
    in the interest_groups that I will be implementing.
    :param lst: list of non-empty strings, unsorted
    :param m: maximum length of string, in the longest string in lst
    :return: sorted list with. It is stable due to the property of the radix sort
    :complexity: O(NM) where N is the number of strings in list and M is the length of longest
    string in the list.
    """
    count_array = [0] * m
    for item in lst:
        count_array[len(item)] += 1

    rank_array = [0] * m
    for i in range(1, m):
        rank_array[i] = count_array[i - 1] + rank_array[i - 1]
    # again, count arrays and rank arrays are made for lengh of each strings
    # there is a short form of this, but I like this from the tutorials

    output = [0] * len(lst)
    for item in lst:
        output[rank_array[len(item)]] = item
        rank_array[len(item)] += 1
    # output array is complete and sorted, based on length of each string
    return output


def str_rad_sort(lst: list, b: int) -> list:
    """
    Using the previous two functions, I can finally make a radix sort for list of strings
    :param lst: list of strings, non-empty and unsorted
    :param b: base, usually 27 as I have 27 characters including empty character
    :return: list, sorted alphabetically in ascending order
    :complexity: O(N+M) where N is the number of each strings in list and M is the length of the
    longest strong in that list.
    Since this uses the combination of sort_by_length() and str_counting_sort(), its total would be
    O(NM) + O(NM) -> O(2(NM)) -> O(NM),
    which can be reduced and considered as O(NM)
    """
    m = len(lst[0])  # m refers to maximum string length among all of the element
    for item in lst:
        if len(item) > m:
            m = len(item)  # found maximum m

    lst = sort_by_length(lst, m + 1)  # sort this list in terms of length

    for counter in range(1, m + 1):
        lst = str_counting_sort(lst, b, counter, m)
        # for 1-m, for each column perform radix sort
    return lst


def interest_groups(data: list) -> list:
    """
    And finally, a function we needed to satisfy Q3.
    It outputs a list of people, sorted, with identical interests
    :param data: list, where each element is a 2-element tuple representing a person.
    The first element in tuple is their name, which is a non-empty string of lowercase a-z with no spaces or
    punctuation. Every name in the list is unique.
    The second element in tuple is a non-empty list of non-empty strings, each represents the things this person
    likes.
    :return: a list of lists. For each distinct set of liked things, there is a list which contains
    all the names of the people who like exactly htose things. Within each list, names are sorted in ascending
    alphabetical order. However the lists may appear in any order in the big list.
    :complexity: O(NM) where N is the number of elements in data and M is the maximum numbers of characters among liked
    lists.

    complexity of str_rad_sort() is O(XY) where X is the number of strings in any list of liked things
    and Y is the length of the longest string in that list.
    Consider XY as O(M), as specification sheet mentions.
    Then, if I sum up time complexities it becomes:
    O(NM) + O(NM) + O(NK), where K is the number of maximum characters for list of names, which is specified that
    is small compared to M, and it reduces down to
    O(2(NM)) -> O(NM) where M is XY.
    """
    """
    My approach to this question, is to 
    1) Consider the second element for each tuple, and sort them alphabetically. This is to make sure that
    ("cat", "dog") are considered identical to ("dog", "cat").
    2) Then I concatenate strings together, and between each strings I added "+" sign, which can be character.
    This is to differentiate ("cat", "dog") with ("catdo", "g). I use string.join() to minimize complexity,
    and although extra time complexity is required by adding "+", this is constant and negligible.
    Since O(X(Y+1)) where X is the number of strings and  Y is the length of the longest string,
    can be reduced to O(XY + X), which leads to -> O(XY) -> O(M), as per input constraints.
    3) Make a new list to contain people with same interst
    4) Sort each list using str_rad_sort() again
    5) Finally, return that as a completion of this task
    """
    output = []
    for i in range(len(data)):
        data[i] = (data[i][0], "+".join(str_rad_sort(data[i][1], 27)))
    # tuples were immutable here, so I replaced it with a new tuple having concatenated strings
    # with "+" in between, sorted alphabetically
    # complexity for this bit is O(NM), as explained earlier

    while data:  # loop continues until all elements are popped and removed
        item = data.pop()
        if item is None:  # if the popped item is None(after it has been removed), then go on to next item
            continue
        tmp_list = [item[0]]  # a list containing the name of popped item
        for i in range(len(data)):  # then, a loop to compare string part with all other elmeents
            if data[i] is None:  # if it is already considered and was None, then ignore and go on
                continue
            if item[1] == data[i][1]:
                tmp_list.append(data[i][0])
                data[i] = None  # if duplicate interests are found, group them and replace it with None
                # I am doing this method, since using pop(i) or remove(i) would take O(n) due to the need to
                # re-format the index of the entire list in the worst case.
                # replaced with None would take O(1), so I used this implementation
        output.append(tmp_list)
    # the while loop here, this bit has complexity of O(NM)
    # a list of list of people are now made, there is a need to sort them, finally
    for i in range(len(output)):
        output[i] = str_rad_sort(output[i], 27)
    # lastly, this part has complexity of O(NK) where k is the length of maximum characters in name list,
    # and hence k is small.

    return output
    # it is complete!

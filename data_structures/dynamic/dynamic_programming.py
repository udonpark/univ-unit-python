def count_encounters(target_difficulty: int, monster_list: list) -> int:
    """
    This is Game Master, which computes number of different possible encounters which satisfy
    and adds up to a target difficulty.
    :param target_difficulty: a non-negative integer
    :param monster_list: a list of tuples, where each tuples represents a type of monster. The first value
    in each tuple is a string, which is the name of the type of monster, and the second value is a positive
    integer representing the difficulty of that particular type of monster.
    :return: it returns an integer, which is the number of different sets of monsters whose
    difficulties sum up to target_difficulty. Each type of monsters may be used more than once
    in an encounter.
    :complexity: O(NM), where N is the value of target_difficulty, and M is the length of monster_list
    """
    # For this Task, I have referred to Lecture Notes on Coin Change Problem.
    # After I have digested the concept and algorithm, wrote my codes from there.
    if target_difficulty == 0:  # I have hardcoded case to return 1 for this exceptional case
        return 1
    memo = [0] * (target_difficulty + 1)  # initialize memo array of 1 dimention
    memo[0] = 1
    for monster in monster_list:
        for i in range(target_difficulty + 1):
            if i >= monster[1]:  # go through from 0 to target_difficulty, and only if i is greater than that monster
                memo[i] += memo[i - monster[1]]  # then, update the memo array by using the previous memo
    return memo[-1]  # get the value for the desired target_difficulty


target_difficulty = 15
monster_list = [("bear", 5), ("imp", 2), ("kobold", 3), ("dragon", 10)]
print(count_encounters(target_difficulty, monster_list))


# Test as specified by the specs


def best_lamp_allocation(num_p: int, num_l: int, probs: list) -> float:
    """
    This is my implementation for Green House. This will calculate the probability that each plant will be
    ready on time, based on the number of lamps assigned to it.
    :param num_p: positive integer representing the number of plants
    :param num_l: positive integer representing the numebr of lamps
    :param probs: a list of lists, where probs[i][j] represents the probability that plant i will be ready
    in time if it is allocated j lamps. Values in this are floats between 0 and 1 inclusive.
    :return:  the highest probability of all plants being
    ready by the party that can be obtained by allocating lamps to plants optimally
    :complexity:
    O(NM^2) time complexity, where N is num_p and M is num_l.
    :space:
    space complexity is O(NM), where N is num_p and M is num_l
    """
    # For this task, I have referred to Knapsack Problem and Longest Common Subsequence to
    # get an idea for 2-D Array. I then designed myself algorithm for this specific problem.
    # Knapsack video for reference:
    # https://youtu.be/8LusJS5-AGo
    # Longest Common Subsequence video for reference:
    # https://www.youtube.com/watch?v=NnD96abizww

    memo = [[1] * (num_l + 1) for i in range(num_p)]  # initialized 2 dimention memo array
    for i in range(len(probs[0])):
        memo[0][i] = probs[0][i]  # set the first plant as default probabilities

    for i in range(1, num_p):
        for j in range(num_l + 1):  # iterate through each plant, and each lump case
            if j >= len(probs[0]):  # if lump is excess
                memo[i][j] = memo[i - 1][j] * probs[i][0]  # set it as previous plant, multiplied by 0lump probability
            else:  # this is the usual case
                # I preferred not to use max(a, b) to visualize complexity better
                a = memo[i - 1][j] * probs[i][0]  # case 1: use 0 lumps for this plant
                b = memo[i - 1][num_l - j] * probs[i][j]  # case 2: use j lumps for this plant, and referred to preivous
                # memo for probability using the remaining lumps left
                if a > b:
                    memo[i][j] = a
                else:  # this block is just for memo[i][j] = max(a, b)
                    memo[i][j] = b

    maxp = 0
    for item in memo[-1]:
        if maxp < item:
            maxp = item  # again, this is also just to find the maximum probability from the last row
    return maxp  # maxp is the output that we want


probs = [[0.5, 0.5, 1], [0.25, 0.1, 0.75]]
print(best_lamp_allocation(2, 2, probs))

probs = [[0.5, 0.75, 0.25], [0.75, 0.25, 0.8]]
print(best_lamp_allocation(2, 2, probs))

#  Tests as shown by the specs sheet.

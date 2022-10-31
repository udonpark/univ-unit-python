"""
In this assignment we create a Python module
to perform some basic data science tasks. While the
instructions contain some mathematics, the main focus is on 
implementing the corresponding algorithms and finding 
a good decomposition into subproblems and functions 
that solve these subproblems. 

To help you to visually check and understand your
implementation, a module for plotting data and linear
prediction functions is provided.

The main idea of linear regression is to use data to
infer a prediction function that 'explains' a target variable 
of interest through linear effects of one 
or more explanatory variables. 

Part I - Univariate Regression

Task A: Optimal Slope

-> example: price of an apartment

Let's start out simple by writing a function that finds
an "optimal" slope (a) of a linear prediction function 
y = ax, i.e., a line through the origin. A central concept
to solve this problem is the residual vector defined as

(y[1]-a*x[1], ..., y[m]-a*x[m]),

i.e., the m-component vector that contains for each data point
the difference of the target variable and the corresponding
predicted value.

With some math (that is outside the scope of this unit) we can show
that for the slope that minimises the sum of squared the residual

x[1]*(y[1]-a*x[1]) + ... + x[m]*(y[m]-a*x[m]) = 0

Equivalently, this means that

a = (x[1]*y[1]+ ... + x[m]*y[m])/(x[1]*x[1]+ ... + x[m]*x[m])

Write a function slope(x, y) that, given as input
two lists of numbers (x and y) of equal length, computes
as output the lest squares slope (a).

Task B: Optimal Slope and Intercept

To get a better fit, we have to consider the intercept b as well, 
i.e., consider the model f(x) = ax +b. 
To find the slope of that new linear model, we \centre the explanatory variable 
by subtracting the mean from each data point. 
The correct slope of the linear regression f(x)=ax + b is the same 
slope as the linear model without intercept, f(x)=ax, calculated on the 
centred explanatory variables instead of the original ones. 
If we have calculated the correct slope a, we can calculate the intercept as
b = mean(y) - a*mean(x).

Write a function line(x,y) that, given as input
two lists of numbers (x and y) of equal length, computes
as output the lest squares slope a and intercept b and
returns them as a tuple a,b.


Task C: Choosing the Best Single Predictor

We are now able to determine a regression model that represents 
the linear relationship between a target variable and a single explanatory variable.
However, in usual settings like the one given in the introduction, 
we observe not one but many explanatory variables (e.g., in the example `GDP', `Schooling', etc.). 
As an abstract description of such a setting we consider n variables 
such that for each j with 0 < j < n we have measured m observations 

$x[1][j], ... , x[m][j]$. 


These conceptually correspond to the columns of a given data table. 
The individual rows of our data table then become n-dimensional 
data points represented not a single number but a vector.

A general, i.e., multi-dimensional, linear predictor is then given by an n-dimensional 
weight vector a and an intercept b that together describe the target variable as








y = dot(a, x) + b





i.e., we generalise y = ax + b by turning the slope a into an n-component linear weight vector
and replace simple multiplication by the dot product (the intercept b is still a single number).
Part 2 of the assignment will be about finding such general linear predictors. 
In this task, however, we will start out simply by finding the best univariate predictor 
and then represent it using a multivariate weight-vector $a$. %smooth out with the text that follows.

Thus, we need to answer two questions: (i) how do we find the best univariate predictor, 
and (ii) how to we represent it as a multivariate weight-vector. 

Let us start with finding the best univariate predictor. For that, we test all possible
predictors and use the one with the lowest sum of squared residuals.
Assume we have found the slope a^j and intercept b^j of the best univariate predictor---and assume it 
uses the explanatory variable x^j---then we want to represent this as a multivariate 
slope a and intercept b. That is, we need to find a multivariate slop a such that dot(a, x) + b 
is equivalent to a^jx^j + b^j. Hint: The intercept remains the same, i.e., $b = b^j$.

Task D: Regression Analysis

You have now developed the tools to carry out a regression analysis. 
In this task, you will perform a regression analysis on the life-expectancy 
dataset an excerpt of which was used as an example in the overview. 
The dataset provided in the file /data/life_expectancy.csv.


Part 2 - Multivariate Regression

In part 1 we have developed a method to find a univariate linear regression model 
(i.e., one that models the relationship between a single explanatory variable and the target variable), 
as well as a method that picks the best univariate regression model when multiple 
explanatory variables are available. In this part, we develop a multivariate regression method 
that models the joint linear relationship between all explanatory variables and the target variable. 


Task A: Greedy Residual Fitting

We start using a greedy approach to multivariate regression. Assume a dataset with m data points 
x[1], ... , x[m] 
where each data point x[i] has n explanatory variables x[i][1], ... , x[i][m], 
and corresponding target variables y[1], ... ,y[m]. The goal is to find the slopes for 
all explanatory variables that help predicting the target variable. The strategy we 
use greedily picks the best predictor and adds its slope to the list of used predictors. 
When all slopes are computed, it finds the best intercept. 
For that, recall that a greedy algorithm iteratively extends a partial solution by a 
small augmentation that optimises some selection criterion. In our setting, those augmentation 
options are the inclusion of a currently unused explanatory variable (i.e., one that currently 
still has a zero coefficient). As selection criterion, it makes sense to look at how much a 
previously unused explanatory variable can improve the data fit of the current predictor. 
For that, it should be useful to look at the current residual vector r,
because it specifies the part of the target variable that is still not well explained. 
Note that a the slope of a predictor that predicts this residual well is a good option for 
augmenting the current solution. Also, recall that an augmentation is used only if it 
improves the selection criterion. In this case, a reasonable selection criterion is 
again the sum of squared residuals.

What is left to do is compute the intercept for the multivariate predictor. 
This can be done  as


b = ((y[1]-dot(a, x[1])) + ... + (y[m]-dot(a, x[m]))) / m

The resulting multivariate predictor can then be written as 

y = dot(a,x) + b .



Task B: Optimal Least Squares Regression

Recall that the central idea for finding the slope of the optimal univariate regression line (with intercept) 
that the residual vector has to be orthogonal to the values of the centred explanatory variable. 
For multivariate regression we have many variables, and it is not surprising that for an optimal 
linear predictor dot(a, x) + b, it holds that the residual vector is orthogonal to each of the 
centred explanatory variables (otherwise we could change the predictor vector a bit to increase the fit). 
That is, instead of a single linear equation, we now end up with n equations, one for each data column.
For the weight vector a that satisfies these equations for all i=1, ... ,n, you can again simply find the 
matching intercept b as the mean residual when using just the weights a for fitting:

b = ((y[1] - dot(a, x[1])) + ... + (y[m] - dot(a, x[m])))/m .

In summary, we know that we can simply transform the problem of finding the least squares predictor to solving a system of linear equation, which we can solve by Gaussian Elimination as covered in the lecture. An illustration of such a least squares predictor is given in Figure~\ref{fig:ex3dPlotWithGreedyAndLSR}.
"""








"""
32134541
Yo Kogure
MAT1045

"""

from math import inf, sqrt




def slope(x, y):
    xdotx = []
    xdoty = []
    sumofxx = 0
    sumofxy = 0
    for elements in range(len(x)):
        xdotx.append(x[elements]*x[elements])
        xdoty.append(x[elements]*y[elements])
    for times in range(len(x)):
        sumofxx += xdotx[times]
        sumofxy += xdoty[times]
    a = sumofxy / sumofxx
    return a

    """
This is a slope function that returns the optimal slope for the simple regresssion.
Input: x are y are both a list of equal length, showing data of an explanatory and a target variable.
Output: This function outputs the optimal least squares slope, value of "a" from the data provided.
One of the challenges that this question has, is that there has to be multiple steps to slowly build up toward the output. I have decided to break it into parts using decomposition.
xdotx and xdoty are an empty list to which respective data would be put. In fact, I don't need to use the list and simply add the values using the for loop. However, I have decided to temporary store values in
the list and then sum up later, because later I might need to use the data in the following questions. We can adjust the code little bit to extract the variable used inside the function. For example, add " return xdoty + xdotx" instead of the return a.
I used 2 for loops, but it can be one if I dont use the list method. I one by one calculate the data stored in the list by append method, and then for each time (index of a list), I repeat.
Breaking into step by step it makes it easier to spot mistakes later on.



    """
        
        
        
    
    
    


    
    """
    Computes the slope of the least squares regression line
    (without intercept) for explaining y through x.

    For example:
    >>> slope([0, 1, 2], [0, 2, 4])
    2.0
    >>> slope([0, 2, 4], [0, 1, 2])
    0.5
    >>> slope([0, 1, 2], [1, 1, 2])
    1.0
    >>> slope([0, 1, 2], [1, 1.2, 2])
    1.04
    """
    pass




def line(x, y):
    sumofx = 0
    xbar = []
    xbardotxbar = 0
    xbardoty = 0
    for elements in range(len(x)):
        sumofx += x[elements]
    miu = sumofx / len(x)
    
    for elements in range(len(x)):
        xbar.append(x[elements]-miu)
    for elements in range(len(x)):
        xbardotxbar += xbar[elements]**2
        xbardoty += xbar[elements]*y[elements]
    optimal_a = xbardotxbar / xbardoty
    sum_for_b = 0
    for i in range(len(x)):
        sum_for_b += (y[i]-(optimal_a * x[i]))
    optimal_b = sum_for_b / len(x)

    return (optimal_a, optimal_b)



"""
this function, unlike previous one, takes into account that the line might not pass through origin, so it allows a new variable b to come in as a y-intercept of the perfect line.
line(x, y) returns the optimal slope and the intercept for the regression model.

Input: Two lists of numbers, x and y of equal length representing data of an explanatory and a target variable.
Output: A tuple (a,b) where a is the optimal least squares slope and b the optimal intercept with respect to
the given data.

there are many variables for this one. One of the challenges it has is the process is extremely complicated.
To solve this I broke into many small steps to tackle one by one.
It was very hard to find out the value of optimal_b, as many imagination had to be done in head.

prepare many variables, and then first sum of all values of x to find out the average, miu for x.
We use this miu value often, it was a good idea to take our time to secure this value early in the code.
I like to use append command to add elements to a list, that way we can take out the data anytime.
As a technique, in the third for loop, I have inserted both calculations for xbardotxbar and xbardoty. The naming of variable can be anything but I like to name it this way to viasualize what the value
shows. I use the character 'elements' as a count in for loop, but in the fourth one I use i. I differentiate when I use the loop for the list and for calculation such as summing up values.



I have conducted multiple tests which proven for this function to work.
the value of b might often be cotinuous, we can use round function embbed into the import math, and easily manipulate with the values.  We have now prepared 2 working functions, both returning exact values after
computing difficult solutions.

"""
        
    
    
    """
    Computes the least squares regression line (slope and intercept)
    for explaining y through x.

    For example:
    >>> a, b = line([0, 1, 2], [1, 1, 2])
    >>> round(a,1)
    0.5
    >>> round(b,2)
    0.83
    """
    pass






def best_single_predictor(data, y):
    n = len(data)
    m = len(data[0])
    min_a = 0
    memory = 0
    for i in range(n):
        temporary_a, temporary_b = line(data[m], y[n])
        if min_a > temporary_a:
            min_a = temporary_a
            memory = i    
        b = y[memory]   
    return a, b
    
    

    


    

    
    

    

"""
this function computes the best linear predictor by picking the best prediction models for all values of possible explanatory variables.
this function has many problems to overcome. I have decomposed it into few parts.
I will list the pseudocodes as an overall guide before starting coding to know which steps I need to take.
first, secure the value of m and n, they are playing important role in this task. this is easily foundable by using the property of multidimensional lists in python.
n is the number of rows. m shows number of coloums which can be found out by couting the length of the data[0], first row of the dataset.
We are using a function inside the function in this case.

we dont use the outputs b from line really so we store it in temporary_b and let go.
using line function from the previous task and assigning outputs of the line function as temporary_a and temporary_b, we can manipulate datas obtained for each m.
in the same for loop, right after updatin the temp_a and temp_b, we go on to the task of obtaining the minimum value of a. use if loops to check if the value is minimum, and memory variable,
remembers when the data was updated. If a was found minimum for m=3, it remembers 3 and so we can find out the respective value of b as well later on.
Make sure to repeat the for loop for n times, as n indiates the number of rows, the dimension of the huge multidimensional list.


Overall in this assignment there was multiple opportunities to make an empty list which I found interesting. assigning values outside the for loop is important
because if not declared earlier, it might update itself over and over for each time the program goes through the loop.





"""
    
    """
Input: Table data with m > 0 rows and n > 0 columns representing data of n explanatory variables and a list
y of length m containing the values of the target variable corresponding to the rows in the table.
Output: A pair (a, b) of a list a of length n and a number b representing a linear predictor with weights a
and intercept b with the following properties:
a) There is only one non-zero element of a, i.e., there is one i in range(n) such that a[j]==0 for all
indices j!=i.
b) The predictor represented by (a, b) has the smallest possible squared error among all predictors
that satisfy property a).

    """



    
    """
    >>> data = [[1, 0],
    ...         [2, 3],
    ...         [4, 2]]
    >>> y = [2, 1, 2]
    >>> weights, b = best_single_predictor(data, y)
    >>> weights[0]
    0.0
    >>> round(weights[1],2)
    -0.29
    >>> round(b,2)
    2.14
    """
    pass


def greedy_predictor(data, y):
    """
    This implements a greedy correlation pursuit algorithm.

    >>> data = [[1, 0],
    ...         [2, 3],
    ...         [4, 2]]
    >>> y = [2, 1, 2]
    >>> weights, intercept = greedy_predictor(data, y)
    >>> round(weights[0],2)
    0.21
    >>> round(weights[1],2)
    -0.29
    >>> round(intercept, 2)
    1.64
    
    >>> data = [[0, 0],
    ...         [1, 0],
    ...         [0, -1]]
    >>> y = [1, 0, 0]
    >>> weights, intercept = greedy_predictor(data, y)
    >>> round(weights[0],2)
    -0.5
    >>> round(weights[1],2)
    0.75
    >>> round(intercept, 2)
    0.75
    """
    pass




def equation(i, data, y):
    """
    Finds the row representation of the i-th least squares condition,
    i.e., the equation representing the orthogonality of
    the residual on data column i:

    (x_i)'(y-Xb) = 0
    (x_i)'Xb = (x_i)'y

    x_(1,i)*[x_11, x_12,..., x_1n] + ... + x_(m,i)*[x_m1, x_m2,..., x_mn] = <x_i , y>

    For example:
    >>> data = [[1, 0],
    ...         [2, 3],
    ...         [4, 2]]
    >>> y = [2, 1, 2]
    >>> coeffs, rhs = equation(0, data, y)
    >>> round(coeffs[0],2)
    4.67
    >>> round(coeffs[1],2)
    2.33
    >>> round(rhs,2)
    0.33
    >>> coeffs, rhs = equation(1, data, y)
    >>> round(coeffs[0],2)
    2.33
    >>> round(coeffs[1],2)
    4.67
    >>> round(rhs,2)
    -1.33
    """
    pass

def least_squares_predictor(data, y):
    """
    Finding the least squares solution by:
    - centering the variables (still missing)
    - setting up a system of linear equations
    - solving with elimination from the lecture

    For example:
    >>> data = [[0, 0],
    ...         [1, 0],
    ...         [0, -1]]
    >>> y = [1, 0, 0]
    >>> weights, intercept = least_squares_predictor(data, y)
    >>> round(weights[0],2)
    -1.0
    >>> round(weights[1],2)
    1.0
    >>> round(intercept, 2)
    1.0
    
    >>> data = [[1, 0],
    ...         [2, 3],
    ...         [4, 2]]
    >>> y = [2, 1, 2]
    >>> weights, intercept = least_squares_predictor(data, y)
    >>> round(weights[0],2)
    0.29
    >>> round(weights[1],2)
    -0.43
    >>> round(intercept, 2)
    1.71
    """
    pass


def regression_analysis():        
    """
    The regression analysis can be performed in this function or in any other form you see
    fit. The results of the analysis can be provided in this documentation. If you choose
    to perform the analysis within this funciton, the function could be implemented 
    in the following way.
    
    The function reads a data provided in "life_expectancy.csv" and finds the 
    best single predictor on this dataset.
    It than computes the predicted life expectancy of Rwanda using this predictor, 
    and the life expectancy of Liberia, if Liberia would improve its schooling 
    to the level of Austria.
    The function returns these two predicted life expectancies.
    
    For example:
    >>> predRwanda, predLiberia = regression_analysis()
    >>> round(predRwanda)
    65
    >>> round(predLiberia)
    79
    """
    pass
    
if __name__=='__main__':
    import doctest
    doctest.testmod()

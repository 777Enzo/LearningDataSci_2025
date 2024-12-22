# this is me practicing basic syntax - for numpy, sci-py, and pandas.
#     i will practice applying different built in methods



# notes


# -------------------------------------------------
    #numpy --

        # Demonstrate np.linspace, np.arange, and np.random for creating arrays.
        # Showcase array broadcasting with operations of different shapes.
        # Use more aggregation functions like np.min, np.max, and np.percentile.

# -------------------------------------------------
# -------------------------------------------------
    #SciPy --

        # Include examples of using common modules like scipy.stats (e.g., calculating mode, kurtosis, skewness).
        # Demonstrate solving equations or optimization problems using scipy.optimize.
        # Include integration (scipy.integrate) or interpolation (scipy.interpolate).

# -------------------------------------------------
# -------------------------------------------------
    #Pandas  --

        # Create, read, and manipulate DataFrames using pd.DataFrame and CSV/Excel reading functions.
        # Practice operations like filtering, grouping, and pivoting.
        # Perform statistical summaries (df.describe()), missing data handling, and type conversions.

# -------------------------------------------------
# -------------------------------------------------
    #Visualization  --

        #Introduce visualization using matplotlib.pyplot or seaborn to plot results, which is vital for data science.

# -------------------------------------------------


# Function Segregation: Split different sections into specific functions (e.g., array_operations, array_statistics, basic_stats, etc.) to improve reusability.



#TESTING VERSION CONTROL & GIT!!!!


import math
import numpy as np
import pandas as pd
import scipy as sc


def numpy():
    #-------------------------------------------------------------------------------------------------
    # section 1.0
    # declaring arrays using "np.array()" and printing out number of dim (ndims)
    #-------------------------------------------------------------------------------------------------
    # declaring arrays using "np.array() - method via from np; with [list(s)] as parameter
    print("-----------------------------------------")
    print("Declaring arrays in numpy w/ diff ndims \n Printing array \n Printing ndims in array")
    print("-----------------------------------------")
    arr1dim = np.array([1, 2, 3]) #one dim
    arr2dim = np.array([[1, 2, 3], [4, 5, 6]]) #two dim
    arr3dim = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]]) #threedim

    print("1 dim: ")
    print(arr1dim)
    # ndim returns the number of dimensions
    print("\tNdim: " + str(arr1dim.ndim) + "\n")

    print("2 dim: ")
    print(arr2dim)
    print("\tNdim: " + str(arr2dim.ndim) + "\n")

    print("3 dim: ")
    print(arr3dim)
    print("\tNdim: " + str(arr3dim.ndim) + "\n\n\n")

    #-------------------------------------------------------------
    # section 1.1
    # accessing array elements by using 0 based indexing
    #-------------------------------------------------------------
    print("-----------------------------------------")
    print("Accessing array elements")
    print("-----------------------------------------")


    print("Arr1Dim: ")
    print("\tFirst element [0]: " + str(arr1dim[0]))
    # if [0] is the very FIRST element in the array, [-1] is the very LAST element
    print("\tLast element [-1]: " + str(arr1dim[-1])) #accessing LAST array by negative indexing



    # ----------------------------------------------------------
    # [rows, col] - using the colon, to select an entire row or column

    # to select an entire *row* select all the columns
    # to select an entire *column* select all the rows
    # ----------------------------------------------------------
    print("\n")
    print("Arr2Dim: ")
    print("\t2nd element, 2nd row: " + str(arr2dim[1, 1]))
    # for the 2nd column, we use the : to select all rows,
    # and then we indicate which colum index
    print("\t2nd column: " + str(arr2dim[:, 1]))
    #vice versa for 2nd row
    print("\t2nd row: " + str(arr2dim[1, :])) #select 2nd row, and colon indicates all the column in that row




    print("\n")
    print("Arr3Dim: " + "\n")
    print(arr3dim)
    print("\n")

    #first printing out shape
    print(str(arr3dim.shape) + ": 2 rows/groups of arrays. Each row, has 2 arrays inside of it, each array has 3 elements")
    # Rows/groups of arrays, number of arrays in each row/group, number of elements in each array

    print("\n\t1st group/row of arrays[0], 2nd array[1], 3rd element[2]: " + str(arr3dim[0, 1, 2]))
    print("\n\t2nd group/row of arrays[1], 1st array[0], 1st element[0]: " + str(arr3dim[1, 0, 0]))

    # ----------------------------------------------------------
    # [array (group),rows, col] - using the colon, to select an entire row or column

    # to select an entire *row* select all the columns
    # to select an entire *column* select all the rows
    # ----------------------------------------------------------    print("\n---------------------")
    print("Rows & columns")
    print("---------------------")
    #columns
    print("\t1st group/row of arrays[0], All rows[:], 2nd column: " + str(arr3dim[0, :, 1])) #0 = first array group,select all rows, 2nd col[:, 1] = every value in 2nd col

    #rows
    print("\n\t2nd group/row of arrays[1], entire 1st row[0], All columns[:]: " + str(arr3dim[1, 0, :]))#1 = second array group, select first row, all cols[0,:] = every value in row



    #-------------------------------------------------------------
    # section 1.2
    # peforming math operations on arrays
    #-------------------------------------------------------------
    print("\n---------------------------------")
    print("Peforming math operations")
    print("---------------------------------" + "\n")
    print("Arr1Dim: " + str(arr1dim))
    print("\tArr1Dim * 2: " + str(arr1dim*2))
    print("\tArr1Dim + 10: " + str(arr1dim + 10))


    #-------------------------------------------------------------
    # summing along diff axis (0, 1)
    # axis=0: Sum along the rows (collapses across the rows, resulting in one sum per column).
    # axis=1: Sum along the columns (collapses across the columns, resulting in one sum per row).
    #-------------------------------------------------------------


    print("\n\nArr3Dim: " + str(arr3dim) + "\n\n")


    print("Arr3Dim - total sum of all elements in arrays: " + str(arr3dim.sum()))



    print("Arr3Dim - sum by column: " + str(arr3dim.sum(1)) + "\nPt.2: - sum of sum of columns " + str(arr3dim.sum(1).sum(0)))


    #-------------------------------------------------------------
    # section 1.3
    # statistics
    #-------------------------------------------------------------

    print("------------------------")
    print("Stats")
    print("----------------------------" + "\n\n")

    # arr1dim - stats
    print("Arr1Dim: " + str(arr1dim))
    arr1dim_mean = arr1dim.mean()
    # Mean (avg) = Sum of all elements / # of elements
    print("Mean - (avg): " + str(arr1dim_mean) + "\n\n")

    intMiddleIndex = len(arr1dim) // 2 #taking length of array and int dividing by 2, // (int div) rounds DOWN
    arr1dim_median = np.sort(arr1dim)[intMiddleIndex]
    print("Median (manually): " + str(arr1dim_median))

    arr1dim_median_b = np.median(arr1dim)
    print("Median (np method): " + str(arr1dim_median_b))



    # print("Mode: - Sci PY")


    #-------------------------------------------------------------
    # STD = Standard deviation
    # Statistical measure that quantifies the amount of variation or dispersion in a set of data points...
    # Tells you how spread out the values in your data set are around the mean (average).

    # ----Low---- standard deviation means the data points are CLOSE to the mean, indicating less variability.
    # ----High---- standard deviation means the data points are SPREAD out over a wider range, indicating more variability.
    #-------------------------------------------------------------

    arr1dim_std = arr1dim.std()
    print("STD: " + str(arr1dim_std) + "\n\n")


    # arr2dim - stats
    print("Arr2Dim: " + str(arr2dim))


    # mean flattens the 2dim array into one dim. sums all elements and divides by len (# of elements)
    arr2dim_mean = arr2dim.mean()
    print(f"Arr2Dim mean: {arr2dim_mean}")

    print("Length of Arr2Dim: " + str(len(arr2dim))) # max index of 1 + 1 ( element = index + 1 )




    #-------------------------------------------------------------
    # Array copies and views

    # Copy - A copy is a new array with its own independent data.
    # Changes in the original array **DO NOT** affect the copy, and vice versa.

    # View - A new array object that SHARES the same data as the original array.
    # Changes made to the view **DO** affect the original array and vice versa.

    #-------------------------------------------------------------


    # ------ COPIES -------- #
    print(f"Arr2Dim: {arr2dim}")

    arr2dim_copy = arr2dim.copy()
    print(f"\n\n Arr2Dim copy: {arr2dim_copy}")

    # Modifying the copy of the array - changing the first array, first elment to 99
    arr2dim_copy[0][0] = 99
    print(f"\n Arr2Dim copy modified: {arr2dim_copy}")
    print(f"\n Arr2Dim ORIGINAL: {arr2dim}")
    #The orginal array stays the same, because the copy was modified

    # copying and "flattening" array - reducing ndim's to 1
    arr2dim_copy_flattened = arr2dim_copy.flatten()
    print("\nPrinting Arr2Dim copy flattened " + str(arr2dim_copy_flattened))



    # ------ VIEWS -------- #
    arr2dim_view = arr2dim.view()
    print(f"\n\nArr2dim view {arr2dim_view}")
    # Modifying the view of the array - changing the entire first array, to 99
    arr2dim_view[0] = 99
    #Now printing the orginal array, which is connected to the view
    print(f"\n\nArr2dim orginal {arr2dim}")
    print(f"The orginal array is modified because it is synced to the view - (unlike the copy of the array)\n")


    #reverting modification, back to orginal array

    original_values = [1, 2, 3]
    for i in range(len(arr2dim_view[0])):        # looping through the range of the len of first row

        arr2dim_view[0][i] = original_values[i]     #Assigning values to the first rowt row at index [0][]


    #-------------------------------------------------------------
    #Reshaping arrays
    #-------------------------------------------------------------


    print("\nOriginal Arr2Dim: " + str(arr2dim))


    #for reshape() method the paramaters are (rows, columns) must have same # of elements as orginal array
    arr2dim_reshape = arr2dim.reshape(1, 6) #flattening - one row, 6 elements
    print("\nFlattening(reshaping) Arr2Dim - reshape(): " + str(arr2dim_reshape))


    #for flattening arrays using the flatten() method is easier, automatically turns ndims = to 1
    arr2dim_flatten = arr2dim.flatten()
    print("\nFlattening(reshaping) Arr2Dim - flatten(): " + str(arr2dim_flatten))








numpy()

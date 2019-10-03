#!/bin/python3

import math
import os
import random
import re
import sys


def diagonalDifference(arr):
    l_to_r = 0
    r_to_l = 0
    for i in range(len(arr)):
        l_to_r += arr[i][i]
        r_to_l += arr[i][len(arr)-i-1]
    result = abs(l_to_r-r_to_l)

    return result
arr = [[-11, 2, 4], [4, 5, 6], [10, 8, -12]]
result = diagonalDifference(arr)

print(result)
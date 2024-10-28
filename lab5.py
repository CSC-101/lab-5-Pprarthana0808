import data
from data import Time, Point
from typing import Optional, List
import math

# Write your functions for each part in the space below.

# Part 1
   # The function for Part 1 should be within the class in data.py.


# Part 2
   # The function for Part 2 should be within the class in data.py.


# Part 3
def time_add(time1: Time, time2: Time) -> Time:
    total_seconds = time1.second + time2.second
    extra_minutes, new_seconds = divmod(total_seconds, 60)
    total_minutes = time1.minute + time2.minute + extra_minutes
    extra_hours, new_minutes = divmod(total_minutes, 60)
    total_hours = time1.hour + time2.hour + extra_hours
    return Time(total_hours, new_minutes, new_seconds)

# Part 4
def is_descending(lst: list[float]) -> bool:
    return all(lst[i] > lst[i+1] for i in range(len(lst)-1))


# Part 5
def largest_between(lst: List[int], lower: int, upper: int) -> [int]:
    if lower > upper:
        return None
    lower = max(0, lower)
    upper = min(len(lst) - 1, upper)
    if lower <= upper:
        max_index = lower
        for i in range(lower, upper + 1):
            if lst[i] > lst[max_index]:
                max_index = i
        return max_index
    return None

# Part 6
def furthest_from_origin(points: List[Point]) -> [int]:
    if not points:
        return None
    max_index = 0
    max_distance =0
    for i, point in enumerate(points):
        distance = math.sqrt(point.x ** 2 + point.y ** 2)
        if distance > max_distance:
            max_distance = distance
            max_index = i
    return max_index

"""
Unpack the following tuple into 4 variables:

("John Smith", 11743, ("Computer Science", "Mathematics"))

The data represents a student's name, their student id number, and their major and minor disciplines in that order.
"""

name, number, mt1 = ("John Smith", 11743, ("Computer Science", "Mathematics"))

print(name, number, mt1[0], mt1[1])
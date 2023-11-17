# -*- coding:utf-8 -*-

"""
177. Nth Highest Salary

Table: Employee

+-------------+------+
| Column Name | Type |
+-------------+------+
| id          | int  |
| salary      | int  |
+-------------+------+
id is the primary key (column with unique values) for this table.
Each row of this table contains information about the salary of an employee.
 

Write a solution to find the nth highest salary from the Employee table. If there is no nth highest salary, return null.

The result format is in the following example.

 

Example 1:

Input: 
Employee table:
+----+--------+
| id | salary |
+----+--------+
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
+----+--------+
n = 2
Output: 
+------------------------+
| getNthHighestSalary(2) |
+------------------------+
| 200                    |
+------------------------+
Example 2:

Input: 
Employee table:
+----+--------+
| id | salary |
+----+--------+
| 1  | 100    |
+----+--------+
n = 2
Output: 
+------------------------+
| getNthHighestSalary(2) |
+------------------------+
| null                   |
+------------------------+
"""


import pandas as pd
import numpy as np


def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    employee = employee.drop_duplicates(subset="salary").sort_values("salary", ascending=False)
    ser_salary = employee["salary"]
    if len(ser_salary) >= N:
        return pd.DataFrame({f"getNthHighestSalary({N})":[ser_salary.iloc[N-1]]})
    else:
        return pd.DataFrame({f"getNthHighestSalary({N})":[np.nan]})


print(nth_highest_salary(
    pd.DataFrame({
        "id": [1, 2],
        "salary": [100, 200],
    }),2
))

# -*- coding: utf-8 -*-

"""
176. Second Highest Salary

Table: Employee

+-------------+------+
| Column Name | Type |
+-------------+------+
| id          | int  |
| salary      | int  |
+-------------+------+
id is the primary key (column with unique values) for this table.
Each row of this table contains information about the salary of an employee.
 

Write a solution to find the second highest salary from the Employee table. If there is no second highest salary, return null (return None in Pandas).

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
Output: 
+---------------------+
| SecondHighestSalary |
+---------------------+
| 200                 |
+---------------------+
Example 2:

Input: 
Employee table:
+----+--------+
| id | salary |
+----+--------+
| 1  | 100    |
+----+--------+
Output: 
+---------------------+
| SecondHighestSalary |
+---------------------+
| null                |
+---------------------+
"""

import pandas as pd
import numpy as np

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    employee = employee.drop_duplicates(subset="salary").sort_values("salary", ascending=False)
    ser_salary = employee["salary"]
    if len(ser_salary) >= 2:
        return pd.DataFrame({"SecondHighestSalary":[ser_salary.iloc[1]]})
    else:
        return pd.DataFrame({"SecondHighestSalary":[np.nan]})


print(second_highest_salary(
    pd.DataFrame({
        "id": [1, 2],
        "salary": [100, 200],
    })
))
# Students and Examinations

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-students-and-examinations` |
| Topics | Database |
| Solved | 2026-05-02 |
| Runtime | 1105 ms (beats 22.79279999999992%) |
| Memory | 0B (beats 100%) |

## Problem Statement

Table: `Students`

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| student_id    | int     |
| student_name  | varchar |
+---------------+---------+
student_id is the primary key (column with unique values) for this table.
Each row of this table contains the ID and the name of one student in the school.

 

Table: `Subjects`

+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| subject_name | varchar |
+--------------+---------+
subject_name is the primary key (column with unique values) for this table.
Each row of this table contains the name of one subject in the school.

 

Table: `Examinations`

+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| student_id   | int     |
| subject_name | varchar |
+--------------+---------+
There is no primary key (column with unique values) for this table. It may contain duplicates.
Each student from the Students table takes every course from the Subjects table.
Each row of this table indicates that a student with ID student_id attended the exam of subject_name.

 

Write a solution to find the number of times each student attended each exam.

Return the result table ordered by `student_id` and `subject_name`.

The result format is in the following example.

 

**Example 1:**

**Input:** 
Students table:
+------------+--------------+
| student_id | student_name |
+------------+--------------+
| 1          | Alice        |
| 2          | Bob          |
| 13         | John         |
| 6          | Alex         |
+------------+--------------+
Subjects table:
+--------------+
| subject_name |
+--------------+
| Math         |
| Physics      |
| Programming  |
+--------------+
Examinations table:
+------------+--------------+
| student_id | subject_name |
+------------+--------------+
| 1          | Math         |
| 1          | Physics      |
| 1          | Programming  |
| 2          | Programming  |
| 1          | Physics      |
| 1          | Math         |
| 13         | Math         |
| 13         | Programming  |
| 13         | Physics      |
| 2          | Math         |
| 1          | Math         |
+------------+--------------+
**Output:** 
+------------+--------------+--------------+----------------+
| student_id | student_name | subject_name | attended_exams |
+------------+--------------+--------------+----------------+
| 1          | Alice        | Math         | 3              |
| 1          | Alice        | Physics      | 2              |
| 1          | Alice        | Programming  | 1              |
| 2          | Bob          | Math         | 1              |
| 2          | Bob          | Physics      | 0              |
| 2          | Bob          | Programming  | 1              |
| 6          | Alex         | Math         | 0              |
| 6          | Alex         | Physics      | 0              |
| 6          | Alex         | Programming  | 0              |
| 13         | John         | Math         | 1              |
| 13         | John         | Physics      | 1              |
| 13         | John         | Programming  | 1              |
+------------+--------------+--------------+----------------+
**Explanation:** 
The result table should contain all students and all subjects.
Alice attended the Math exam 3 times, the Physics exam 2 times, and the Programming exam 1 time.
Bob attended the Math exam 1 time, the Programming exam 1 time, and did not attend the Physics exam.
Alex did not attend any exams.
John attended the Math exam 1 time, the Physics exam 1 time, and the Programming exam 1 time.

## Solutions

```MySQL
# Write your MySQL query statement below
SELECT
    S.student_id
    ,S.student_name
    ,SU.subject_name
    ,COUNT(E.student_id) attended_exams
FROM Students S
CROSS JOIN Subjects SU
LEFT JOIN Examinations E
    ON S.student_id = E.student_id
                        AND SU.subject_name = E.subject_name

                        GROUP BY S.student_id, S.student_name, SU.subject_name
                        ORDER BY S.student_id, S.student_name, SU.subject_name
                        ;
```

## AI Review

1. **Complexity**:
   * **Time**: $O(S \times U + E \log E)$, where $S$ is the number of students, $U$ is subjects, and $E$ is examinations. The Cartesian product creates $S \times U$ rows; the join and sorting dominate the time.
   * **Space**: $O(S \times U)$ to store the intermediate result set and final output.

2. **Correctness**:
   * The solution is **correct**. It properly uses a `CROSS JOIN` to ensure every student-subject combination exists, even those with zero attendance.
   * `COUNT(E.student_id)` is crucial here; it correctly returns `0` for `NULL` matches from the `LEFT JOIN`.
   * **Edge cases**: Handles students with no exams and subjects with no participants correctly.

3. **Optimization**:
   * **Indexing**: Ensure a composite index exists on `Examinations(student_id, subject_name)`. This transforms the `LEFT JOIN` into a highly efficient index seek rather than a full table scan.
   * **Group By**: If `student_id` is the primary key, grouping by `S.student_name` is technically redundant for logic but necessary for certain SQL modes (`ONLY_FULL_GROUP_BY`).

4. **Key Algorithmic Pattern**:
   * **Cartesian Product + Left Join**: Generating a complete set of possibilities (all students $\times$ all subjects) and then mapping sparse activity data onto that set.

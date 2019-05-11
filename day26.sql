/*
Two tables: professor, department. 

DEPARTMENT(ID SERIAL PRIMARY KEY (FOREIGN KEY IN PROFESSOR), NAME VARCHAR(30) NOT NULL);
EMPLOYEE(ID SERIAL PRIMARY KEY, DEPARTMENT_ID INTEGER NOT NULL, SALARY FLOAT NOT NULL);

Write a query which return MAX AVG SALARY for DEPARTMENT ROUNDED to 4 DECIMAL points
and DEPARTMENT NAME. IF MAX AVG SALARY is the same in more than one DEPARMENT, return 
all DEPARTMENTS (not ordered).

*/


SELECT
    department.name,
    CAST(ROUND(AVG(salary), 4) as DECIMAL(10,4)) AS avg_salary
FROM
    professor, department
WHERE
    professor.department_id = department.id
GROUP BY
    department.name
HAVING
    AVG(salary) =       
    (
    SELECT
        MAX(avg_salary)
    FROM
        (
        SELECT
            AVG(professor.salary) AS avg_salary
        FROM
            professor
        GROUP BY
            department_id
        )
        AS averages
    );
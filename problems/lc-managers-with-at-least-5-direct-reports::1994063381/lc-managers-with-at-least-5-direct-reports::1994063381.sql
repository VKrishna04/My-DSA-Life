# Write your MySQL query statement below
select m.name
from employee as m
inner join employee as e
on e.managerId = m.id
group by m.id
having count(e.id) >= 5
-- select first_name as FirstName , last_name as LastName from employees
-- select distinct department_id from departments
-- select * from employees order by first_name desc
-- select first_name,last_name ,salary ,salary/100*15 as pf from employees
-- select employee_id , first_name , last_name , salary from employees order by salary asc
-- select sum(salary) from employees 
-- select max(salary),min(salary) from employees
-- select avg(salary) from employees
-- select count(first_name) from employees
-- select upper(first_name) as first_name from employees 
-- select substring(first_name , 1,3) from employees
-- select first_name ||' '||last_name as full_name from employees
-- select first_name,last_name  ,length(first_name) +length(last_name) as full_name from employees
-- select first_name from employees where  first_name like '%[^0-9]%'
-- select * from employees limit 10

-- 🌟 Restricting And Sorting
-- select first_name , last_name , salary from employees where salary between 10000 and 15000
-- select first_name, last_name,hire_date from employees where hire_date between '1987-01-01' and '1987-12-31'
-- select * from employees where first_name ilike '%c%' and first_name ilike '%e%'
-- select e.last_name,e.salary,f.job_title,f.min_salary,f.max_salary 
-- from employees as e
-- inner join jobs as f
-- on e.job_id = f.job_id
-- where f.job_title not ilike 'Programmer' and job_title not ilike 'Shipping Clerk' and salary != 4500 and salary !=10000 and salary != 15000
-- select last_name from employees where length(last_name)=6
-- select last_name from employees where last_name ilike '__e%'
-- select e.last_name,e.first_name,f.job_title
-- from employees as e
-- inner join jobs as f
-- on e.job_id = f.job_id
select * from employees where last_name ilike 'Jones' or last_name ilike 'Blake' or last_name ilike 'Scott' or last_name ilike 'king' or last_name ilike 'ford'
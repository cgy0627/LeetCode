# Write your MySQL query statement below
select u.name, sum(t.amount) as balance from Users as u, Transactions as t where u.account = t.account group by t.account having balance > 10000;
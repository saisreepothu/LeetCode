-- LeetCode 3497: Analyze Subscription Conversion

--- this is the single table traversal 
select user_id,
round(AVG(case when activity_type = 'free_trial' then activity_duration end), 2) as trial_avg_duration,
round(AVG(case when activity_type = "paid" then activity_duration end), 2) as paid_avg_duration
from useractivity 
group by user_id
having sum(activity_type = 'free_trial') > 0
and sum(activity_type = 'paid') > 0 


#-----using joins 

with paid_customer as (select user_id, round(avg(activity_duration), 2) as paid_avg_duration from USERACTIVITY  where activity_type = 'paid' group by user_id),
trial_customer as (select user_id, round(avg(activity_duration), 2) as trial_avg_duration from USERACTIVITY  where activity_type = 'free_trial' group by user_id)
select a.user_id , trial_avg_duration, paid_avg_duration FROM paid_customer a join trial_customer b on a.user_id = b.user_id 
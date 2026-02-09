with unbanned as 
(select users_id from users where banned = 'No'),
t1 as (select * from trips where client_id in (select users_id from unbanned) and 
driver_id in (select users_id from unbanned)),
trip as (
    select 
    request_at as Day,
    count(id) as total_rides,
    sum(case when status like 'cancelled%' then 1 else 0 end) as cancel_rides
     from t1 
    where request_at between '2013-10-01' and '2013-10-03'
    group by request_at)

select Day, round(cancel_rides/total_rides, 2) as  'Cancellation Rate' from trip 
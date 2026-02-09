with
    t1 as (
        select
            user_id,
            a.product_id,
            quantity,
            category,
            price
        from
            ProductPurchases a
            join ProductInfo b on a.product_id = b.product_id
    )
select
    a.category as category1,
    b.category as category2,
    count(distinct a.user_id) as customer_count
from
    t1 a
    join t1 b on a.category < b.category
    and a.user_id = b.user_id
group by
    category1,
    category2
having
    count(distinct a.user_id) >= 3
order by
    customer_count desc,
    category1 asc,
    category2 asc
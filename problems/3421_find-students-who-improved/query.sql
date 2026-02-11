WITH dates AS (
    SELECT
        student_id,
        subject,
        MIN(exam_date) AS first_date,
        MAX(exam_date) AS latest_date
    FROM Scores
    GROUP BY student_id, subject
    HAVING MIN(exam_date) <> MAX(exam_date)   -- at least 2 different dates
)
SELECT
    d.student_id,
    d.subject,
    s_first.score  AS first_score,
    s_last.score   AS latest_score
FROM dates d
JOIN Scores s_first
  ON s_first.student_id = d.student_id
 AND s_first.subject    = d.subject
 And s_first.exam_date  = d.first_date
JOIN Scores s_last
  ON s_last.student_id = d.student_id
 AND s_last.subject    = d.subject
 And s_last.exam_date  = d.latest_date
WHERE s_last.score > s_first.score
ORDER BY d.student_id, d.subject;

#-------
with cte as (SELECT student_id, subject, 
first_value(score) over (partition by student_id, subject order by exam_date ) as first_score, 
first_value(score) over (partition by student_id, subject order by exam_date desc) as latest_score
FROM Scores )

select  student_id, subject, first_score, latest_score from cte where first_score < latest_score group by student_id, subject, first_score, latest_score

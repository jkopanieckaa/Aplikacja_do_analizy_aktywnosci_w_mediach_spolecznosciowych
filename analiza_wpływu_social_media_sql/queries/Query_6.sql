create view dataset_united as
SELECT age, screen_time_min
from mental_health_and_social_media_balance_dataset
UNION ALL
Select age, social_media_time_min
from mental_health_social_media_dataset
UNION ALL
select age, screen_time_min
from screentime_vs_mentalwellness
UNION ALL
SELECT AGE, screen_time_min
from students_social_media_addiction
UNION ALL
select age, "Total Time Spent"
from time_wasters_on_social_media
where screen_time_min <= 700;



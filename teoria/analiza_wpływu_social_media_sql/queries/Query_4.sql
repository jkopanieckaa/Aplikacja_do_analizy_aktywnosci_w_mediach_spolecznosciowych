SELECT person_name,count(person_name)
FROM mental_health_social_media_dataset
group by person_name;


select min(age), max(age), AVG(age)
from mental_health_social_media_dataset;

select platform, count(platform)
from mental_health_social_media_dataset
group by platform;

select date
from mental_health_social_media_dataset
where date like '11%2025';

select min(mood_level), max(mood_level)
from mental_health_social_media_dataset;

select avg(mood_level)
from mental_health_social_media_dataset;

select min(negative_interactions_count), max(negative_interactions_count), AVG(negative_interactions_count)
from mental_health_social_media_dataset;

alter table public.mental_health_social_media_dataset
    alter column social_media_time_min type integer using social_media_time_min::integer;

select gender, count(gender)
from mental_health_social_media_dataset
group by gender;
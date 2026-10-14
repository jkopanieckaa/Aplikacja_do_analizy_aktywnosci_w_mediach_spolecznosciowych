SELECT
    "Daily_Screen_Time(hrs)",
     AS screen_time_min
FROM mental_health_and_social_media_balance_dataset;

alter table students_social_media_addiction add column screen_time_min INTEGER;

update students_social_media_addiction set screen_time_min = FLOOR("avg_daily_usage_hours") * 60
    + ROUND(("avg_daily_usage_hours" - FLOOR("avg_daily_usage_hours")) * 100) where screen_time_min IS NULL;

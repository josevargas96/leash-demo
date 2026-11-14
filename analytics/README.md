# Leash analytics

Product analytics, the way a dashboard tool would export them. logs/ only holds the walks support has asked about; these files hold every walk.

- **walks-since-launch.csv:** one row per walk that ended between the 4.12 launch (Mon Nov 2, 10:00 AM) and Wed Nov 4, 8:00 PM.
    - outcome: counted, not_counted (under 20 tracked minutes) or cancelled_weather
    - duration_min: start to end on the clock. tracked_min: minutes with GPS signal. gps_gap_min: the difference.
    - alert_type: walk_done, not_counted or weather_cancel. alert_status: delivered or failed. alert_opened: yes or no (blank if it never arrived).
    - owner_texts_to_walker: messages the owner sent the walker during the walk
    - app_opens_during_walk: times the owner opened the app while the walk was on. app_opens_first_10_min: how many of those were in the first 10 minutes.
- **week-before-launch.json:** the same numbers for the week before 4.12, to compare against.

from datetime import datetime, date, timedelta

semester_start = date(2026, 9, 7)
semester_end = date(2026, 12, 19)
total_weeks = 15

today = datetime.now().date()

week_start = today - timedelta(days=today.weekday())
week_end = min(week_start + timedelta(days=6),semester_end)

print(week_end)
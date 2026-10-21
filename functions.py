from datetime import date, timedelta

SEMESTER_START = date(2026, 9, 7)
SEMESTER_END = date(2026, 12, 19)
TOTAL_WEEKS = 15

def today():
    current_date = date.today()
    weekday_names = [
        "Понедельник",
        "Вторник",
        "Среда",
        "Четверг",
        "Пятница",
        "Суббота",
        "Воскресенье"
    ]
    monday = current_date - timedelta(days=current_date.weekday())
    sunday = monday + timedelta(days=6)
    if current_date < SEMESTER_START:
        week_number = 0
    elif current_date > SEMESTER_END:
        week_number = TOTAL_WEEKS
    else:
        week_number = (
            (current_date - SEMESTER_START).days // 7 + 1
        )
    return (
        "📚 Учебный календарь\n\n"
        f"🎓 Учебная неделя: {week_number} из {TOTAL_WEEKS}\n\n"
        f"📅 Дата: {current_date:%d.%m.%Y}\n\n"
        f"📅 День недели: "
        f"{weekday_names[current_date.weekday()]}\n\n"
        f"📆 Период: {monday:%d.%m}–{sunday:%d.%m} "
    )

class Course:
    def __init__(self):
        self.courses = {
            "PVSh 5201": {
                "name": "Педагогика высшей школы",
                "ects": "4",
                "teacher": "Жукенова Г.Б."
            },
            "PU 5202": {
                "name": "Психология управления",
                "ects": "4",
                "teacher": "Мамбеталина А.С."
            },
            "ADYaP 5212": {
                "name": "Анализ данных на языке Python",
                "ects": "5",
                "teacher": "Тихонова О.А."
            },
            "PM 5204": {
                "name": "Проектный менеджмент",
                "ects": "5",
                "teacher": "Тлеубердиева С.С."
            },
            "VOT 5214": {
                "name": "Виртуализация и облачные технологии",
                "ects": "5",
                "teacher": "Тихонова О.А."
            },
            "IFN 5204": {
                "name": "История и философия науки",
                "ects": "4",
                "teacher": "Нет данных"
            },
            "TIBD 5316": {
                "name": "Технологии и инструменты Big Data",
                "ects": "5",
                "teacher": "Нет данных"
            }
        }

    def get_courses(self):
        text = "📚 Доступные курсы:\n\n"

        for course in self.courses.values():
            text += f"📖 {course['name']}\n"

        return text

    def get_course_info(self, course_id):
        course = self.courses.get(course_id)
        if course is None:
            return "❌ Предмет не найден."

        return (
            f"📚 Предмет: {course['name']}\n\n"
            f"📝 Описание: {course['ects']}\n"
            f"👨‍🏫 Преподаватель: {course['teacher']}"
        )
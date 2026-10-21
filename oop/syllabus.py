
import re
from pathlib import Path


class Syllabus:
    def __init__(self):
        self.folder = Path("syllabus")
        self.files = {
            "PVSh 5201": "pedagogy.md",
            "PU 5202": "psychology.md"
        }
    def get_week_info(self, course_id, week):
        if course_id not in self.files:
            return "❌ Нет информации."
        if week < 1 or week > 15:
            return "❌ Укажите неделю от 1 до 15."
        file_path = self.folder / self.files[course_id]

        if not file_path.exists():
            return "❌ Файл силлабуса не найден."
        text = file_path.read_text(encoding="utf-8")

        pattern = r"(?m)^#{2,4}\s+Неделя\s+(\d+)\b[^\n]*"
        matches = list(re.finditer(pattern, text, re.IGNORECASE))
        for i, match in enumerate(matches):
            if int(match.group(1)) == week:
                start = match.start()
                if i + 1 < len(matches):
                    end = matches[i + 1].start()
                else:
                    end = len(text)
                section = text[start:end].strip()
                return section
        return f"❌ Информация за {week}-ю неделю не найдена."

# -*- coding: utf-8 -*-
"""
Скрипт для создания PDF-календаря на 2026 год.
Формат A3 (альбомная ориентация), 365 клеточек.
"""

from reportlab.lib.pagesizes import A3, landscape
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor
import datetime
import os

# ============================================================
# SETTINGS - Edit these values to customize your calendar
# ============================================================

# Year for the calendar
YEAR = 2026

# Output file name
OUTPUT_FILENAME = "calendar_2026.pdf"

# Month names (customize for your language)
MONTHS = [
    "янв.", "фев.", "мар.", "апр.", "май", "июн.",
    "июл.", "авг.", "сен.", "окт.", "ноя.", "дек."
]

# Grid layout (columns x rows)
COLS = 25
ROWS = 15

# Page margins for printing (in mm)
MARGIN_MM = 15

# Cell padding (in mm)
CELL_PADDING_MM = 0.5

# Border line width
LINE_WIDTH = 0.25

# Colors
COLOR_BORDER = "#000000"    # Black - cell borders
COLOR_TEXT = "#555555"      # Dark gray - date and day number

# Font directory (relative to script)
FONT_DIR = "Roboto Font"

# ============================================================
# END OF SETTINGS
# ============================================================

# Convert settings to internal units
MARGIN = MARGIN_MM * mm
CELL_PADDING = CELL_PADDING_MM * mm
PAGE_WIDTH, PAGE_HEIGHT = landscape(A3)


def register_fonts():
    """Регистрация шрифтов Roboto для поддержки кириллицы."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    font_dir = os.path.join(script_dir, FONT_DIR)

    pdfmetrics.registerFont(TTFont('Roboto', os.path.join(font_dir, 'Roboto-Regular.ttf')))
    pdfmetrics.registerFont(TTFont('Roboto-Light', os.path.join(font_dir, 'Roboto-Light.ttf')))


def generate_days(year):
    """
    Генерирует список дней года.
    Возвращает список кортежей: (номер_дня, число_месяца, индекс_месяца)
    """
    days = []
    start_date = datetime.date(year, 1, 1)
    end_date = datetime.date(year, 12, 31)

    current = start_date
    day_number = 1

    while current <= end_date:
        days.append((day_number, current.day, current.month - 1))
        current += datetime.timedelta(days=1)
        day_number += 1

    return days


def draw_cell(c, x, y, width, height, day_data):
    """
    Рисует одну клетку календаря.

    Args:
        c: canvas объект
        x, y: координаты левого нижнего угла клетки
        width, height: размеры клетки
        day_data: кортеж (номер_дня, число_месяца, индекс_месяца) или None
    """
    # Рисуем границу клетки
    c.setStrokeColor(HexColor(COLOR_BORDER))
    c.setLineWidth(LINE_WIDTH)
    c.rect(x, y, width, height, stroke=1, fill=0)

    if day_data is None:
        return

    day_number, day_of_month, month_index = day_data

    # Размеры шрифтов (адаптивные)
    font_size = min(height * 0.18, width * 0.12)

    # Дата и месяц сверху слева
    date_text = f"{day_of_month:02d} {MONTHS[month_index]}"
    c.setFont('Roboto', font_size)
    c.setFillColor(HexColor(COLOR_TEXT))
    c.drawString(x + CELL_PADDING, y + height - CELL_PADDING - font_size, date_text)

    # Номер дня справа внизу (симметрично дате)
    day_number_text = str(day_number)
    text_width = c.stringWidth(day_number_text, 'Roboto', font_size)
    text_x = x + width - CELL_PADDING - text_width
    text_y = y + CELL_PADDING

    c.drawString(text_x, text_y, day_number_text)


def create_calendar_pdf(output_filename=OUTPUT_FILENAME):
    """Создает PDF-календарь."""

    # Регистрируем шрифты
    register_fonts()

    # Генерируем список дней
    days = generate_days(YEAR)

    # Вычисляем размеры рабочей области
    work_width = PAGE_WIDTH - 2 * MARGIN
    work_height = PAGE_HEIGHT - 2 * MARGIN

    # Размеры клетки
    cell_width = work_width / COLS
    cell_height = work_height / ROWS

    # Создаем canvas
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(script_dir, output_filename)
    c = canvas.Canvas(output_path, pagesize=landscape(A3))

    # Рисуем клетки (только заполненные)
    for day_index, day_data in enumerate(days):
        row = day_index // COLS
        col = day_index % COLS

        # Координаты клетки (слева направо, сверху вниз)
        x = MARGIN + col * cell_width
        y = PAGE_HEIGHT - MARGIN - (row + 1) * cell_height

        draw_cell(c, x, y, cell_width, cell_height, day_data)

    # Сохраняем PDF
    c.save()
    print(f"PDF-календарь создан: {output_path}")
    print(f"Формат: A3 (альбомная ориентация)")
    print(f"Сетка: {COLS}x{ROWS}")
    print(f"Ячеек: {len(days)}")


if __name__ == "__main__":
    create_calendar_pdf()

# 365 Days Wall Calendar PDF Generator

Generate a **printable A3 wall calendar** with 365 boxes — one for each day of the year. Perfect for yearly planning, habit tracking, and goal visualization.

<p align="center">
  <img src="calendar_2026_ru.jpg" alt="Printable 365 day wall calendar for yearly planning and habit tracking" width="100%">
</p>

## Features

- **A3 printable format** (420×297mm) — fits standard poster frames
- **365 numbered day boxes** — date, month, and day-of-year number (1-365)
- **Minimalist design** — clean lines, readable fonts, lots of writing space
- **Multi-language support** — easily customize month names for any language
- **Customizable colors** — adjust borders and text colors to your preference
- **Print-ready PDF output** — includes margins for easy printing

## Use Cases

- **Habit tracking** — mark each day you exercise, read, meditate, or code
- **Year-long project planning** — visualize deadlines and milestones at a glance
- **Goal countdown** — track progress toward yearly goals
- **Daily journaling** — use as a prompt for daily reflections
- **Productivity tracking** — see your entire year of work on one page

## Quick Start

```bash
pip install reportlab
python calendar_2026.py
```

Then print `calendar_2026.pdf` on A3 paper.

## Customization

Edit settings at the top of `calendar_2026.py`:

```python
YEAR = 2026

MONTHS = [
    "Jan", "Feb", "Mar", "Apr", "May", "Jun",
    "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
]

COLS = 25          # Grid columns
ROWS = 15          # Grid rows

COLOR_BORDER = "#000000"
COLOR_TEXT = "#555555"
```

### Language Examples

**Russian:**
```python
MONTHS = ["янв.", "фев.", "мар.", "апр.", "май", "июн.", "июл.", "авг.", "сен.", "окт.", "ноя.", "дек."]
```

**German:**
```python
MONTHS = ["Jan", "Feb", "Mär", "Apr", "Mai", "Jun", "Jul", "Aug", "Sep", "Okt", "Nov", "Dez"]
```

**Spanish:**
```python
MONTHS = ["ene", "feb", "mar", "abr", "may", "jun", "jul", "ago", "sep", "oct", "nov", "dic"]
```

## Requirements

- Python 3.6+
- [ReportLab](https://www.reportlab.com/)

## License

[MIT](LICENSE)

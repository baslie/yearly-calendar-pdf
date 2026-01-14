# 365 Days Wall Calendar

A simple Python script that generates a printable A3 wall calendar with 365 boxes — one for each day of the year.

## Why This Calendar?

Planning your year shouldn't require expensive tools or subscriptions. Print this minimalist calendar, hang it on your wall, and see your entire year at a glance.

**Perfect for:**
- Habit tracking (mark each day you exercise, meditate, or learn)
- Project deadlines and milestones
- Countdown to important events
- Daily journaling prompts
- Visualizing your yearly progress

## What You Get

- **A3 format** (420×297mm) — large enough to write in, fits standard frames
- **365 numbered boxes** — each shows the date, month, and day number (1-365)
- **Clean minimal design** — thin borders, readable text, plenty of white space
- **Print-ready PDF** — margins included for easy printing

## Quick Start

1. Install the required library:
   ```
   pip install reportlab
   ```

2. Run the script:
   ```
   python calendar_2026.py
   ```

3. Print `calendar_2026.pdf` on A3 paper

## Customization

Edit the settings at the top of `calendar_2026.py`:

```python
# Year for the calendar
YEAR = 2026

# Month names (customize for your language)
MONTHS = [
    "янв.", "фев.", "мар.", "апр.", "май", "июн.",
    "июл.", "авг.", "сен.", "окт.", "ноя.", "дек."
]

# Grid layout (columns x rows)
COLS = 25
ROWS = 15

# Colors
COLOR_BORDER = "#000000"    # Cell borders
COLOR_TEXT = "#555555"      # Date text
```

### Language Examples

**English:**
```python
MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
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
- reportlab

## License

[MIT](LICENSE)

# ISM3232 Midterm: Harvest Table Catering

- **Name:** Pamela Emmrich
- **Version:** 1.0
- **Date:** October 21, 2026

## What This Program Does

Harvest Table Catering's catering event pricing are determined by this program. It calculates the cost of meals for each occasion, applies the appropriate discount, and, if applicable, adds a service charge. After that, it prints a report with the amount of each event, a summary of all the events, and information about whether a manager's approval or a second chef is required.

## Business Rules

1. The price per customer multiplied by the number of guests is the meal cost.
2. There is no discount for events with fewer than 25 attendees. 5% off events with 25 to 99 attendees, and 12% off events with 100 or more attendees.
3. Only registered nonprofit organizations are eligible for the 12% discount. 5% is applied to any other event with 100 or more attendees.
4. If the discounted price is $500 or less, a $75 service charge is applied.
5. A manager's approval is required for events costing more than $2,500.
6. When an event has more than 80 attendees or costs $3,000 or more, a second chef is required.

## How to Run

```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python main.py
```

## How to Test

```
ruff format .
ruff check .
pytest -v
```

I wrote 30 tests.

## Files in This Repository

- `business_rules.py`: the eight functions that apply the business rules.
- `main.py`: the event list and the code that prints the report.
- `commands.md`: a record of the terminal commands I used and their output.
- `README.md`: this file, which explains how to use the project.
- `requirements.txt`: the Python packages the project needs.
- `.gitignore`: tells git to leave out `.venv/` and `__pycache__/`.
- `tests/__init__.py`: marks the tests folder as a Python package.
- `tests/test_business_rules.py`: the 30 tests for the business rules.

## AI Use Statement

I did not use AI
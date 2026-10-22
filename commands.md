# Terminal Record: Harvest Table Catering

## 1. Building the project

```
cd ~
mkdir ism3232-midterm
cd ism3232-midterm
git rev-parse --show-toplevel
deactivate
git init
python3 -m venv .venv
source .venv/bin/activate
pip install pytest ruff
touch business_rules.py main.py commands.md README.md requirements.txt .gitignore
mkdir tests
touch tests/__init__.py tests/test_business_rules.py
printf ".venv/\n__pycache__/\n" > .gitignore
pip freeze > requirements.txt
ls -a
ls tests
git status
git add .
git commit -m "Start midterm: project structure and environment"
git config --global user.name "Pamelaemmrich"
git config --global user.email "pamelaemmrich@usf.edu"
git branch -M main
git remote add origin https://github.com/pamelaemmrich/ism3232-midterm.git
git push -u origin main
git remote set-url origin https://github.com/Pamelaemmrich/ism3232-midterm.git
git add commands.md
git commit -m "Add commands log"
git push
git add business_rules.py
git commit -m "Add business rules functions"
git push
git add tests/test_business_rules.py
git commit -m "Add business rules tests"
git push
git add main.py
git commit -m "Add main.py event report"
git push
brew install ripgrep
```

## 2. The virtual environment

```
which python3
```

```
/Users/pamelaemmrich/ism3232-midterm/.venv/bin/python3
```

The path goes through ism3232-midterm/.venv/bin/, which shows the virtual environment is active.

## 3. The project structure

```
tree -L 2
```

```
.
├── __pycache__
│   └── business_rules.cpython-314.pyc
├── business_rules.py
├── commands.md
├── main.py
├── README.md
├── requirements.txt
└── tests
    ├── __init__.py
    ├── __pycache__
    └── test_business_rules.py

4 directories, 8 files
```

The __pycache__ folder is on my computer but not in my GitHub repository, because .gitignore tells git to leave it out.

## 4. Every function and test

```
rg 'def '
```

```
tests/test_business_rules.py:def make_event(client, guest_price, guests, nonprofit=False):
tests/test_business_rules.py:def test_food_cost_is_price_times_guests():
tests/test_business_rules.py:def test_food_cost_with_zero_guests_is_zero():
tests/test_business_rules.py:def test_discount_24_guests_is_none():
tests/test_business_rules.py:def test_discount_25_guests_is_five_percent():
tests/test_business_rules.py:def test_discount_99_guests_is_five_percent():
tests/test_business_rules.py:def test_discount_100_guests_not_nonprofit_is_five_percent():
tests/test_business_rules.py:def test_discount_100_guests_nonprofit_is_twelve_percent():
tests/test_business_rules.py:def test_discount_99_guests_nonprofit_is_five_percent():
tests/test_business_rules.py:def test_nonprofit_changes_discount_at_150_guests():
tests/test_business_rules.py:def test_nonprofit_changes_event_total_for_120_guests():
tests/test_business_rules.py:def test_event_total_small_event_adds_service_fee():
tests/test_business_rules.py:def test_event_total_discounted_cost_exactly_500_adds_fee():
tests/test_business_rules.py:def test_event_total_discounted_cost_just_under_500_adds_fee():
tests/test_business_rules.py:def test_event_total_discounted_cost_just_over_500_has_no_fee():
tests/test_business_rules.py:def test_event_total_applies_discount_before_fee_check():
tests/test_business_rules.py:def test_event_total_large_nonprofit_event():
tests/test_business_rules.py:def test_signoff_exactly_2500_is_not_needed():
tests/test_business_rules.py:def test_signoff_just_over_2500_is_needed():
tests/test_business_rules.py:def test_signoff_small_total_is_not_needed():
tests/test_business_rules.py:def test_second_chef_exactly_80_guests_is_not_needed():
tests/test_business_rules.py:def test_second_chef_81_guests_is_needed():
tests/test_business_rules.py:def test_second_chef_total_just_under_3000_is_not_needed():
tests/test_business_rules.py:def test_second_chef_total_exactly_3000_is_needed():
tests/test_business_rules.py:def test_total_booked_adds_event_totals():
tests/test_business_rules.py:def test_total_booked_empty_list_is_zero():
tests/test_business_rules.py:def test_largest_event_returns_client_with_biggest_total():
tests/test_business_rules.py:def test_largest_event_tie_returns_first_in_list():
tests/test_business_rules.py:def test_largest_event_empty_list_returns_empty_string():
tests/test_business_rules.py:def test_format_event_line_with_no_flags():
tests/test_business_rules.py:def test_format_event_line_with_both_flags_and_two_decimals():
main.py:def main() -> None:
business_rules.py:def calculate_food_cost(guest_price: float, guests: int) -> float:
business_rules.py:def get_event_discount(guests: int, nonprofit: bool = False) -> float:
business_rules.py:def calculate_event_total(
business_rules.py:def needs_signoff(total: float) -> bool:
business_rules.py:def needs_second_chef(guests: int, total: float) -> bool:
business_rules.py:def total_booked(events: list) -> float:
business_rules.py:def largest_event(events: list) -> str:
business_rules.py:def format_event_line(
```

business_rules.py defines 8 functions, and tests/test_business_rules.py defines 30 tests (plus one helper function, make_event).

## 5. Which files print

```
rg -l 'print'
```

```
main.py
```

Only main.py prints among the Python files, and business_rules.py is not in the list because its functions return values instead of printing them.

## 6. The commit history

```
git log --oneline
```

```
d3f33cb Complete commands.md terminal record
b3fb5aa Add main.py event report
8e541f6 Add business rules tests
c50a393 Add business rules functions
ce10c93 Add commands log
caf4273 Start midterm: project structure and environment
```

There were 6 commits at that point.

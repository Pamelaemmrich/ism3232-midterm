"""Tests for the Harvest Table Catering business rules."""

from business_rules import (
    calculate_event_total,
    calculate_food_cost,
    format_event_line,
    get_event_discount,
    largest_event,
    needs_second_chef,
    needs_signoff,
    total_booked,
)


def make_event(client, guest_price, guests, nonprofit=False):
    """Build one event dictionary for a test."""
    return {
        "client": client,
        "guest_price": guest_price,
        "guests": guests,
        "nonprofit": nonprofit,
    }


# calculate_food_cost (rule 1)


def test_food_cost_is_price_times_guests():
    assert round(calculate_food_cost(18.00, 20), 2) == 360.00


def test_food_cost_with_zero_guests_is_zero():
    assert round(calculate_food_cost(18.00, 0), 2) == 0.00


# get_event_discount (rules 2 and 3)


def test_discount_24_guests_is_none():
    assert get_event_discount(24) == 0.0


def test_discount_25_guests_is_five_percent():
    assert get_event_discount(25) == 0.05


def test_discount_99_guests_is_five_percent():
    assert get_event_discount(99) == 0.05


def test_discount_100_guests_not_nonprofit_is_five_percent():
    assert get_event_discount(100, nonprofit=False) == 0.05


def test_discount_100_guests_nonprofit_is_twelve_percent():
    assert get_event_discount(100, nonprofit=True) == 0.12


def test_discount_99_guests_nonprofit_is_five_percent():
    assert get_event_discount(99, nonprofit=True) == 0.05


def test_nonprofit_changes_discount_at_150_guests():
    assert get_event_discount(150, nonprofit=False) != get_event_discount(
        150, nonprofit=True
    )


def test_nonprofit_changes_event_total_for_120_guests():
    regular = calculate_event_total(30.00, 120, nonprofit=False)
    nonprofit = calculate_event_total(30.00, 120, nonprofit=True)
    assert round(regular, 2) == 3420.00
    assert round(nonprofit, 2) == 3168.00


# calculate_event_total (rules 2, 3 and 4)


def test_event_total_small_event_adds_service_fee():
    assert round(calculate_event_total(18.00, 20), 2) == 435.00


def test_event_total_discounted_cost_exactly_500_adds_fee():
    assert round(calculate_event_total(100.00, 5), 2) == 575.00


def test_event_total_discounted_cost_just_under_500_adds_fee():
    assert round(calculate_event_total(99.75, 5), 2) == 573.75


def test_event_total_discounted_cost_just_over_500_has_no_fee():
    assert round(calculate_event_total(100.25, 5), 2) == 501.25


def test_event_total_applies_discount_before_fee_check():
    assert round(calculate_event_total(22.00, 40, nonprofit=True), 2) == 836.00


def test_event_total_large_nonprofit_event():
    assert round(calculate_event_total(25.00, 150, nonprofit=True), 2) == 3300.00


# needs_signoff (rule 5)


def test_signoff_exactly_2500_is_not_needed():
    assert needs_signoff(2500.00) is False


def test_signoff_just_over_2500_is_needed():
    assert needs_signoff(2500.01) is True


def test_signoff_small_total_is_not_needed():
    assert needs_signoff(435.00) is False


# needs_second_chef (rule 6)


def test_second_chef_exactly_80_guests_is_not_needed():
    assert needs_second_chef(80, 100.00) is False


def test_second_chef_81_guests_is_needed():
    assert needs_second_chef(81, 100.00) is True


def test_second_chef_total_just_under_3000_is_not_needed():
    assert needs_second_chef(10, 2999.99) is False


def test_second_chef_total_exactly_3000_is_needed():
    assert needs_second_chef(10, 3000.00) is True


# total_booked


def test_total_booked_adds_event_totals():
    events = [
        make_event("Alpha", 10.00, 10),
        make_event("Beta", 20.00, 30),
    ]
    assert round(total_booked(events), 2) == 745.00


def test_total_booked_empty_list_is_zero():
    assert round(total_booked([]), 2) == 0.00


# largest_event


def test_largest_event_returns_client_with_biggest_total():
    events = [
        make_event("Alpha", 10.00, 10),
        make_event("Beta", 20.00, 30),
        make_event("Gamma", 10.00, 10),
    ]
    assert largest_event(events) == "Beta"


def test_largest_event_tie_returns_first_in_list():
    events = [
        make_event("First", 10.00, 10),
        make_event("Second", 10.00, 10),
    ]
    assert largest_event(events) == "First"


def test_largest_event_empty_list_returns_empty_string():
    assert largest_event([]) == ""


# format_event_line


def test_format_event_line_with_no_flags():
    line = format_event_line("Finch Law", 435.00, False, False)
    assert line == "Finch Law: $435.00 | sign-off: no | second chef: no"


def test_format_event_line_with_both_flags_and_two_decimals():
    line = format_event_line("Hilltop Gym", 3420, True, True)
    assert line == "Hilltop Gym: $3420.00 | sign-off: yes | second chef: yes"

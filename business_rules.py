"""Business rules for Harvest Table Catering."""

# Rule 2 and 3: discounts
SMALL_DISCOUNT_MIN_GUESTS = 25
LARGE_DISCOUNT_MIN_GUESTS = 100
NO_DISCOUNT = 0.0
SMALL_DISCOUNT = 0.05
NONPROFIT_DISCOUNT = 0.12

# Rule 4: service fee
SERVICE_FEE = 75.0
SERVICE_FEE_MAX_COST = 500.0

# Rule 5: manager sign-off
SIGNOFF_MIN_TOTAL = 2500.0

# Rule 6: second chef
SECOND_CHEF_MIN_GUESTS = 80
SECOND_CHEF_MIN_TOTAL = 3000.0


def calculate_food_cost(guest_price: float, guests: int) -> float:
    """Return the food cost before any discount."""
    return guest_price * guests


def get_event_discount(guests: int, nonprofit: bool = False) -> float:
    """Return the discount rate as a decimal."""
    if guests >= LARGE_DISCOUNT_MIN_GUESTS:
        if nonprofit:
            return NONPROFIT_DISCOUNT
        return SMALL_DISCOUNT
    if guests >= SMALL_DISCOUNT_MIN_GUESTS:
        return SMALL_DISCOUNT
    return NO_DISCOUNT


def calculate_event_total(
    guest_price: float, guests: int, nonprofit: bool = False
) -> float:
    """Return the discounted cost plus the service fee when it applies."""
    food_cost = calculate_food_cost(guest_price, guests)
    discount = get_event_discount(guests, nonprofit)
    discounted_cost = food_cost * (1 - discount)
    if discounted_cost <= SERVICE_FEE_MAX_COST:
        return discounted_cost + SERVICE_FEE
    return discounted_cost


def needs_signoff(total: float) -> bool:
    """Return True when the event total needs a manager's sign-off."""
    return total > SIGNOFF_MIN_TOTAL


def needs_second_chef(guests: int, total: float) -> bool:
    """Return True when the event needs a second chef."""
    return guests > SECOND_CHEF_MIN_GUESTS or total >= SECOND_CHEF_MIN_TOTAL


def total_booked(events: list) -> float:
    """Return the sum of the event totals for every event in the list."""
    booked = 0.0
    for event in events:
        booked += calculate_event_total(
            event["guest_price"], event["guests"], event["nonprofit"]
        )
    return booked


def largest_event(events: list) -> str:
    """Return the client with the largest event total, first one wins ties."""
    best_client = ""
    best_total = None
    for event in events:
        total = calculate_event_total(
            event["guest_price"], event["guests"], event["nonprofit"]
        )
        if best_total is None or total > best_total:
            best_total = total
            best_client = event["client"]
    return best_client


def format_event_line(
    client: str, total: float, signoff: bool, second_chef: bool
) -> str:
    """Return one report line for an event."""
    signoff_text = "yes" if signoff else "no"
    chef_text = "yes" if second_chef else "no"
    return (
        f"{client}: ${total:.2f} | sign-off: {signoff_text} | second chef: {chef_text}"
    )

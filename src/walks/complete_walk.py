"""Decides whether a walk counts as completed when the walker taps End."""

MIN_DURATION_MIN = 25
MIN_DISTANCE_MI = 0.5


def complete_walk(walk):
    """walk has duration_min, distance_mi and gps_gap_minutes.

    A walk is completed only if it was long enough AND covered enough distance.
    Otherwise the owner is refunded and the walker is not paid.
    """
    if walk["duration_min"] < MIN_DURATION_MIN or walk["distance_mi"] < MIN_DISTANCE_MI:
        refund_owner(walk)
        skip_walker_payout(walk)
        return "incomplete"

    charge_owner(walk)
    pay_walker(walk)
    return "completed"


def refund_owner(walk): ...
def skip_walker_payout(walk): ...
def charge_owner(walk): ...
def pay_walker(walk): ...

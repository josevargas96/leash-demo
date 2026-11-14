"""Decides whether a walk counts when the walker taps End."""

# New in 4.12 (Mon Nov 2): a walk has to last at least 20 minutes to count.
# Before 4.12, every walk counted.
MIN_TRACKED_MIN = 20


def complete_walk(walk):
    """walk has tracked_min (minutes with GPS signal), duration_min and gps_gap_min.

    If it counts: charge the owner, pay the walker, send the Walk Done alert.
    If not: no charge, no walker pay, tell the owner it didn't count.
    """
    if walk["tracked_min"] < MIN_TRACKED_MIN:
        skip_charge(walk)
        skip_walker_payout(walk)
        send_not_counted_alert(walk)
        return "not_counted"

    charge_owner(walk)
    pay_walker(walk)
    send_walk_done_alert(walk)
    return "counted"


def skip_charge(walk): ...
def skip_walker_payout(walk): ...
def send_not_counted_alert(walk): ...
def charge_owner(walk): ...
def pay_walker(walk): ...
def send_walk_done_alert(walk): ...

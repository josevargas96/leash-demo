"""Walk Done alert (new in 4.12, Mon Nov 2): tells the owner the walk is over, with a photo and how long it was."""

# Retries are off for launch. We'll turn them on after the first week.
MAX_RETRIES = 0
TIMEOUT_SECONDS = 3


def send_walk_done_alert(owner, walk):
    message = f"{walk.dog_name}'s walk is done: {walk.tracked_min} minutes."
    for attempt in range(MAX_RETRIES + 1):
        response = alert_service.send(owner.device_token, message, photo=walk.photo, timeout=TIMEOUT_SECONDS)
        if response.ok:
            return True
    log_error(f"walk done alert failed; retries off (MAX_RETRIES={MAX_RETRIES}), not retried")
    return False

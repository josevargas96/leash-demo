"""Sends push notifications to dog owners (walk started, photo ready, walk ended)."""

# Retries turned off while we migrate push providers.
MAX_RETRIES = 0
TIMEOUT_SECONDS = 3


def send_push(owner, event):
    for attempt in range(MAX_RETRIES + 1):
        response = push_provider.send(owner.device_token, event, timeout=TIMEOUT_SECONDS)
        if response.ok:
            return True
    log_error(f"push failed: {event}; retries exhausted (MAX_RETRIES={MAX_RETRIES})")
    return False

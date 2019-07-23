from datetime import datetime, timezone
from dateutil import parser

def avoid_infinite_retries(max_age_ms=10*60*1000):
    def avoid_infinite_retries_decorator(func):
        def wrapper(data, context):
            """Decorator for Background Cloud Function to ensure that only executes within a certain
            time period after the triggering event.

            Args:
                data (dict): The event payload.
                context (google.cloud.functions.Context): The event metadata.
                max_age_ms: Stop retrying after this time, default 9 minutes
            Returns:
                None; output is written to Stackdriver Logging
            """

            timestamp = context.timestamp

            event_time = parser.parse(timestamp)
            event_age = (datetime.now(timezone.utc) - event_time).total_seconds()
            event_age_ms = event_age * 1000

            # Ignore events that are too old
            if event_age_ms > max_age_ms:
                print('Dropped {} (age {}ms, retry timeout)'.format(context.event_id, event_age_ms))
                return "Retry timeout."

            # Do what the function is supposed to do
            func(data, context)
        return wrapper
    return avoid_infinite_retries_decorator

from django.db.models import IntegerChoices


class RequestState(IntegerChoices):
    SUBMITTED = 1, "SUBMITTED"
    ON_HOLD = 2, "ON_HOLD"
    REJECTED = 3, "REJECTED"
    CANCELED = 4, "CANCELED"
    ACCEPTED = 5, "ACCEPTED"
    PROCESSING = 6, "PROCESSING"
    COMPLETE = 7, "COMPLETE"
    FAILED = 8, "FAILED"
    ARCHIVED = 9, "ARCHIVED"
    # SUBMITTED = 1, "Submitted"
    # ON_HOLD = 2, "On Hold"
    # REJECTED = 3, "Rejected"
    # CANCELED = 4, "Canceled"
    # ACCEPTED = 5, "Accepted"
    # PROCESSING = 6, "Processing"
    # COMPLETE = 7, "Complete"
    # FAILED = 8, "Failed"
    # ARCHIVED = 9, "Archived"

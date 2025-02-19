from django.db import models
from datetime import timedelta, datetime

class Topic(models.Model):
    subject = models.CharField(max_length=100)  # Subject name
    topic_name = models.CharField(max_length=200)  # Topic title
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set timestamp when created

    def get_repetition_dates(self):
        """
        Generate spaced repetition dates based on the creation date.
        The offsets are in days and represent the intervals for repetitions.
        """
        # Offsets for spaced repetition in days
        offsets = [0, 1, 5, 10, 20, 30]
        return [self.created_at + timedelta(days=offset) for offset in offsets]

    def get_due_revisions(self, reference_date=None):
        """
        Get the due revision dates up to a specific reference date.
        If no reference date is provided, defaults to today.
        """
        if reference_date is None:
            reference_date = datetime.now()

        # Filter only revision dates up to the given date
        return [
            (index + 1, revision_date)
            for index, revision_date in enumerate(self.get_repetition_dates())
            if revision_date.date() <= reference_date.date()
        ]

    def __str__(self):
        return f"{self.subject}: {self.topic_name}"

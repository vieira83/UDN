from django.db import models


class Participants(models.Model):
    REVIEW_CHOICES = (
        ('Not-Rev', 'Not Reviewed'),
        ('Rev-NA', 'Reviewed ­ Accepted'),
        ('Rev-AC', 'Reviewed ­ Not Accepted'),
    )

    name = models.CharField(max_length=55, blank=True, null=False)
    age = models.IntegerField(null=True, blank=True)
    any_siblings = models.BooleanField(default=False)
    known_env_exposures = models.CharField(max_length=55, blank=True, null=True)
    known_genetic_mutations = models.CharField(max_length=55, blank=True, null=True)
    review = models.CharField(max_length =30, default="Not Reviewed")

    def __str__(self):
        return self.name

from django.db import models


class Location(models.Model):
    place = models.CharField(max_length=225)
    people = models.CharField(max_length=225)

    def __str__(self):
        return self.place



CATEGORY_CHOICES = [
        ("FOOD", "Food"),
        ("TRAVEL", "Travel"),
        ("STAY", "Stay"),
        ("TICKET", "Ticket"),
        ("OTHER", "Other"),
    ]


class Expense(models.Model):
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)

    title = models.CharField(max_length=255)

    amount = models.DecimalField(max_digits=10, decimal_places=2)

    location = models.ForeignKey(
        Location,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - ₹{self.amount}"

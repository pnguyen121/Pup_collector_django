from django.db import models
from django.urls import reverse


# Create your models here.

class Pup(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()

# Add a redirect after a form is submitted, make sure its intended to be undder the Pup model
    def get_absolute_url(self):
        return reverse('detail', kwargs={'pup_id': self.id})



# A tuple of 2-tuples
MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner')
)



# Add new Feeding model below Cat model
class Feeding(models.Model):
  date = models.DateField('Feeding date')
  meal = models.CharField(
    max_length=1,
    # add the 'choices' field option to match MEALS above
    choices=MEALS,
    # set the default value for meal to be 'B' bcuz the inddex of the tuples
    default=MEALS[0][0]
  )

  # Create a cat_id FK when something deletes all the feeding delete also on ONE TO MANY YOU NEED THIS
  pup = models.ForeignKey(Pup, on_delete=models.CASCADE)

  def __str__(self):
    # Nice method for obtaining the friendly value of a Field.choice
    return f"{self.get_meal_display()} on {self.date}"

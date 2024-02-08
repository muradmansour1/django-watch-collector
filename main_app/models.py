from django.db import models
from django.contrib.auth.models import User

BRAND = (
    ('R', 'Rolex'),
    ('P', 'Patek'),
    ('G', 'Gshock')
)

class Band(models.Model):
  name = models.CharField(max_length=50)
  color = models.CharField(max_length=20)

  def __str__(self):
    return self.name
  
# Create your models here.
class Watch(models.Model):
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    year = models.IntegerField()
    band = models.ManyToManyField(Band)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

# Add new Feeding model below Cat model
class Brand(models.Model):
  date = models.DateField('Feeding Date')
  brand = models.CharField(
    max_length=1,
    # add the 'choices' field option
    choices=BRAND,
    # set the default value for meal to be 'B'
    default=BRAND[0][0]
  )

  brand = models.ForeignKey(Watch, on_delete=models.CASCADE)

  class Meta:
    ordering = ['-date']

def __str__(self):
    # Nice method for obtaining the friendly value of a Field.choice
  return f"{self.get_brand_display()} on {self.date}"

from django.db import models
from django.core.exceptions import ValidationError

class SpyCat (models.Model):

    name = models.CharField(max_length=100)
    years_of_experience = models.PositiveIntegerField()
    breed = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
    
class Mission(models.Model):
    cat = models.ForeignKey(SpyCat, on_delete=models.CASCADE, blank=True, null=True)
    complete = models.BooleanField(default=False)

    def clean(self):

        targets_number = self.targets.count()

        if targets_number < 1:
            raise ValidationError("Not able to have less than 1 target")
        elif targets_number > 3:
            raise ValidationError("More than 3 targets - not an option ")
        
    def delete(self, *using, **keep_parents ):
        if self.cat is not None:
            raise ValidationError ("We can't delete a mission while havening a cat assigned to it")
        super().delete(*using, **keep_parents)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)




class Target(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    notes = models.TextField()
    complete = models.BooleanField(default=False)
    mission = models.ForeignKey(Mission, on_delete=models.CASCADE, related_name='targets')



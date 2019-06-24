from django.db import models

# Create your models here.
class UserManager(models.Manager):
    def validate_trip_creation(self, postData):
        errors={}
        if len(postData['destination']) < 3:
            errors['destination_error'] = "At least 3 characters"
        if postData['start_date'] == "":
            errors['start_date_error'] = "Please select a date"
        elif datetime.strptime(postData['start_date'], '%Y-%m-%d') < datetime.today():
            errors['start_date_error'] = "Start date must be in the future. No time traveling!"
        if postData['end_date'] == "":
            errors['end_date_error'] = "Please select a date"
        elif datetime.strptime(postData['end_date'], '%Y-%m-%d') < datetime.strptime(postData['start_date'], '%Y-%m-%d'):
            errors['end_date_error'] = "End date must be after start date. No time traveling!"
        if len(postData['plan']) < 3:
            errors['plan_error'] = "At least 3 characters"
        return errors

    def process_trip_creation(self, postData, userid):
        user = User.objects.get(id=userid)
        trip_id = self.create(
            destination = postData['destination'],
            start_date = postData['start_date'],
            end_date = postData['end_date'],
            plan = postData['plan'],
            creator = user
        ).id
        return trip_id

    def update_trip(self, postData, trip_id):
        trip = self.get(id=trip_id)
        trip.destination = postData['destination']
        trip.start_date = postData['start_date']
        trip.end_date = postData['end_date']
        trip.plan = postData['plan']
        trip.save()
        return


class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=100)
    password_hash = models.CharField(max_length=255)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    objects = UserManager()

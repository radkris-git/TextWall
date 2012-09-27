from django.db import models

# Create your models here.
class Content(models.Model):
    paste_title = models.CharField(max_length=100)
    unique_hash_id = models.CharField(max_length=20)
    # Limit 50 KB
    content = models.CharField(max_length=50000)
    pasted_time = models.DateTimeField();

    def __unicode__(self):
        return str(self.id) + " " +self.unique_hash_id + " "+self.content + " "+ str(self.pasted_time)


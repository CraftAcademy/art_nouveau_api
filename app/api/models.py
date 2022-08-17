from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)

    # def __str__(self):
    #     return self.title

    # class Meta:
    #     ordering = ['-created_at']
    #     verbose_name = 'Project'
    #     verbose_name_plural = 'Projects'

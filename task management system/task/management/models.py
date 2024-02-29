from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class taskmodel(models.Model):
    STATUS_CHOICES = [
        ('complete', 'Complete'),
        ('incomplete', 'Incomplete'),
    ]
    Priority_choices = [('high','High'),('medium','Medium'),('low','Low')]
    title = models.CharField(max_length=200)
    description = models.TextField()
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')
    assigned_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='assigned_tasks',default = 6)
    priority = models.CharField(max_length = 100,choices=Priority_choices,default="Not Specified")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='incomplete')
    due_date = models.DateField()

    def time_remaining(self):
      
        today = datetime.now().date()
        remaining_time = self.due_date - today
        remaining_days = remaining_time.days
        return max(0, remaining_days)
        

    @property
    def time_remaining_days(self):
       
        return self.time_remaining()

    def __str__(self):
        return self.title
    

class Comment(models.Model):
    task = models.ForeignKey(taskmodel,on_delete=models.CASCADE, related_name = 'comments')
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return f"Comment by {self.user.username} on {self.task.title}"

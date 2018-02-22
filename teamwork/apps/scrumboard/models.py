from django.contrib.auth.models import User
from django.db import models


class Board(models.Model):
    tittle = models.CharField(max_length=100, default='')
    description = models.CharField(max_length=200, default='')
    owner = models.ForeignKey(
        User, related_name='owner', on_delete=models.CASCADE)
    members = models.ManyToManyField(
        User, related_name='users')

    # The Meta class provides some extra information about the ScrumBoard model.
    class Meta:
        # Verbose name is the same as class name in this case.
        verbose_name = "Scrum Boards"
        # Multiple Project objects are referred to as Projects.
        verbose_name_plural = "Scrum Boards"


    @staticmethod
    def get_my_scrums(user):
        """
        Gets a list of ScrumBoard objects. Used in views then passed to the template.
        """
        # #Gets membership and ownership object of current user
        mem = list(user.users.all())

        owner = list(user.owner.all())

        scrums = list(set(mem + owner))

        return scrums


class Column(models.Model):
    tittle = models.CharField(max_length=100, default='')
    description = models.CharField(max_length=200, default='')
    board = models.ForeignKey(Board, on_delete=models.CASCADE,
                              related_name="board", default=0)


class Task(models.Model):
    assigned = models.BooleanField(default=False)
    title = models.CharField(max_length=100, default='')
    description = models.CharField(max_length=400, default='')
    column = models.ForeignKey(Column, on_delete=models.CASCADE,
                               related_name="column", default=0)
    userID = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name="user", default=0)

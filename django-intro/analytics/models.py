from django.db import models

class Location(models.Model):
    id = models.CharField(max_length=45, primary_key=True)
    name = models.CharField(max_length=45)

    def __str__(self):
        s = "ID:%s NAME:%s" % (self.id, self.name)
        return self.id

    @classmethod
    def create(cls, id, name):
        if not Location.objects.get(name=name):
            l = cls(id=id, name=name)
            return l
        else:
            return "Already in the table"

class Search(models.Model):
    username = models.CharField(max_length=45, primary_key=True)
    counter = models.IntegerField()

    def __str__(self):
        s = "Username:%s\t;counter:%s" % (self.username, self.counter)
        return self.username


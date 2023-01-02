from django.db import models


class shows(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    releasedate = models.DateTimeField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


def add_show(title, network, releasedate, description):
    return shows.objects.create(title=title, network=network, releasedate=releasedate, description=description)


def get_showbyid(id):
    return shows.objects.get(id=id)


def get_all_shows():
    return shows.objects.all()


def delete_show(id):

    return shows.objects.get(id=id).delete()


def update_show(id, title, network, releasedate, description):
    show = shows.objects.get(id=id)
    show.title = title
    show.network = network
    show.releasedate = releasedate
    show.description = description
    show.save()
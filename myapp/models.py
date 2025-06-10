from django.db import models

class Service(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class GroupBacterie(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='groups')
    name = models.CharField(max_length=100)
    image1 = models.ImageField(upload_to='group_bacterie_images/', blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.service.name})"


class Bacterie(models.Model):
    group = models.ForeignKey(GroupBacterie, on_delete=models.CASCADE, related_name='bacteries')
    name = models.CharField(max_length=100)
    explanation = models.TextField()
    image1 = models.ImageField(upload_to='bacterie_images/', blank=True, null=True)
    image2 = models.ImageField(upload_to='bacterie_images/', blank=True, null=True)
    image3 = models.ImageField(upload_to='bacterie_images/', blank=True, null=True)
    image4 = models.ImageField(upload_to='bacterie_images/', blank=True, null=True)
    image5 = models.ImageField(upload_to='bacterie_images/', blank=True, null=True)
    image6 = models.ImageField(upload_to='bacterie_images/', blank=True, null=True)
    image7 = models.ImageField(upload_to='bacterie_images/', blank=True, null=True)
    image8 = models.ImageField(upload_to='bacterie_images/', blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.group.name})"

from django.db import models



class Sport_New(models.Model):
    name = models.CharField(max_length = 250)
    description = models.TextField()
    slug  = models.SlugField(max_length = 125, default = 'slug', unique = True)
    photo = models.ImageField(upload_to = "main_images/sports")
    turi = models.CharField(max_length=120,default = "turi")

    
    def get_image_url(self):
        if self.photo:
            return self.photo.url
        return " "


    def __str__(self):
        return f"{self.name} --> {self.turi}"


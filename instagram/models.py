# from django.db import models
# import datetime as dt
# from django.contrib.auth.models import User
# from tinymce.models import HTMLField

# # Create your models here.
# class Profile(models.Model):
#     profile_photo = models.ImageField(upload_to = 'images/', blank = True)
#     user = models.ForeignKey(User,on_delete = models.CASCADE,null=True)
#     bio = models.TextField(max_length = 100)

#     def save_profile(self):
#         self.save()

#     def delete_profile(self):
#         self.delete()

#     @classmethod
#     def update_profile(cls,profile,update):
#          updated = cls.objects.filter(Image_name=profile).update(name=update)
#          return updated

#     @classmethod
#     def search_by_username(cls,search_term):
#         instagram = cls.objects.filter(user__username=search_term)
#         return instagram

# class Image(models.Model):
#     image = models.ImageField(upload_to = 'images/', blank = True)
#     image_name = models.CharField(max_length = 30)
#     image_caption = models.TextField(max_length = 200)
#     profile = models.ForeignKey(User,on_delete = models.CASCADE,null=True)
#     pub_date = models.DateTimeField(auto_now_add=True)



#     def save_image(self):
#         self.save()

#     def delete_image(self):
#         self.delete()

#     @classmethod
#     def get_all(cls):
#         images = cls.objects.all()
#         return images

#     @classmethod
#     def get_image(cls, image_id):
#         image = cls.objects.get(id=image_id)
#         return image

# class Comment(models.Model):
#     comment_photo = models.ForeignKey(Image,on_delete = models.CASCADE, blank = True)
#     username = models.ForeignKey(User,on_delete = models.CASCADE)
#     comment = models.CharField(max_length = 400)


#     def save_comment(self):
#         self.save()

#     def delete_comment(self):
#         self.delete()

#     verbose_name_plural = "Categories"

#     def get_comments_by_images(cls, id):
#         comments = Comment.objects.filter(image_pk = id)
#         return comments
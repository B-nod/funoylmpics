from enum import Flag
from django.db import models
from django.utils.text import slugify
from user_profile.models import User


# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length = 150, unique = True)
    created_date = models.DateField(auto_now_add = True)
    slug = models.SlugField(null = True, blank = True)
    
    class Meta: 
        verbose_name = "Category"
        verbose_name_plural = "Categories"
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
        
    
        
    


# class Tag(models.Model):
#     title = models.CharField(max_length = 150)
#     created_date = models.DateField(auto_now_add = True)
#     slug = models.SlugField(null = True, blank = True)
    
#     def __str__(self):
#         return self.title
    
#     def save(self, *args, **kwargs):
#         self.slug = slugify(self.title)
#         super().save(*args, **kwargs)




class Blog(models.Model):
    user =models.ForeignKey(
        User,
        related_name = 'user_blogs',
        on_delete = models.CASCADE
        
    )
    category = models.ForeignKey(
        Category,
        related_name = 'category_blogs',
        on_delete = models.CASCADE
    )
    
    # tags = models.ManyToManyField(
    #     Tag,
    #     related_name= 'tag_blogs',
    #     blank = True
    # )
    title = models.CharField(
        max_length=250
    )
    slug = models.SlugField(null = True, blank = True)
    banner = models.ImageField(
        upload_to = 'video_banners'
    )
    posted_date = models.DateField(auto_now_add=True)
    descriptions = models.TextField()
    video = models.FileField(
        upload_to="video/%y"
    )
    likes = models.ManyToManyField(
        User,
        related_name = 'user_likes',
        blank = True
    )
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    

class Comment(models.Model):
    user =models.ForeignKey(
        User,
        related_name = 'user_comments',
        on_delete = models.CASCADE
        
    )
    
    blog =models.ForeignKey(
        Blog,
        related_name = 'blog_comments',
        on_delete = models.CASCADE
        
    )
    text = models.TextField()
    created_date = models.DateField(auto_now_add = True)
    
    def __str__(self):
        return self.text
    
    
    
class Reply(models.Model):
    user =models.ForeignKey(
        User,
        related_name = 'user_reply',
        on_delete = models.CASCADE
        
    )
    
    reply =models.ForeignKey(
        Comment,
        related_name = 'comment_replies',
        on_delete = models.CASCADE
        
    )
    text = models.TextField()
    created_date = models.DateField(auto_now_add = True)
    
    def __str__(self):
        return self.text
    
    class Meta: 
        verbose_name = "Reply"
        verbose_name_plural = "Replies"
        
        
        
class Country(models.Model):
    country = models.CharField(max_length=250)
    flag = models.ImageField(
        upload_to = 'country_flag',
        null = True
    )
    def __str__(self):
        return self.country
    
    def get_country_picture(self):
        url = ""
        try:
            url = self.flag.url
        except:
            url = ""
        return url
    
    
    class Meta: 
        verbose_name = "Country"
        verbose_name_plural = "Countries"   
        
class ScoreBoard(models.Model):
    category = models.ForeignKey(
        Category,
        related_name = 'score_category',
        on_delete = models.CASCADE
    )
    country_a = models.ForeignKey(
        Country,
        related_name = 'country_a',
        on_delete = models.CASCADE        
    )
    
    country_b = models.ForeignKey(
        Country,
        related_name = 'country_b',
        on_delete = models.CASCADE        
    )
    score_a = models.FloatField()
    score_b= models.FloatField()
    
    def __str__(self):
        return ("{}:{} | {}:{}".format(self.country_a, self.score_a,self.country_b, self.score_b))
    
    
    
    
    
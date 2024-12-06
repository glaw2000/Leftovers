from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

class Ingredient(models.Model):
    """
    Stores a list of main ingredients for each Post model by Post ID
    """
    INGREDIENT_CHOICES = [
        (0, "any"),
        (1, "meat"),
        (2, "fish"),
        (3, "veg"),
        (4, "fruit"),
        (5, "dairy"),
        (6, "eggs"),
        (7, "bread"),
        (8, "grains"),
    ]
    
    ingredient = models.IntegerField(choices=INGREDIENT_CHOICES, default=0)

    def __str__(self):
        return self.get_ingredient_display()

class Post(models.Model):
    """
    Stores a single blog post entry related to User model by author ID.
    """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    fk_author_id = models.ForeignKey( 
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    content = models.TextField()
    excerpt = models.TextField(blank=True)
    ingredients = models.ManyToManyField(Ingredient, related_name="posts")
    image = CloudinaryField('image', default='placeholder')
    alt_image =models.CharField(max_length=200)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_on"]
    def __str__(self):
        return f"The title of this post is {self.title}"

class Comment(models.Model):
    """
    Stores a single comment related to Post model by Post ID and User model by User Id.
    """
    fk_post_id = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    fk_user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="commenter")
    remark = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_on"]
    def __str__(self):
        return f"Comment {self.remark} by {self.fk_user_id}"

from django.shortcuts import render, get_object_or_404, reverse
from django.views.generic import ListView
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, JsonResponse
from .models import Post, Comment, Like, Ingredient
from .forms import CommentForm

# Create your views here.

class AllPosts(ListView):
    """
    Displays listing of all posts, filtered by ingredient if specified
    """
    model = Post
    template_name = 'blog/blog.html'
    context_object_name = 'items'
    paginate_by = 9

    # Map ingredient names to their respective integer values
    ingredient_mapping = {
        'any': 0,
        'meat': 1,
        'fish': 2,
        'veg': 3,
        'fruit': 4,
        'dairy': 5,
        'eggs': 6,
        'bread': 7,
        'grains': 8,
        'seasonal': 9
    }
    def get_queryset(self):
        ingredient = self.kwargs.get('ingredient', 'any').lower()
        # Get the corresponding integer value for the ingredient
        ingredient_value = self.ingredient_mapping.get(ingredient, 0)  # Default to 'any' (0)
        
        if ingredient_value == 0:  # 'any' selected, show all posts
            return Post.objects.all().order_by("-created_on")
        else:
            return Post.objects.filter(ingredients__ingredient=ingredient_value).order_by("-created_on")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        ingredient = self.kwargs.get('ingredient', 'any').capitalize()
        context['current_ingredient'] = ingredient
        return context

def post_detail(request, slug):
    """
    Display an individual post :model:`blog.Post`.

    **Context**

    ``post``
        An instance of :model:`blog.Post`.

    **Template:**

    :template:`blog/post_detail.html`
    """

    queryset = Post.objects.all()
    post = get_object_or_404(queryset, slug=slug)
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.filter(approved=True).count()
    user_has_liked = post.likes.filter (fk_user_id=request.user).exists() if request.user.is_authenticated else False
    
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.fk_user_id = request.user
            comment.fk_post_id = post
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Your comment has been submitted and is awaiting approval'
                )

    comment_form = CommentForm()
    

    return render(
        request,
        "blog/post_detail.html",
        {
            "post": post,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
            "user_has_liked":user_has_liked,
        },
    )

    

@login_required
def like_post(request, slug):
    """
    Toggles a like icon for post
    **Context**

    ``post``
        An instance of :model:`blog.Post`.
    ``like``
        A like related to the post.
    """
    post = get_object_or_404(Post, slug=slug)
    like, created = Like.objects.get_or_create(fk_post_id=post, fk_user_id = request.user)
    if not created:
        like.delete()
        liked=False
    else:
        liked=True
    likes_count = post.likes.count()
    return JsonResponse({
        'liked':liked,
        'like_count':likes_count
    })

def comment_edit(request, slug, comment_id):
    """
    Display an individual comment for edit.

    **Context**

    ``post``
        An instance of :model:`blog.Post`.
    ``comment``
        A single comment related to the post.
    ``comment_form``
        An instance of :form:`blog.CommentForm`.
    """
    if request.method == "POST":

        queryset = Post.objects.all()
        post = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.fk_user_id == request.user:
            comment = comment_form.save(commit=False)
            comment.fk_post_id = post
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating comment!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))

def comment_delete(request, slug, comment_id):
    """
    Delete an individual comment.
        
    **Context**

    ``post``
        An instance of :model:`blog.Post`.
    ``comment``
        A single comment related to the post.   
    """
    queryset = Post.objects.all()
    post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.fk_user_id == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))
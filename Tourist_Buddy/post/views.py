from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponseRedirect

from post.models import Post, Tag, Follow, Stream, Likes
from django.contrib.auth.models import User
from post.forms import NewPostform
from users.models import Profile
from django.urls import resolve
from django.core.paginator import Paginator

from django.db.models import Q

# Create your views here.
def post(request):
    user = request.user
    if request.user.is_authenticated:
        try:
            posts = Stream.objects.filter(user=user)
        except user.DoesNotExist:
            user=None
    else:
        user=None
    group_ids = []
    
    if request.user.is_authenticated:
        try:
            for post in posts:
                group_ids.append(post.post_id)
        except:
            posts=None
    else:
        posts=None
        
    post_items = Post.objects.filter(id__in=group_ids).all().order_by('-posted')
    context = {
        'post_items': post_items,
        #'follow_status': follow_status,
        #'profile': profile,
        #'all_users': all_users,
        # 'users_paginator': users_paginator,
    }
    return render(request, 'post/post.html',context)

def NewPost(request):
    user = request.user.id
    tags_objs = []
    
    if request.method == "POST":
        form = NewPostform(request.POST, request.FILES)
        if form.is_valid():
            picture = form.cleaned_data.get('picture')
            caption = form.cleaned_data.get('caption')
            tag_form = form.cleaned_data.get('tags')
            tag_list = list(tag_form.split(','))

            for tag in tag_list:
                t, created = Tag.objects.get_or_create(title=tag)
                tags_objs.append(t)
            p, created = Post.objects.get_or_create(picture=picture, caption=caption, user_id=user)
            #tags_obj.append
            p.tags.set(tags_objs)
            p.save()
            return redirect('post')
    else:
        form = NewPostform()
    context = {
        'form': form
    }
    return render(request, 'post/newpost.html', context)

# def PostDetail(request, post_id):
#     # user = request.user
#     post = get_object_or_404(Post, id=post_id)
#     # comments = Comment.objects.filter(post=post).order_by('-date')

#     # if request.method == "POST":
#     #     form = CommentForm(request.POST)
#     #     if form.is_valid():
#     #         comment = form.save(commit=False)
#     #         comment.post = post
#     #         comment.user = request.user
#     #         comment.save()
#     #         return HttpResponseRedirect(reverse('post-details', args=[post.id]))
#     # else:
#     #     form = CommentForm()

#     context = {
#         'post': post,
#         # 'form': form,
#         # 'comments': comments
#     }

#     return render(request, 'post/postdetail.html', context)

def Tags(request, tag_slug):
    tag = get_object_or_404(Tag, slug=tag_slug)
    posts = Post.objects.filter(tags=tag).order_by('-posted')

    context = {
        # 'posts': posts,
        'tag': tag

    }
    return render(request, 'post/tag.html', context)


def like(request, post_id):
    user = request.user
    post = Post.objects.get(id=post_id)
    current_likes = post.likes
    liked = Likes.objects.filter(user=user, post=post).count()

    if not liked:
        Likes.objects.create(user=user, post=post)
        current_likes = current_likes + 1
    else:
        Likes.objects.filter(user=user, post=post).delete()
        current_likes = current_likes - 1
        
    post.likes = current_likes
    post.save()
    # return HttpResponseRedirect(reverse('post-details', args=[post_id]))
    return HttpResponseRedirect(reverse('post', args=[post_id]))
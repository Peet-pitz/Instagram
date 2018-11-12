from django.shortcuts import render,redirect,get_object_or_404
from django.http  import HttpResponse,Http404
from .models import Image,Profile,Comment
from django.core.exceptions import ObjectDoesNotExist
from .email import send_welcome_email
from django.contrib.auth.decorators import login_required
from .forms import NewImageForm,NewProfileForm,NewCommentForm

# Create your views here.
def welcome(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit = False)
            profile.user = current_user
            profile.save()
        return redirect('insta-Profile')
    else:
        form = NewProfileForm()
    return render(request,'welcome.html',{'form':form})

@login_required(login_url='/accounts/login/')
def instagram(request):
    photos = Image.get_all()
    return render(request,'all-photos/post.html',{'photos':photos})

def image(request,image_id):
    try:
        image = Image.objects.get(id = image_id)
    except ObjectDoesNotExist:
        raise Http404()
    return render(request,'all-photos/image.html',{'image':image})

@login_required(login_url='/accounts/login/')
def new_image(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit = False)
            image.profile = current_user
            image.save()
        return redirect('instaToday')
    else:
        form = NewImageForm()
    return render(request,'new_image.html', {'form':form})

# def profile(request):
#     current_user = request.user
#     image = Image.objects.filter(profile = current_user)

#     try:
#         # profile = get_object_or_404(Profile,user=current_user)
#         profile = Profile.objects.get(user=current_user)
#     except ObjectDoesNotExist:
#         return redirect('welcome')
#     print(profile.bio)
#     return render(request,'profile.html',{ 'profile':profile,'image':image,'current_user':current_user})

# def edit_profile(request):
#     current_user = request.user
#     if request.method == 'POST':
#         form = NewProfileForm(request.POST, request.FILES)
#         if form.is_valid():
#             profile = form.save(commit = False)
#             profile.profile = current_user
#             profile.save()
#         return redirect('profile')
#     else:
#         form = NewProfileForm()
#     return render(request,'edit_profile.html', {'form':form})

# def search_results(request):

#     if 'profile' in request.GET and request.GET["profile"]:
#         search_term = request.GET.get("profile")
#         searched_profile = Profile.search_by_username(search_term)
#         message = f"{search_term}"

#         return render(request, 'all-photos/search.html',{"message":message,"profiles": searched_profile})

#     else:
#         message = "You haven't searched for any term"
#         return render(request, 'all-photos/search.html',{"message":message})

# def search_profile(request,profile_id):
#     try :
#         profile = Profile.objects.get(id = profile_id)

#     except ObjectDoesNotExist:
#         # raise Http404()
#         return render(request, 'all-photos/no_profile.html')

#     return render(request, 'all-photos/search_profile.html', {'profile':profile})

# def comment_photo(request, image_id):
#     current_user = request.user
#     if request.method == 'POST':
#         form = NewCommentForm(request.POST, request.FILES)
#         image = get_object_or_404(Image, pk = image_id)
#         if form.is_valid():
#             comment = form.save(commit = False)
#             comment.comment = current_user
#             comment.image = image
#             comment.save()
#         return redirect('comment-photo')
#     else:
#         form = NewCommentForm()
#     return render(request,'comment.html', {'form':form})
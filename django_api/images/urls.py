from django.conf.urls import url

from . import views

app_name = 'images'
urlpatterns = [
    url(
        regex=r'^images_all/$',
        view=views.ListAllImages.as_view(),
        name='all_images'
    ),
    url(
        regex=r'^comments_all/$',
        view=views.ListAllComments.as_view(),
        name='all_images'
    ),
    url(
        regex=r'^likes_all/$',
        view=views.ListAllLikes.as_view(),
        name='all_images'
    ),
]
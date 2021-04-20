from django.urls import path
from .views import index,search_data,get_behance_images

app_name = "freelancer_profile"
urlpatterns = [
    path("", view=index, name="home"),
    path("search/", view=search_data, name="search"),
    path("images/<int:id>/", view=get_behance_images, name="get_image"),

]

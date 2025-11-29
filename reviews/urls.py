from django.urls import path
from . import views

urlpatterns = [
    path("", views.ReviewViewss.as_view()),
    path("thanks/", views.Thanks.as_view(), name="thanks"),
    path("list-reviews/",views.ListReviews.as_view(), name='listreviews'),
    path("list-reviews/liked_id/",views.AddLikeView.as_view()),
    path("list-reviews/<int:pk>/",views.SingleReview.as_view(),name='singlereview')
]



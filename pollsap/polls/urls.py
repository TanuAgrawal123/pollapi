from django.urls import path

from .apiviews import PollViewSet, ChoiceList, CreateVote
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register('polls', PollViewSet, base_name='polls')

app_name='polls'
urlpatterns=[
path("polls/<int:pk>/choices/", ChoiceList.as_view(), name='choice_list'),
path("polls/<int:pk>/choices/<int:choice_pk>/vote/", CreateVote.as_view(), name='create_vote'),]
urlpatterns+=router.urls
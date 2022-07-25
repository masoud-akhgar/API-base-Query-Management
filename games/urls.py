from django.urls import path
from rest_framework import views
from games import views as app_view


urlpatterns = [
    path('gamesRank/<int:rank>', app_view.ShowGamesByRanking.as_view()),
    path('gamesName/<str:name>', app_view.ShowGamesByName.as_view()),
    path('bestGame/', app_view.NbestGameinEveryYear.as_view()),
    path('fiveBestGame/', app_view.FiveBestGameForOnePlatformInParticularYear.as_view()),
    path('euGTna/', app_view.EuGtNa.as_view()),
    path('comparison/<str:name_game1>/<str:name_game2>', app_view.ComparisonTwoGames.as_view()),
    path('totalsales/<int:yearOne>/<int:yearTwo>', app_view.TotalSalesEachYear.as_view()),
    path('comparisonpublisher/<int:yearOne>/<int:yearTwo>/<str:publisherOne>/<str:publisherTwo>', app_view.TotalSalesBetweenPublisherEachYear.as_view()),
    path('totalsalesGenre/<int:yearOne>/<int:yearTwo>',app_view.TotalSalesBetweenGenreEachYear.as_view()),
]
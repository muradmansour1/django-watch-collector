from django.urls import path
from .views import Home, WatchList, WatchDetail, BrandListCreate, BrandDetail, BandList, BandDetail # additional imports

urlpatterns = [
  path('', Home.as_view(), name='home'),
  # new routes below 
  path('Watch/', WatchList.as_view(), name='Watch-list'),
  path('Watch/<int:id>/', WatchDetail.as_view(), name='Watch-detail'),
  path('Watch/<int:watch_id>/brand/', BrandListCreate.as_view(), name='brand-list-create'),
	path('Watch/<int:watch_id>/brand/<int:id>/', BrandDetail.as_view(), name='brand-detail'),
  path('band/', BandList.as_view(), name='band-list'),
  path('band/<int:id>/', BandDetail.as_view(), name='band-detail'),
]



from django.urls import path
from .views import Home, WatchList, WatchDetail, BrandListCreate, BrandDetail, BandList, BandDetail, AddBandToWatch # additional imports

urlpatterns = [
  path('', Home.as_view(), name='home'),
  # new routes below 
  path('watch/', WatchList.as_view(), name='Watch-list'),
  path('watch/<int:id>/', WatchDetail.as_view(), name='Watch-detail'),
  path('watch/<int:watch_id>/brand/', BrandListCreate.as_view(), name='brand-list-create'),
	path('watch/<int:watch_id>/brand/<int:id>/', BrandDetail.as_view(), name='brand-detail'),
  path('band/', BandList.as_view(), name='band-list'),
  path('band/<int:id>/', BandDetail.as_view(), name='band-detail'),
  path('watch/<int:watch_id>/add_band/<int:band_id>/', AddBandToWatch.as_view(), name='add-band-to-watch'),
]



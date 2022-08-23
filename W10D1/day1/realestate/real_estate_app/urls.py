
from .views import about, dashboard, home, listing, listing2, listing3, listing4, listing5, listing6, listings, register, search
from django.urls import path

urlpatterns = [
   path("", home,name= 'home'),
   path("listing", listing, name='listing'),
   path("about",about, name='about'),
   path("search", search, name='search'),
   path("register", register, name="register"),
   path("dashboard", dashboard, name='dashboard'),
   path("listings", listings, name='listings'),
   path("listingtwo", listing2, name='listingtwo'),
   path("listingthree", listing3, name='listingthree'),
   path("listingfour", listing4, name='listingfour'),
   path("listingfive", listing5, name='listingfive'),
   path("listingsix", listing6, name='listingsix'),



]
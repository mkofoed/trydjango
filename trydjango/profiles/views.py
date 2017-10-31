from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.views.generic import DetailView
from django.contrib.auth import get_user_model
# Create your views here.

from menus.models import Item
from restaurants.models import RestaurantLocation

User = get_user_model()

class ProfileDetailView(DetailView):
    # queryset = User.objects.filter(is_active=True)
    template_name = 'profiles/user.html'

    def get_object(self):
        username = self.kwargs.get('username')
        if username is None:
            raise Http404
        return get_object_or_404(User, username__iexact=username, is_active=True)

    def get_context_data(self, *args, **kwargs):
        context = super(ProfileDetailView, self).get_context_data(*args, **kwargs)
        # Getting user from the model - i.e. the instance's user
        user = context['user']
        # Checking if user has any Items
        query = self.request.GET.get('q')
        items_exist = Item.objects.filter(user=user).exists()
        # Searching for RestaurantLocation with the given user
        qs = RestaurantLocation.objects.filter(owner=user)
        if query:
            qs = qs.search(query)
        if items_exist and qs.exists():
            context['locations'] = qs
        return context

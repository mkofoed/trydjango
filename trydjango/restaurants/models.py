from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save, post_save
from django.core.urlresolvers import reverse

from .utils import unique_slug_generator
from .validators import validate_category

# Create your models here.

User = settings.AUTH_USER_MODEL


class RestaurantLocationQueryset(models.query.QuerySet):
    def search(self, query):
        return self.filter(name__icontains=query)


class RestaurantLocationManager(models.Manager):
    def get_queryset(self):
        return RestaurantLocationQueryset(self.model, using=self._db)

    def search(self, query):
        return self.get_queryset().search(query)


class RestaurantLocation(models.Model):
    owner           = models.ForeignKey(User) # class_instance.model_set.all()
    name            = models.CharField(max_length=120)
    location        = models.CharField(max_length=120, null=True, blank=True)
    category        = models.CharField(max_length=120, null=True, blank=True, validators=[validate_category])
    timestamp       = models.DateTimeField(auto_now_add=True)
    updated         = models.DateTimeField(auto_now=True)
    slug            = models.SlugField(null=True, blank=True)
    #my_date_field   = models.DateField(auto_now=False, auto_now_add=False)

    objects = RestaurantLocationManager() # Adding Model.objects.all()

    def __str__(self):
        return self.name.title()

    def get_absolute_url(self):
        return reverse('restaurants:detail', kwargs={'slug': self.slug})

    @property
    def title(self):
        return self.name


def rl_pre_save_receiver(sender, instance, *args, **kwargs):
    # print(sender)
    # print(instance)
    instance.name = instance.name.title()
    if instance.category:
        instance.category = instance.category.title()
    if instance.location:
        instance.location = instance.location.title()
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


#def rl_post_save_receiver(sender, instance, created, *args, **kwargs):
#    print('saved!')
#    print(instance.timestamp)

pre_save.connect(rl_pre_save_receiver, sender=RestaurantLocation)

#post_save.connect(rl_post_save_receiver, sender=RestaurantLocation)

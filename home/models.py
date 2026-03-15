from django.db import models
from wagtail.models import Page, Orderable
from wagtail.admin.panels import FieldPanel, InlinePanel, MultiFieldPanel
from modelcluster.fields import ParentalKey
from wagtail.admin.panels import PageChooserPanel


class FeaturedCar(Orderable):
    page = ParentalKey('HomePage', related_name='featured_cars')
    car_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    car_name = models.CharField(max_length=100)

    panels = [
        FieldPanel('car_image'),
        FieldPanel('car_name'),
    ]

class HomePage(Page):
    hero_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    explore_page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    hero_caption = models.CharField(
        max_length=255, 
        default="Cars are a different experience"
    )

    showroom_address = models.TextField(blank=True)

    content_panels = Page.content_panels + [
        PageChooserPanel('explore_page', 'cars.CarIndexPage'),
        MultiFieldPanel([
            FieldPanel('hero_image'),
            FieldPanel('hero_caption'),
        ], heading="Hero Section"),
        InlinePanel('featured_cars', label="Featured Cars", max_num=3),
        FieldPanel('showroom_address'),
    ]
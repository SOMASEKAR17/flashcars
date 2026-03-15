from django.db import models
from wagtail.models import Page
from wagtail.admin.panels import FieldPanel
from wagtail.images.models import Image

class CarIndexPage(Page):
    """The 'Explore Cars' list page"""
    intro = models.TextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro'),
    ]

    def get_context(self, request):
        context = super().get_context(request)
        context['cars'] = CarPage.objects.live().child_of(self).order_by('-first_published_at')
        return context

class CarPage(Page):
    """Individual Car Detail Page"""
    brand = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    car_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    specifications = models.TextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('brand'),
        FieldPanel('price'),
        FieldPanel('car_image'),
        FieldPanel('specifications'),
    ]
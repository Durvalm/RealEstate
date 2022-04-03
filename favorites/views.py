from django.shortcuts import render, redirect, get_object_or_404
from houses.models import Property
from .models import Favorite, Page
# Create your views here.


def _page_id(request):
    """This function gets a session id from the cookies in a website"""
    page = request.session.session_key
    if not page:
        page = request.session.create()
    return page


def add_fav(request, id):
    """This function goes to the anchor tag in the favorite button in the property.html file to add
    a property in the favorites list"""
    property = Property.objects.get(id=id)

    try:
        page = Page.objects.get(page_id=_page_id(request))
    except Page.DoesNotExist:
        page = Page.objects.create(
            page_id=_page_id(request),
        )
    page.save()

    try:
        fav_property = Favorite.objects.get(property=property, page=page)
        fav_property.save()
    except Favorite.DoesNotExist:
        fav_property = Favorite.objects.create(
            property=property,
            page=page,
        )
        fav_property.save()

    return redirect('favorites')


def remove_fav(request, id):
    """This function goes to the anchor tag in the favorite button in the favorite.html file
    and removes a property from the list"""

    page = Page.objects.get(page_id=_page_id(request))
    property = get_object_or_404(Property, id=id)

    fav_property = Favorite.objects.get(page=page, property=property)
    fav_property.delete()
    return redirect('favorites')



def favorites(request, fav_properties=None):
    """Main function which passes data to the html file"""
    try:
        page = Page.objects.get(page_id=_page_id(request))
        fav_properties = Favorite.objects.filter(page=page)

    except Exception:
        pass

    context = {
        'fav_properties': fav_properties,
    }
    return render(request, 'favorites.html', context)



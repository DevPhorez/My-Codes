                    #-----------views codes-----------#
# views for main page
color = request.GET.get('color')
sort = request.GET.get('sorted')
size = request.GET.get('size')
price_min = request.GET.get('min')
price_max = request.GET.get('max')

order = None
if sort == 'cheapest':
    order = 'price'
elif sort == 'latest':
    order = '-id'
elif sort == 'popularity':
    order = '-view_count'

if (sort and color and size and price_min and price_max) is not None:
    return Products.objects.get_color_size_price_sorting(color, size, price_min, price_max, order)
elif (sort and color and size) is not None:
    return Products.objects.get_color_size_sorting(color, size, order)
elif (sort and size) is not None:
    return Products.objects.get_color_sorting(color, order)
elif (sort and size) is not None:
    return Products.objects.get_size_sorting(size, order)
elif (color and size) is not None:
    return Products.objects.get_color_size(color, size)
elif (sort and price_min and price_max) is not None:
    return Products.objects.get_price_sorting(price_min, price_max, order)
elif (color and price_min and price_max) is not None:
    return Products.objects.get_color_price(color, price_min, price_max)
elif (size and price_min and price_max) is not None:
    return Products.objects.get_size_price(size, price_min, price_max)
elif color is not None:
    return Products.objects.get_color(color)
elif sort is not None:
    return Products.objects.is_active().order_by(f'{order}')
elif size is not None:
    return Products.objects.get_size(size)
elif (price_min and price_max) is not None:
    return Products.objects.get_price(price_min, price_max)
elif (price_min or price_max) is not None:
    raise Http404('')
else:
    return Products.objects.is_active()


# views for search page
query = request.GET.get('q')
color = request.GET.get('color')
sort = request.GET.get('sorted')
size = request.GET.get('size')
price_min = request.GET.get('min')
price_max = request.GET.get('max')

order = None
if sort == 'cheapest':
    order = 'price'
elif sort == 'latest':
    order = '-id'
elif sort == 'popularity':
    order = '-view_count'

if (sort and color and size and price_min and price_max) is not None:
    return Products.objects.search_color_size_price_sorting(color, size, price_min, price_max, order, query)
elif (sort and size and price_min and price_max) is not None:
    return Products.objects.search_size_price_sorting(size, price_min, price_max, sort, query)
elif (sort and color and size) is not None:
    return Products.objects.search_color_size_sorting(color, size, order, query)
elif (sort and size) is not None:
    return Products.objects.search_size_sorting(size, order, query)
elif (color and size) is not None:
    return Products.objects.search_color_size(color, size, query)
elif (sort and price_min and price_max) is not None:
    return Products.objects.search_price_sorting(price_min, price_max, order, query)
elif (color and price_min and price_max) is not None:
    return Products.objects.search_color_price(color, price_min, price_max, query)
elif (size and price_min and price_max) is not None:
    return Products.objects.search_size_price(size, price_min, price_max, query)
elif color is not None:
    return Products.objects.search_color(color, query)
elif sort is not None:
    return Products.objects.search(query).order_by(f'{order}')
elif size is not None:
    return Products.objects.search_size(size, query)
elif (price_min and price_max) is not None:
    return Products.objects.search_price(price_min, price_max, query)
elif (price_min or price_max) is not None:
    raise Http404('')
else:
    return Products.objects.search(query)

# views codes
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

# models codes
def get_color_size_price_sorting(self, COLOR, SIZE, PRICE_MIN, PRICE_MAX, SORT_BY):
    return self.get_queryset().filter(color=COLOR, size=SIZE, price__range=(PRICE_MIN, PRICE_MAX)).order_by(f'{SORT_BY}')

def get_price_sorting(self, PRICE_MIN, PRICE_MAX, SORT_BY):
    return self.get_queryset().filter(price__range=(PRICE_MIN, PRICE_MAX)).order_by(f'{SORT_BY}')

def get_color_price(self, COLOR, PRICE_MIN, PRICE_MAX):
    return self.get_queryset().filter(color=COLOR, price__range=(PRICE_MIN, PRICE_MAX))

def get_size_price(self, SIZE, PRICE_MIN, PRICE_MAX):
    return self.get_queryset().filter(size=SIZE, price__range=(PRICE_MIN, PRICE_MAX))

def get_price(self, PRICE_MIN, PRICE_MAX):
    return self.get_queryset().filter(price__range=(PRICE_MIN, PRICE_MAX))

def get_color_size_sorting(self, COLOR, SIZE, SORT_BY):
    if COLOR == '2' and SIZE == '6':
        return self.get_queryset().filter(active=True).order_by(f'{SORT_BY}')
    elif COLOR == '2':
        return self.get_queryset().filter(size=SIZE, active=True).order_by(f'{SORT_BY}')
    elif SIZE == '6':
        return self.get_queryset().filter(color=COLOR, active=True).order_by(f'{SORT_BY}')
    return self.get_queryset().filter(color=COLOR, size=SIZE).order_by(f'{SORT_BY}')

def get_color_size(self, COLOR, SIZE):
    return self.get_queryset().filter(color=COLOR, size=SIZE)

def get_size_sorting(self, SIZE, SORT_BY):
    return self.get_queryset().filter(size=SIZE).order_by(f'{SORT_BY}')

def get_size(self, SIZE):
    if SIZE == '6':
        return self.get_queryset().filter(active=True)
    return self.get_queryset().filter(size=SIZE)

def get_color_sorting(self, COLOR, SORT_BY):
    if COLOR == '2':
        return self.get_queryset().filter(active=True).order_by(f'{SORT_BY}')
    return self.get_queryset().filter(color=COLOR).order_by(f'{SORT_BY}')

def get_color(self, COLOR):
    if COLOR == '2':
        return self.get_queryset().filter(active=True)
    return self.get_queryset().filter(color=COLOR)
if COLOR == '2':
    return self.get_queryset().filter(active=True)
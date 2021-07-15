# views codes
color = request.GET.get('color')
sort = request.GET.get('sorted')
size = request.GET.get('size')

order = None
if sort == 'cheapest':
    order = 'price'
elif sort == 'latest':
    order = '-id'
elif sort == 'popularity':
    order = '-view_count'

if sort is not None and color is not None and size is not None:
    return Products.objects.get_color_size_sorting(color, size, order)
elif sort is not None and color is not None:
    return Products.objects.get_color_sorting(color, order)
elif sort is not None and size is not None:
    return Products.objects.get_size_sorting(size, order)
elif color is not None and size is not None:
    return Products.objects.get_color_size(color, size)
elif color is not None:
    return Products.objects.get_color(color)
elif sort is not None:
    return Products.objects.is_active().order_by(f'{order}')
elif size is not None:
    return Products.objects.get_size(size)
else:
    return Products.objects.is_active()

# models codes
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
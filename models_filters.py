                    #-----------models codes-----------#
# model for search page 
def search_color_size_price_sorting(self, COLOR, SIZE, PRICE_MIN, PRICE_MAX, SORT_BY, QUERY):
    lookup = (
        Q(title__icontains= QUERY) |
        Q(short_description__icontains= QUERY) |
        Q(long_description__icontains= QUERY)
    )

    return self.get_queryset().filter(lookup, color=COLOR, size=SIZE, price__range=(PRICE_MIN, PRICE_MAX)).order_by(f'{SORT_BY}').distinct()

def search_price_sorting(self, PRICE_MIN, PRICE_MAX, SORT_BY, QUERY):
    lookup = (
        Q(title__icontains= QUERY) |
        Q(short_description__icontains= QUERY) |
        Q(long_description__icontains= QUERY)
    )

    return self.get_queryset().filter(lookup, price__range=(PRICE_MIN, PRICE_MAX)).order_by(f'{SORT_BY}').distinct()

def search_color_price(self, COLOR, PRICE_MIN, PRICE_MAX, QUERY):
    lookup = (
        Q(title__icontains= QUERY) |
        Q(short_description__icontains= QUERY) |
        Q(long_description__icontains= QUERY)
    )

    return self.get_queryset().filter(lookup, color=COLOR, price__range=(PRICE_MIN, PRICE_MAX)).distinct()

# have to fix it
def search_size_price_sorting(self, SIZE, PRICE_MIN, PRICE_MAX, SORT_BY, QUERY):
    lookup = (
        Q(title__icontains= QUERY) |
        Q(short_description__icontains= QUERY) |
        Q(long_description__icontains= QUERY)
    )

    return self.get_queryset().filter(lookup, size=SIZE, price__range=(PRICE_MIN, PRICE_MAX)).distinct()#.order_by(f'{SORT_BY}')

def search_size_price(self, SIZE, PRICE_MIN, PRICE_MAX, QUERY):
    lookup = (
        Q(title__icontains= QUERY) |
        Q(short_description__icontains= QUERY) |
        Q(long_description__icontains= QUERY)
    )
    
    return self.get_queryset().filter(lookup, size=SIZE, price__range=(PRICE_MIN, PRICE_MAX)).distinct()

def search_price(self, PRICE_MIN, PRICE_MAX, QUERY):
    lookup = (
        Q(title__icontains= QUERY) |
        Q(short_description__icontains= QUERY) |
        Q(long_description__icontains= QUERY)
    )

    return self.get_queryset().filter(lookup, price__range=(PRICE_MIN, PRICE_MAX)).distinct()

def search_color_size_sorting(self, COLOR, SIZE, SORT_BY, QUERY):
    lookup = (
        Q(title__icontains= QUERY) |
        Q(short_description__icontains= QUERY) |
        Q(long_description__icontains= QUERY)
    )

    if COLOR == '2' and SIZE == '6':
        return self.get_queryset().filter(lookup, active=True).order_by(f'{SORT_BY}').distinct()
    elif COLOR == '2':
        return self.get_queryset().filter(lookup, size=SIZE, active=True).order_by(f'{SORT_BY}').distinct()
    elif SIZE == '6':
        return self.get_queryset().filter(lookup, color=COLOR, active=True).order_by(f'{SORT_BY}').distinct()
    return self.get_queryset().filter(lookup, color=COLOR, size=SIZE).order_by(f'{SORT_BY}').distinct()

def search_color_size(self, COLOR, SIZE, QUERY):
    lookup = (
        Q(title__icontains= QUERY) |
        Q(short_description__icontains= QUERY) |
        Q(long_description__icontains= QUERY)
    )

    return self.get_queryset().filter(lookup, color=COLOR, size=SIZE).distinct()

def search_size_sorting(self, SIZE, SORT_BY, QUERY):
    lookup = (
        Q(title__icontains= QUERY) |
        Q(short_description__icontains= QUERY) |
        Q(long_description__icontains= QUERY)
    )

    return self.get_queryset().filter(lookup, size=SIZE).order_by(f'{SORT_BY}').distinct()

def search_size(self, SIZE, QUERY):
    lookup = (
        Q(title__icontains= QUERY) |
        Q(short_description__icontains= QUERY) |
        Q(long_description__icontains= QUERY)
    )

    if SIZE == '6':
        return self.get_queryset().filter(lookup, active=True).distinct()
    return self.get_queryset().filter(lookup, size=SIZE).distinct()

def search_color_sorting(self, COLOR, SORT_BY, QUERY):
    lookup = (
        Q(title__icontains= QUERY) |
        Q(short_description__icontains= QUERY) |
        Q(long_description__icontains= QUERY)
    )

    if COLOR == '2':
        return self.get_queryset().filter(lookup, active=True).order_by(f'{SORT_BY}').distinct()
    return self.get_queryset().filter(lookup, color=COLOR).order_by(f'{SORT_BY}').distinct()

def search_color(self, COLOR, QUERY):
    lookup = (
        Q(title__icontains= QUERY) |
        Q(short_description__icontains= QUERY) |
        Q(long_description__icontains= QUERY)
    )

    if COLOR == '2':
        return self.get_queryset().filter(lookup, active=True).distinct()
    return self.get_queryset().filter(lookup, color=COLOR).distinct()

def search(self, QUERY):
    lookup = (
        Q(title__icontains= QUERY) |
        Q(short_description__icontains= QUERY) |
        Q(long_description__icontains= QUERY)
    )

    return self.get_queryset().filter(lookup, active=True).distinct()




# model for main page 
def get_color_size_price_sorting(self, COLOR, SIZE, PRICE_MIN, PRICE_MAX, SORT_BY):
    return self.get_queryset().filter(color=COLOR, size=SIZE, price__range=(PRICE_MIN, PRICE_MAX)).order_by(
        f'{SORT_BY}')

def get_price_sorting(self, PRICE_MIN, PRICE_MAX, SORT_BY):
    return self.get_queryset().filter(price__range=(PRICE_MIN, PRICE_MAX)).order_by(f'{SORT_BY}')

def get_color_price(self, COLOR, PRICE_MIN, PRICE_MAX):
    return self.get_queryset().filter(color=COLOR, price__range=(PRICE_MIN, PRICE_MAX))

# have to fix it
def get_size_price_sorting(self, SIZE, PRICE_MIN, PRICE_MAX, SORT_BY):
    return self.get_queryset().filter(size=SIZE, price__range=(PRICE_MIN, PRICE_MAX))#.order_by(f'{SORT_BY}')

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
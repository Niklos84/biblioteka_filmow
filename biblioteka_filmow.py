from random import randint

class Movie:
    def __init__(self, title, year, category):
        self.title = title
        self.year = year
        self.category = category
        
        self.views = 0

    def play(self):
        self.views += 1

    def __str__(self):
        return f'{self.title} ({self.year})'

class Series(Movie):
    def __init__(self, episode_no, series_no, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.episode_no = episode_no
        self.series_no = series_no

    def __str__(self):
        return f'{self.title} S{self.series_no:02}E{self.episode_no:02}'

def add_item(type, *args, **kwargs):
    if type == 'Movie':
        movie = Movie(*args, **kwargs)
        return movie
    if type == 'Series':
        series = Series(*args, **kwargs)
        return series

imdb = []
imdb.append(add_item('Movie', 'Pulp Fiction', 1994, 'action'))
imdb.append(add_item('Movie', 'Terminator', 1984, 'action'))
imdb.append(add_item('Movie', 'Hot Shots', 1991, 'comedy'))
imdb.append(add_item('Series', 3, 1, 'Stranger Things', 2016, 'thriller'))
imdb.append(add_item('Series', 2, 1, 'Stranger Things', 2016, 'thriller'))
imdb.append(add_item('Series', 5, 2, 'South Park', 1997, 'comedy'))

def get_movies(imdb):
    movies = []
    for i in imdb:
        if isinstance(i, Series) == False:
            movies.append(i)
    return movies

def get_series(imdb):
    series = []
    for i in imdb:
        if isinstance(i, Series) == True:
            series.append(i)
    return series

def search(imdb):
    phrase = input('Wprowadź tytuł: ')
    for i in imdb:
        if i.title == phrase:
            return i

def generate_views(imdb):
    elements = len(imdb) - 1
    random_item = imdb[randint(0,elements)]
    random_item.views = randint(1,100)
    return imdb

for i in range(10):
    generate_views(imdb)

def top_titles(imdb):
    by_views = sorted(imdb, key=lambda item: item.views)
    top_titles = []
    for i in by_views[:3]:
        top_titles.append(i)
    return top_titles

top = top_titles(imdb)
for i in top: print(i)


#print(random.views)
#search_result = search(imdb)
#print(search_result)
#movies = get_movies(imdb)
#for i in movies: print(i)
#series = get_series(imdb)
#for i in series: print(i)


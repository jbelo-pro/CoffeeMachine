class Painting:
    museum = 'Louvre'

    def __init__(self, title, painter, year_creation):
        self.title = title
        self.painter = painter
        self.year_creation = year_creation


title = input()
painter = input()
year = input()

p = Painting(title, painter, year)

print('"{}" by {} ({}) hangs in the {}.'.format(p.title, p.painter,
                                                p.year_creation,
                                                Painting.museum))

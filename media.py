class Movie():
    '''
    the class represent movie entity, includes title, storyline, poster_url, trailer_url variable
    and output_html() method
    '''
    MOVIE_HTML_TEMPLATE = '''
    to do
    '''

    def __init__(self,movie_title,movie_storyline,movie_poster,movie_trailer):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = movie_poster
        self.trailer_youtube_url = movie_trailer

    def output_html(self):
        return self.MOVIE_HTML_TEMPLATE


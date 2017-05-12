class Movie():
    '''
    the class represent movie entity, includes title, storyline, poster_url, trailer_url variable
    and init() method
    '''


    def __init__(self,movie_title,movie_storyline,movie_poster,movie_trailer):
        '''
        initialize a instance of movie, set movie property
        :param movie_title: string
        :param movie_storyline: string no more than 265 chars
        :param movie_poster: url of poster
        :param movie_trailer: url of trailer
        '''
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = movie_poster
        self.trailer_youtube_url = movie_trailer




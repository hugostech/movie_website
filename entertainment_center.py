import media

class Entertainment():
    MOVIE_LIST = []
    def __init__(self,movie_infos):
        for movie_name,movie_detail in movie_infos.iteritems():
            movie = media.Movie(movie_name,movie_detail["storyline"],movie_detail["poster_url"],movie_detail["trailer_url"])
            self.MOVIE_LIST.append(movie)


# -- coding:utf8 --
import media

class Entertainment():
    '''
    Class Entertainment is used for transfer input formated data to movie instances.
    '''
    MOVIE_LIST = [] # array to save movie instance
    def __init__(self,movie_infos):
        '''
        :param movie_infos: accept specific data structure. 
        
        Example: {"摔跤吧！爸爸":{
                "storyline":"这是一个温暖幽默的励志故事。马哈维亚辛格珀尕（阿米尔汗饰）曾是印度国家摔跤冠军，因生活所迫放弃摔跤...",
                "poster_url":"http://img5.mtime.cn/mg/2017/05/05/095019.92497624_270X405X4.jpg",
                "trailer_url":'https://youtu.be/x_7YlGv9u1g'}}
        '''
        for movie_name,movie_detail in movie_infos.iteritems():
            movie = media.Movie(movie_name,movie_detail["storyline"],movie_detail["poster_url"],movie_detail["trailer_url"])
            self.MOVIE_LIST.append(movie)


import webbrowser
class Movie:
    """the created webpage plays a movie trailer when the user clicks on the movie poster"""
    
    
    def __init__(self,movie_title,movie_storyline,poster_image,trailer_youtube):
        self.title=movie_title
        self.storyline=movie_storyline
        self.poster_image_url=poster_image
        self.trailer_youtube_url=trailer_youtube
    
    
    
    #function to show the trailer when we click on the poster
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
                 

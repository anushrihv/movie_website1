import fresh_tomatoes
import media



kung_fu_panda=media.Movie("kung fu panda",
                          "Story of a cute panda",
                          "https://images-na.ssl-images-amazon.com/images/M/MV5BMTIxOTY1NjUyN15BMl5BanBnXkFtZTcwMjMxMDk1MQ@@._V1_UX182_CR0,0,182,268_AL_.jpg",
                          "https://www.youtube.com/watch?v=PXi3Mv6KMzY")


ice_age=media.Movie("Ice age",
                         "The exciting journey of a few animals in the world of ice",
                         "http://vignette4.wikia.nocookie.net/iceage/images/9/94/Ice_Age_Original_Poster.jpg/revision/latest?cb=20100512224000",
                         "https://www.youtube.com/watch?v=HyLquKn3Swc")


finding_nemo=media.Movie("Finding nemo",
                         "Finding a fish called nemo",
                         "https://i.jeded.com/i/finding-nemo.462.jpg",
                         "https://www.youtube.com/watch?v=wZdpNglLbt8")

movies=[kung_fu_panda,ice_age,finding_nemo]
fresh_tomatoes.open_movies_page(movies)

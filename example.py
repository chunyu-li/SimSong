from recommend_song import Recommender

if __name__ == '__main__':

    # Specify the song path
    song_path = './music.mp3'

    # Instantiate a Recommender object
    recommender = Recommender(song_path)

    # Return the song type and similar songs
    song_type, sim_songs = recommender.recommend_sim_songs()

    for item in sim_songs:
        print(item)

# Similar Song Recommendation

## Introduction

The project implements the function of recommending similar songs based on deep learning. The frequencies information is used as song features to implement this, so the reviews of users are not required.

## Basic implementation idea

1. Utilize [Sox](http://sox.sourceforge.net/) to convert audio files to image files in spectrogram form. A *spectrogram* is a visual representation of the spectrum of frequencies of a signal as it varies with time.
2. Use a pretrained CNN model to perform feature extraction. After fully connected layer, a feature vector representing song features will be output (based on [TensorFlow](https://www.tensorflow.org/) framework).
3. Calculate cosine similarity between the given song (expected for recommending) and each of song in our dataset. Rank the scores and return top 4 songs.

## Dependency

```shell
# Execute this command under root directory to install related python dependencies
pip install -r requirements.txt
```

You also need to install command line tool SoX on your machine. The installation steps of different platforms are given below.

### Windows

There is not a convenient package manager on Windows. You should go to official site of [Sox](http://sox.sourceforge.net/) to download it manully.

### Mac OS

```bash
brew install sox
```

### Linux

```bash
sudo apt install sox
sudo apt install libsox-fmt-mp3
```

## Get started

```python
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
```

The result:

```
{'song': 'No Good', 'artist': 'BLU INC'}
{'song': 'Believe Anyway', 'artist': '7008 feat STOOPID & CONTAGIOUS'}
{'song': 'I Am (Club mix)', 'artist': 'BLACKWOOD'}
{'song': 'Right Now (original mix)', 'artist': 'ALEX HOOK feat RENE'}
```


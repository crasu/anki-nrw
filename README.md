# Setup

1. Install via `pipenv install`
2. Enter venv shell via `pipenv shell`
3. Generate sound file
4. Run script `python create-anki.py`

# Generate sounds

1. Install tts-cli
   
    `npm install tts-cli -g`

3. Generate sound files

    `while read f ; do echo $f > "woerter/$f"; tts "woerter/$f" "sound/$f.mp3" --language "de-AT" --voice Vicki --engine neural ; done<wortliste.txt`



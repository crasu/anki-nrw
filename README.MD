# Setup

1. Install via `pipenv install`
2. Enter venv shell via `pipenv shell`

# Generate sounds

1. Install tts-cli

    npm install tts-cli -g

2. Generate sound files

    for f in $(cat wortliste); do echo $f > woerter/$f; tts woerter/$f sound/$f.mp3 --language "de-AT" --voice Vicki --engine neural ; done

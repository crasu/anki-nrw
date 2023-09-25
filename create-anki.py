import genanki
import os

my_model = genanki.Model(
  1607392319,
  'Simple Model',
  fields=[
    {'name': 'Ton'},
    {'name': 'Antwort'},
  ],
  templates=[
    {
      'name': 'Karte 1',
      'qfmt': '{{Ton}}\n{{type:Antwort}}',
      'afmt': '{{FrontSide}}\n<hr id="antwort">{{Antwort}}',
    },
  ])

def add_notes(my_deck):
    media_files = []
    with open('wortliste.txt','r') as wortliste:
        for wort in wortliste:
            wort = wort.replace('\n', '')  
            sound = wort + ".mp3"
            sound = f"[sound:{sound}]"
            
            file = f"sound/{wort}.mp3"
            if os.path.exists(file):
                media_files.append(file)
            else:
                print(f"Sound file {file} nicht gefunden.")
            
            my_note = genanki.Note(
                model=my_model,
                fields=[sound, wort])

            my_deck.add_note(my_note)
            print(wort)
    
    return media_files

def main():
    my_deck = genanki.Deck(2059400110, 'Grundwortschatz Nrw')

    media_files = add_notes(my_deck)

    package=genanki.Package(my_deck)
    package.media_files = media_files
    package.write_to_file('grundwortschatz-nrw.apkg')

main()

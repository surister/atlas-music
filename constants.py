from typing import NamedTuple


class NoteConversion(NamedTuple):

    solf = ('DO', 'RE', 'MI', 'FA', 'SOL', 'LA', 'SI')
    eng = ('A', 'B', 'C', 'D', 'E', 'F', 'G')

    eng_to_kb = {
        'F#': 'W',
        'G#': 'E',
        'A#': 'R',
        'C#': 'Y',
        'D#': 'U',
        'f': 'I',
        'F': 'A',
        'G': 'S',
        'A': 'D',
        'B': 'F',
        'C': 'G',
        'D': 'H',
        'E': 'J'
    }

    lat_to_eng = {
        'DO': 'C',
        'RE': 'D',
        'MI': 'E',
        'FA': 'F',
        'SOL': 'G',
        'LA': 'A',
        'SI': 'B'
    }

import unicodedata

def split(s):
    # XXX - this is not fully working code. See README.md
    s = unicodedata.normalize('NFC', s)
    _buffer = []
    for char in s:
        if unicodedata.combining(char):
            _buffer.append(char)
            continue
        if _buffer:
            yield ''.join(_buffer)
        _buffer = [char]
    if _buffer:
        yield ''.join(_buffer)


def debugprint(l):
    for chars in l:
        print(chars,
              ' '.join('%04x' % ord(c) for c in chars))
    print()


if __name__ == '__main__':
    debugprint(split('c\u0061\u0301t'))
    debugprint(split('c\u0061\u0305t'))
    debugprint(split('c\u0061\u0304t'))
    debugprint(split('᚛ᚑᚌᚐᚋ᚜'))
    debugprint(split('اَلْعَرَبِيَّةُ'))
    debugprint(split('\u0030\ua825'))

# humanchars

From this Twitter thread: https://twitter.com/kapellosaur/status/1232760788089278464

A problem I've come across recently is the need to split a unicode string into the parts that a human would visually understand as one letter/entity each. For example, "cat" splits into "c", "a", "t"; similarly "ca̅t" should split into "c", "a̅" (a with overline), "t".

However, a̅ can only be represented by the unicode sequence of two codepoints: 0061 ("a") + 0305 (overline) [unlike something like á which could be represented by 0061 ("a") + 0301 (acute accent) but is more commonly normalised to the single codepoint 00E1 (a with acute accent)].

In most languages, iterating over a unicode string will give you individual codepoints back<sup>1</sup>, but because a̅ and many other characters can have no single codepoint, this returns four items (c, a, overline, t) rather than the "correct-to-a-human" three (c, a with overline, t).

So if I'm trying to implement a split() method for this in Python 3, what are my options?

Python has a lovely module called unicodedata (https://docs.python.org/3/library/unicodedata.html) though it unfortunately doesn't have a split method for us.

The best I have come up with so far is using unicodedata.normalize() to fix the entities that can be combined into a single codepoint, and unicodedata.combining() to detect combining characters to group them. However I'm sure there's dozens of edge cases here that aren't covered by combining chars. Can you come up with any? Is there a better way to approach this?


<sup>1</sup> Some languages such as Java and JavaScript are also limited by 16-bit character types and have to produce surrogate pairs, which creates more problems, but let's ignore that for now.)

----

Update: the key term here is "extended grapheme cluster", from the Unicode specification at [Annex #29](https://unicode.org/reports/tr29/), as pointed out by @FakeUnicode in a [reply](https://twitter.com/FakeUnicode/status/1232804361861906432). Also, this is implemented by the third party [regex](https://pypi.org/project/regex/) library as r'\X', as pointed out by @dragondave in another [reply](https://twitter.com/dragondave/status/1232885890579681280)

#!/usr/bin/env python3

# Generate an xkb symbol file for Coptic.
# Based on the soft keyboard at https://coptic-dictionary.org/

# xkb symbol file header.
print('default  partial alphanumeric_keys modifier_keys')
print('xkb_symbols "basic" {')
print()
print('   name[Group1]= "Coptic";')

# Numbers like a normal US qwerty layout.
# Final punctuation keys are used for the combining overline,
# marking abbreviations, the diaeresis, and the single and
# double hyphens used to to mark morpheme divisions.
print('''
    key <TLDE> {	[     grave,	asciitilde	]	};
    key <AE01> {	[	  1,	exclam 		]	};
    key <AE02> {	[	  2,	at		]	};
    key <AE03> {	[	  3,	numbersign	]	};
    key <AE04> {	[	  4,	dollar		]	};
    key <AE05> {	[	  5,	percent		]	};
    key <AE06> {	[	  6,	asciicircum	]	};
    key <AE07> {	[	  7,	ampersand	]	};
    key <AE08> {	[	  8,	asterisk	]	};
    key <AE09> {	[	  9,	parenleft	]	};
    key <AE10> {	[	  0,	parenright	]	};
    key <AE11> {	[     U0305,    minus,	underscore	]	};
    key <AE12> {	[     U0308,    U2E17,    equal, plus   ]	};
''')

row1 = ['ⲑ', 'ⲱ', 'ⲉ', 'ⲣ', 'ⲧ', 'ⲯ', 'ⲩ', 'ⲓ', 'ⲟ', 'ⲡ', 'ϣ']
for i, c in enumerate(row1):
    lower = f'U{ord(c):04X}'
    upper = f'U{ord(c) - 1:04X}'
    print(f'    key <AD{i + 1:02d}> {{ [ {lower}, {upper} ] }};')
print('    key <AD12> {	[ bracketleft,	bracketright	]	};')

row2 = ['ⲁ', 'ⲥ', 'ⲇ', 'ϥ', 'ⲅ', 'ϩ', 'ϫ', 'ⲕ', 'ⲗ', 'ϧ', 'ⳉ']
for i, c in enumerate(row2):
    lower = f'U{ord(c):04X}'
    upper = f'U{ord(c) - 1:04X}'
    print(f'    key <AC{i + 1:02d}> {{ [ {lower}, {upper} ] }};')

row3 = ['ⲍ', 'ⲝ', 'ⲭ', 'ⲫ', 'ⲃ', 'ⲛ', 'ⲙ', 'ϭ', 'ϯ', 'ⲏ']
for i, c in enumerate(row3):
    lower = f'U{ord(c):04X}'
    upper = f'U{ord(c) - 1:04X}'
    print(f'    key <AB{i + 1:02d}> {{ [ {lower}, {upper} ] }};')

# The backslash key on ISO/ANSI keyboards is used for the combining
# macron marking syllabic consonants and the combinding underdot
# for marking uncertain readings in manuscript transcription.
print('''
    key <BKSL> { [ U0304, U0323 ] };
''')
print('};')

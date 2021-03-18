#!/usr/bin/env LANG=en_UK.UTF-8 /usr/local/bin/python3
'''
Multiple language title article splitting script

Takes arguments of full title, and title language in ISO Country Code alpha-2
Handles the potential for title entries to be upper case or lower case.
Loads TITLE_ARTICLES dictionary, which returns a list of title articles relevant to supplied language
Script matches title article (if present) to language key's value list,
if not returns original title and empty string.

Joanna White 2021
'''

# Dictionary of ISO country codes and title articles for each language
# These contents may have first originated from AACR2 documentation, with additions from BFI staff through the years
TITLE_ARTICLES = {'af': ["Die ", "'N "],
                  'sq': ["Nji ", "Një "],
                  'ar': ["El-", "Ad-", "Ag-", "Ak-", "An-", "Ar-", "As-", "At-", "Az-"],
                  'da': ["Den ", "Det ", "De ", "En ", "Et "],
                  'nl': ["De ", "Het ", "'S ", "Een ", "Eene ", "'N "],
                  'en': ["The ", "A ", "An "],
                  'fr': ["Le ", "La ", "L'", "Les ", "Un ", "Une "],
                  'de': ["Der ", "Die ", "Das ", "Ein ", "Eine "],
                  'el': ["Ho ", "He ", "To ", "Hoi ", "Hai ", "Ta ", "Henas ", "Heis ", "Mia ", "Hena "],
                  'he': ["Ha-" , "Ho-"],
                  'hu': ["A ", "Az ", "Egy "],
                  'is': ["Hinn ", "Hin ", "Hid ", "Hinir ", "Hinar "],
                  'it': ["Il ", "La ", "Lo ", "I ", "Gli ", "Gl'", "Le ", "L'", "Un ", "Uno ", "Una ", "Un'"],
                  'nb': ["Den ", "Det ", "De ", "En ", "Et "],
                  'nn': ["Dent ", "Det ", "Dei ", "Ein ", "Ei ", "Eit "],
                  'pt': ["O ", "A ", "Os ", "As ", "Um ", "Uma "],
                  'ro': ["Un ", "Una ", "O "],
                  'es': ["El ", "La ", "Lo ", "Los ", "Las ", "Un ", "Una "],
                  'sv': ["Den ", "Det ", "De ", "En ", "Ett "],
                  'tr': ["Bir "],
                  'cy': ["Y ", "Yr "],
                  'yi': ["Der ", "Di ", "Die ", "Dos ", "Das ", "A ", "An ", "Eyn ", "Eyne "]
                  }


def splitter(title_supplied, language):
    # Refresh variables
    title = ''
    title_art = ''
    # Manage title appearing all upper case
    if title_supplied.isupper():
        title_supplied = title_supplied.title()

    # Counts words in the supplied title
    title_strip = title_supplied.strip()
    count = 1 + title_strip.count(" ")

    # For single word titles, splits into title and title_art
    # where articles are attached to first word of title
    language = language.lower()
    if count == 1:
        if 'ar' in language or 'he' in language:
            title_supplied = title_supplied.capitalize()
            # Split here on the first word - hyphen
            if title_supplied.startswith(("El-", "Ad-", "Ag-", "Ak-", "An-", "Ar-", "As-", "At-", "Az-", "Ha-", "Ho-")):
                title_art_split = title_supplied.split("-")
                title_art = title_art_split[0]
                title = "{}".format(title_art_split[1])
        elif 'it' in language or 'fr' in language:
            title_supplied = title_supplied.capitalize()
            # Split on the first word apostrophe where present
            if title_supplied.startswith(("L'", "Un'", "Gl'")):
                title_art_split = title_supplied.split("'")
                title_art = "{}'".format(title_art_split[0])
                title = "{}".format(title_art_split[1])
        else:
            title = title_supplied
            title_art = ''

    # For multiple word titles, splits into title and title_art
    # where articles are attached to first word of title
    # and where articles are separately spaced
    elif count > 1:
        ttl = []
        title_split = title_supplied.split()
        title_art_split = title_split[0]
        title_art_split = title_art_split.capitalize()
        if 'ar' in language or 'he' in language:
            # Split here on the first word - hyphen
            if title_art_split.startswith(("El-", "Ad-", "Ag-", "Ak-", "An-", "Ar-", "As-", "At-", "Az-", "Ha-", "Ho-")):
                article_split = title_art_split.split("-")
                title_art = str(article_split[0])
                ttl.append(article_split[1])
                ttl += title_split[1:]
                title = ' '.join(ttl)
        elif 'it' in language or 'fr' in language:
            # Split on the first word apostrophe where present
            if title_art_split.startswith(("L'", "Un'", "Gl'")):
                article_split = title_art_split.split("'")
                title_art = "{}'".format(article_split[0])
                ttl.append(article_split[1])
                ttl += title_split[1:]
                title_join = ' '.join(ttl)
                title = title_join.strip()
            else:
                ttl = title_split[1:]
                title_art = title_split[0]
                title = ' '.join(ttl)
        else:
            ttl = title_split[1:]
            title_art = title_split[0]
            title = ' '.join(ttl)

    # Searches through keys for language match
    for key in TITLE_ARTICLES.keys():
        if language == str(key):
            lst = []
            lst = TITLE_ARTICLES[language]

            # Looks to match title_art with values in language key match
            # and return title, title_art where this is the case
            for item in zip(lst):
                if len(title_art) > 0:
                    title_art = title_art.capitalize()
                    if title_art in str(item):
                        title_art = title_art.title()
                        title = title[0].upper() + title[1:]
                        if title.isupper():
                            title = title.title()
                            return title, title_art
                        else:
                            return title, title_art

    # Returns titles as they are where no article language matches
    for key in TITLE_ARTICLES.keys():
        if language != str(key):
            return title_supplied, ''

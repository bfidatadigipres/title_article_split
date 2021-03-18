# Title article splitting scripts

During creation of several scripts which write film and television titles to BFI database records, a title article splitting recipe has evolved into the scripts in this repository. These script allows for language ISO codes (alpha-2) to be paired with titles, so that a pre-defined dictionary of definite and indefinite articles can be identified and separated one from another. This is completed using predefined articles in a dictionary and sting comparisons to the title supplied.  The title and title article are then supplied back for inclusion in the database's title and title article fields.

With thanks to the BFI for inclusion of the TITLE_ARTICLE dictionary. The dictionary contents may have first originated from AACR2 documentation, but over the years additions have been made by BFI staff.

Known issues: In some Scandinavian languages, such as Danish, there are instances where the article does not reside before the noun but is appended afterward as an indication of definiteness. Similarly, with some Balkan languages the final vowel of a noun (or even some occasion internal noun changes) can indicate the presence of an article. We have not yet include these examples, and no doubt many others, in the code but hope they can develop in time and with greater understanding. We welcome all feedback and collaboration in developing the script.

## title_article_input.py

This script allows for command line input of a title and ISO country code for immediate return of the title, title article. Developed as a quick way to test multiple title options and the dictionary look up for different country's articles.

Suggested inputs for testing the script:
python3 title_article_input.py "The Lighthouse" "en"
python3 title_article_input.py "L'atalante" "fr"

Where your exmaples include French or Italian titles and the article is joined to the noun, eg "L'atalante" "fr", you should wrap the title in double quotes, allowing for the L' to pass as part of the string. Otherwise the script will not function correctly.

### Script function:


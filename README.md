# Title article splitting scripts
All of these scripts and tests have been used in Python3 only.

During the creation of several scripts that write film and television titles to BFI National Archive collections database records, a title article splitting recipe has evolved into the scripts in this repository. These scripts allows for language ISO codes (alpha-2) to be paired with roman alphabet titles, so that definite and indefinite articles can be identified and separated from the titles. This is completed using predefined articles in a dictionary and string comparisons to the title supplied.  The title and title article are then supplied back for inclusion in the database's title and title article fields.

With thanks to the BFI for inclusion of the TITLE_ARTICLE dictionary. The dictionary contents may have first originated from AACR2 documentation, but over the years additions have been made by BFI staff.

Known issues: In some Scandinavian languages, such as Danish, there are instances where the article does not reside before the noun but is appended as an indication of definiteness. Similarly, with some Balkan languages the final vowel of a noun (or even some occasion internal noun changes) can indicate the presence of an article. We have not yet included these examples, and no doubt many others, but hope they can develop in time and with greater understanding. We welcome all feedback and collaboration in developing these scripts.

## title_article_input.py

This script allows for command line input of a title and ISO country code for immediate return of the title, title article. Developed as a quick way to test multiple title options and the dictionary look up for different country's articles.

Suggested inputs for testing the script:
python3 title_article_input.py "The Lighthouse" "en"
python3 title_article_input.py "L'atalante" "fr"

Where your exmaples include French or Italian titles and the article is joined to the noun, eg "L'atalante" "fr", you should wrap the title in double quotes, allowing for the L' to pass as part of the string. Otherwise the script will not function correctly.

#### Script function:
1. main() accepts two arguments as input and passes these to the splittler method
2. splitter() reformats uppercase titles using Python's title() string method, and the iso code to lower().
   - if the title length is 1:
     the script checks for articles attached to the beginning of the title using Python's startswith() method.
   - if the title length is more than 1:
     the script checks for titles attached again, but also for separate articles in the first word position using startswith().
   splitter() finally uses extracted title_article to double check for a match in the dictionary before returning 'title' and 'title_art' variables to main().

## title_article.py

This script functions as a module to be imported to a script and called with two arguments, title and ISO country code. This returns separated title and title article to the callng script, both of which can be stored in a variable for immediate use.

#### Script function:
1. splitter() receives two arguments title and ISO country code, reformats uppercase titles using Python's title() string method, and the iso code to lower().
   - if the title length is 1:
     the script checks for articles attached to the beginning of the title using Python's startswith() method.
   - if the title length is more than 1:
     the script checks for titles attached again, but also for separate articles in the first word position using startswith().
   splitter() finally uses extracted title_article to double check for a match in the dictionary before returning 'title' and 'title_art' variables

With both scripts, where articles are found the Python string split() method is used to separate the two, the article is then formatted using Python's string capitalize() method and the apostrophe is re-attached to the article, but the hyphen is discarded at present. Where the article was attached by a hyphen or apostrophe, the first letter of the newly separated title is capitalised. The title is reformed using Python's join() method, and where the first word contains both an article and title Python appends the split noun to the remainder of the title as a list.

## test_title_article.py

Test script for the title and title_article return function of title_article.py script. No import of pytest is required to run the test, but you will need it installed and the test code in the same folder as your working code. It should also have the same name as the script to be tested to make it easier to find when you have many tests/scripts in a directory.

You will need to install pytest. The easiest and safest way is to use pip to install into a Virtual Environment.
(Guidance here: https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

There are two ways to run a pytest. Change directory of your terminal console to the folder that holds both the scripts and run: `pytest -v`
This will run any/all scripts prefixed "test_" as long as they have the same script name after this prefix, so "test_title_article.py" is the test for "title_article.py".

Alternatively, from any directory run: pytest -v /path_to_script/test_title_article.py. The -v requests verbosity, useful when you have multiple test functions within the one script.

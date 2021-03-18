#!/usr/bin/env LANG=en_UK.UTF-8 /usr/local/bin/python3

import title_article


def test_en_one():
    data = title_article.splitter("The Lighthouse", "en")
    title = data[0]
    title_art = data[1]
    assert title == "Lighthouse"
    assert title_art == "The"


def test_en_two():
    data = title_article.splitter("the LIGHTHOUSE", "eN")
    title = data[0]
    title_art = data[1]
    assert title == "Lighthouse"
    assert title_art == "The"


def test_en_three():
    data = title_article.splitter("Lighthouse, The", "en")
    title = data[0]
    title_art = data[1]
    assert title == "Lighthouse, The"
    assert title_art == ""


def test_fr():
    data = title_article.splitter("L'atlante", "fr")
    title = data[0]
    title_art = data[1]
    assert title == "Atlante"
    assert title_art == "L'"


def test_ar():
    data = title_article.splitter("EL-KALAA", "ar")
    title = data[0]
    title_art = data[1]
    assert title == "Kalaa"
    assert title_art == "El"


def test_iso_error():
    data = title_article.splitter("The Lighthouse", "es")
    title = data[0]
    title_art = data[1]
    assert title == "The Lighthouse"
    assert title_art == ""


def test_jp():
    data = title_article.splitter("カタカナ", "jp")
    title = data[0]
    title_art = data[1]
    assert title == "カタカナ"
    assert title_art == ""


def test_de():
    data = title_article.splitter("Die berühmte Frau", "de")
    title = data[0]
    title_art = data[1]
    assert title == "Berühmte Frau"
    assert title_art == "Die"


def test_mess_one():
    data = title_article.splitter("kgroleth9jfgkgroleth9jfg", "93")
    title = data[0]
    title_art = data[1]
    assert title == "kgroleth9jfgkgroleth9jfg"
    assert title_art == ""


def test_mess_two():
    data = title_article.splitter("k2134&*%78237489(*7534275892", "=_")
    title = data[0]
    title_art = data[1]
    assert title == "k2134&*%78237489(*7534275892"
    assert title_art == ""

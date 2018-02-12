#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import render_template, jsonify, current_app, request
from app.models.verse import VerseModel
from app.models.chapter import ChapterModel
from . import main
from app import db

import sys
sys.setdefaultencoding('utf8')

verse_dict = {
  1:{
    4:"4-6",
    5:"4-6",
    6:"4-6",
    16:"16-18",
    17:"16-18",
    18:"16-18",
    21:"21-22",
    22:"21-22",
    29:"29-31",
    30:"29-31",
    31:"29-31",
    32:"32-33",
    33:"32-33",
    34:"34-35",
    35:"34-35",
    36:"36-37",
    37:"36-37",
    38:"38-39",
    39:"38-39",
    45:"45-46",
    46:"45-46",
  },
  2:{
    42:"42-43",
    43:"42-43",
  },
  3:{
    1:"1-2",
    2:"1-2",
    20:"20-21",
    21:"20-21",
  },
  4:{
    29:"29-30",
    30:"29-30",
  },
  5:{
    8:"8-9",
    9:"8-9",
    27:"27-28",
    28:"27-28",
  },
  6:{
    12:"12-13",
    13:"12-13",
    24:"24-25",
    25:"24-25",
    41:"41-42",
    42:"41-42",
  },
  7: {},
  8:{
    1:"1-2",
    2:"1-2",
    9:"9-10",
    10:"9-10",
    23:"23-26",
    24:"23-26",
    25:"23-26",
    26:"23-26",
  },
  9:{
    7:"7-8",
    8:"7-8",
    16:"16-17",
    17:"16-17",
  },
  10:{
    4:"4-5",
    5:"4-5",
    12:"12-13",
    13:"12-13",
    16:"16-17",
    17:"16-17",
  },
  11:{
    10:"10-11",
    11:"10-11",
    26:"26-27",
    27:"26-27",
    28:"28-29",
    29:"28-29",
    41:"41-42",
    42:"41-42",
    52:"52-53",
    53:"52-53",
  },
  12:{
    3:"3-4",
    4:"3-4",
    6:"6-7",
    7:"6-7",
    13:"13-14",
    14:"13-14",
    18:"18-19",
    19:"18-19",
  },
  13:{
    8:"8-12",
    9:"8-12",
    10:"8-12",
    11:"8-12",
    12:"8-12",
  },
  14:{
    3:"3-4",
    4:"3-4",
    11:"11-13",
    12:"11-13",
    13:"11-13",
    14:"14-15",
    15:"14-15",
    22:"22-23",
    23:"22-23",
    24:"24-25",
    25:"24-25",
  },
  15:{
    3:"3-4",
    4:"3-4",
  },
  16:{
    1:"1-3",
    2:"1-3",
    3:"1-3",
    13:"13-15",
    14:"13-15",
    15:"13-15",
    19:"19-20",
    20:"19-20",
  },
  17:{
    5:"5-6",
    6:"5-6",
    26:"26-27",
    27:"26-27",
  },
  18:{
    15:"15-16",
    16:"15-16",
    51:"51-53",
    52:"51-53",
    53:"51-53",
  },
}

@main.route('/')
def index():
    chapters = ChapterModel.query.order_by(ChapterModel.chapter_number).all()
    return render_template('main/index.html', chapters=chapters)


@main.route('/search')
def search():
    chapter = ChapterModel.find_by_chapter_number(1)
    chapters = ChapterModel.query.whoosh_search(request.args.get('query')).all()
    verses = VerseModel.query.whoosh_search(request.args.get('query')).all()
    return render_template('main/chapter.html', chapter=chapter, verses=verses)


@main.route('/chapter/<int:chapter_number>')
def chapter(chapter_number):
    chapter = ChapterModel.find_by_chapter_number(chapter_number)
    verses = VerseModel.query.order_by(VerseModel.verse_order).filter_by(chapter_number=chapter_number)

    # for i in range(0, chapter.verses_count):
    #     for verse_range in verse_dict[chapter_number]:
    #         result = []
    #         a, b = verse_range.split('-')
    #         a, b = int(a), int(b)
    #         result.extend(range(a, b + 1))
    #         if verses[i].verse_number in result:
    #             current_app.logger.info(verses[i].verse_number)

    # for verse in verses:
    #     if verse.verse_order in verse_dict[chapter_number]:
    #         verse.verse_number = verse_dict[chapter_number][verse.verse_order]
    #     else:
    #         verse.verse_number = verse.verse_order

    return render_template('main/chapter.html', chapter=chapter, verses=verses)


@main.route('/chapter/<int:chapter_number>/verse/<string:verse_number>')
def verse(chapter_number, verse_number):
    chapter = ChapterModel.find_by_chapter_number(chapter_number)
    verse = VerseModel.find_by_chapter_number_verse_number(chapter_number, verse_number)
    # word_meanings = verse.word_meanings
    # word_meaning = word_meanings.split(';')
    # for meaning in word_meaning:
    #     hanuman = meaning.partition("—")[0]
    #     current_app.logger.info(hanuman)
    return render_template('main/verse.html', chapter=chapter, verse=verse)


@main.route('/about')
def about():
    # verses = VerseModel.query.all()
    # for verse in verses:
    #     verse.word_meanings = (verse.word_meanings).lstrip("u'").rstrip("'")
    #     verse.word_meanings = '"' + verse.word_meanings + '"'
    # db.session.commit()

    return "RadhaKrishna"

# -*- coding: utf-8 -*-
from nose.tools import eq_
import bot_mock
from pyfibot.modules import module_urltitle

import pytest
from vcr import VCR
my_vcr = VCR(path_transformer=VCR.ensure_suffix('.yaml'),
             cassette_library_dir="tests/cassettes/",
             record_mode=pytest.config.getoption("--vcrmode"))


@pytest.fixture
def botmock():
    bot = bot_mock.BotMock()
    module_urltitle.init(bot)
    return bot


@my_vcr.use_cassette()
def test_one(botmock):
    msg = u"https://en.wikipedia.org/wiki/Hatfield–McCoy_feud"
    assert \
     ("#channel", u"Title: The Hatfield–McCoy feud involved two families of the West Virginia–Kentucky area along the Tug Fork of the Big Sandy River.") == \
     module_urltitle.handle_url(botmock, None, "#channel", msg, msg)


@my_vcr.use_cassette()
def test_two(botmock):
    msg = "http://fi.wikipedia.org/wiki/DTMF"
    assert \
     ("#channel", u"Title: DTMF on puhelinlaitteissa käytetty numeroiden äänitaajuusvalintatapa.") == \
     module_urltitle.handle_url(botmock, None, "#channel", msg, msg)


@my_vcr.use_cassette()
def test_three(botmock):
    msg = "http://en.wikipedia.org/wiki/Gender_performativity"
    assert \
     ("#channel", u"Title: Gender performativity is a term created by post-structuralist feminist philosopher Judith Butler in her 1990 book Gender Trouble, which has subsequently been used in a variety of academic fields.") == \
     module_urltitle.handle_url(botmock, None, "#channel", msg, msg)


@my_vcr.use_cassette()
def test_four(botmock):
    msg = "http://en.wikipedia.org/wiki/Dynamo_(magician)"
    eq_(("#channel", u"Title: Steven Frayne, commonly known by his stage name \"Dynamo\", is an English magician, best known for his show Dynamo: Magician Impossible."), module_urltitle.handle_url(botmock, None, "#channel", msg, msg))


@my_vcr.use_cassette()
def test_five(botmock):
    msg = "http://fi.wikipedia.org/wiki/David_Eddings"
    eq_(("#channel", u"Title: David Carroll Eddings oli yhdysvaltalainen kirjailija, joka kirjoitti useita suosittuja fantasiakirjoja."), module_urltitle.handle_url(botmock, None, "#channel", msg, msg))


# @my_vcr.use_cassette()
# def test_six(botmock):
#     msg = "http://fi.wikipedia.org/wiki/Birger_Ek"
#     module_urltitle.init(botmock)
#     eq_(("#channel", u"Title: Rolf Birger Ek oli suomalainen lentäjä ja Mannerheim-ristin ritari."), module_urltitle.handle_url(botmock, None, "#channel", msg, msg))


@my_vcr.use_cassette()
def test_seven(botmock):
    msg = "http://en.wikipedia.org/wiki/Ramon_Llull"
    eq_(("#channel", u"Title: Ramon Llull, T.O.S.F. was a philosopher, logician, Franciscan tertiary and Majorcan writer."), module_urltitle.handle_url(botmock, None, "#channel", msg, msg))


@my_vcr.use_cassette()
def test_eight(botmock):
    msg = "http://en.wikipedia.org/wiki/Lazarus_of_Bethany#In_culture"
    eq_(("#channel", u"Title: Lazarus of Bethany, also known as Saint Lazarus or Lazarus of the Four Days, is the subject of a prominent miracle attributed to Jesus in the Gospel of John, in which Jesus restores him to life four d..."), module_urltitle.handle_url(botmock, None, "#channel", msg, msg))


@my_vcr.use_cassette()
def test_nine(botmock):
    msg = u"http://fi.wikipedia.org/wiki/Kimi_Räikkönen"
    eq_(("#channel", u"Title: Kimi-Matias Räikkönen on suomalainen autourheilija ja Formula 1:n maailmanmestari."), module_urltitle.handle_url(botmock, None, "#channel", msg, msg))


@my_vcr.use_cassette()
def test_ten(botmock):
    msg = 'http://en.wikipedia.org/wiki/802.11ac'
    eq_(("#channel", u"Title: IEEE 802.11ac is a wireless networking standard in the 802.11 family, developed in the IEEE Standards Association process, providing high-throughput wireless local area networks on the 5\xa0GHz band."), module_urltitle.handle_url(botmock, None, "#channel", msg, msg))


@my_vcr.use_cassette()
def test_eleven(botmock):
    msg = 'http://en.wikipedia.org/wiki/Edison_Arantes_do_Nascimento'
    eq_(("#channel", u"Title: Edson Arantes do Nascimento, known as Pelé, is a retired Brazilian professional footballer who played as a forward."), module_urltitle.handle_url(botmock, None, "#channel", msg, msg))


@my_vcr.use_cassette()
def test_twelve(botmock):
    msg = 'http://en.wikipedia.org/wiki/Mr._Bean'
    eq_(("#channel", u"Title: Mr. Bean is a British sitcom created by Rowan Atkinson and Richard Curtis, and starring Atkinson in the title role."), module_urltitle.handle_url(botmock, None, "#channel", msg, msg))

#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (C) 2012 by Łukasz Langa
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

"""Tests for choices."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

def setup():
    import os
    os.environ['DJANGO_SETTINGS_MODULE'] = 'dj._choicestestproject'

def test_dummy():
    """Just see if the import works as expected."""
    from dj import choices

def test_choices_basic():
    from dj.choices import Choices

    class Colors(Choices):
        _ = Choices.Choice

        white = _("White")
        yellow = _("Yellow")
        red = _("Red")
        green = _("Green")
        black = _("Black")

    assert Colors() == [(1, "White"), (2, "Yellow"), (3, "Red"), (4, "Green"),
                        (5, "Black")]
    assert Colors.white.id == 1
    assert Colors.white.desc == "White"
    assert Colors.white.name == "white"
    assert Colors.from_id(1) == Colors.white
    assert Colors.name_from_id(1) == Colors.white.name
    assert Colors.desc_from_id(1) == Colors.white.desc
    assert Colors.raw_from_id(1) == Colors.white.raw
    assert Colors.from_name("white") == Colors.white
    assert Colors.id_from_name("white") == Colors.white.id
    assert Colors.desc_from_name("white") == Colors.white.desc
    assert Colors.raw_from_name("white") == Colors.white.raw
    assert Colors.yellow.id == 2
    assert Colors.yellow.desc == "Yellow"
    assert Colors.yellow.name == "yellow"
    assert Colors.from_id(2) == Colors.yellow
    assert Colors.name_from_id(2) == Colors.yellow.name
    assert Colors.desc_from_id(2) == Colors.yellow.desc
    assert Colors.raw_from_id(2) == Colors.yellow.raw
    assert Colors.from_name("yellow") == Colors.yellow
    assert Colors.id_from_name("yellow") == Colors.yellow.id
    assert Colors.desc_from_name("yellow") == Colors.yellow.desc
    assert Colors.raw_from_name("yellow") == Colors.yellow.raw
    assert Colors.red.id == 3
    assert Colors.red.desc == "Red"
    assert Colors.red.name == "red"
    assert Colors.from_id(3) == Colors.red
    assert Colors.name_from_id(3) == Colors.red.name
    assert Colors.desc_from_id(3) == Colors.red.desc
    assert Colors.raw_from_id(3) == Colors.red.raw
    assert Colors.from_name("red") == Colors.red
    assert Colors.id_from_name("red") == Colors.red.id
    assert Colors.desc_from_name("red") == Colors.red.desc
    assert Colors.raw_from_name("red") == Colors.red.raw
    assert Colors.green.id == 4
    assert Colors.green.desc == "Green"
    assert Colors.green.name == "green"
    assert Colors.from_id(4) == Colors.green
    assert Colors.name_from_id(4) == Colors.green.name
    assert Colors.desc_from_id(4) == Colors.green.desc
    assert Colors.raw_from_id(4) == Colors.green.raw
    assert Colors.from_name("green") == Colors.green
    assert Colors.id_from_name("green") == Colors.green.id
    assert Colors.desc_from_name("green") == Colors.green.desc
    assert Colors.raw_from_name("green") == Colors.green.raw
    assert Colors.black.id == 5
    assert Colors.black.desc == "Black"
    assert Colors.black.name == "black"
    assert Colors.from_id(5) == Colors.black
    assert Colors.name_from_id(5) == Colors.black.name
    assert Colors.desc_from_id(5) == Colors.black.desc
    assert Colors.raw_from_id(5) == Colors.black.raw
    assert Colors.from_name("black") == Colors.black
    assert Colors.id_from_name("black") == Colors.black.id
    assert Colors.desc_from_name("black") == Colors.black.desc
    assert Colors.raw_from_name("black") == Colors.black.raw

def test_choices_groups():
    from dj.choices import Choices

    class Groupies(Choices):
        _ = Choices.Choice

        GROUP1 = Choices.Group(0)
        entry1 = _("entry1")
        entry2 = _("entry2")
        entry3 = _("entry3")

        GROUP2 = Choices.Group(10)
        entry4 = _("entry4")
        entry5 = _("entry5")
        entry6 = _("entry6")

        GROUP3 = Choices.Group(20)
        entry7 = _("entry7")
        entry8 = _("entry8")
        entry9 = _("entry9")

    assert Groupies() == [(1, u'entry1'), (2, u'entry2'), (3, u'entry3'),
                          (11, u'entry4'), (12, u'entry5'), (13, u'entry6'),
                          (21, u'entry7'), (22, u'entry8'), (23, u'entry9')]
    assert Groupies.entry1.group == Groupies.GROUP1
    assert Groupies.entry2.group == Groupies.GROUP1
    assert Groupies.entry3.group == Groupies.GROUP1
    assert Groupies.entry4.group == Groupies.GROUP2
    assert Groupies.entry5.group == Groupies.GROUP2
    assert Groupies.entry6.group == Groupies.GROUP2
    assert Groupies.entry7.group == Groupies.GROUP3
    assert Groupies.entry8.group == Groupies.GROUP3
    assert Groupies.entry9.group == Groupies.GROUP3
    assert Groupies.GROUP1.choices == [Groupies.entry1, Groupies.entry2,
                                       Groupies.entry3]
    assert Groupies.GROUP2.choices == [Groupies.entry4, Groupies.entry5,
                                       Groupies.entry6]
    assert Groupies.GROUP3.choices == [Groupies.entry7, Groupies.entry8,
                                       Groupies.entry9]

def test_choices_validation():
    from dj.choices import Choices

    class NoChoice(Choices):
        not_a_choice = "Not a Choice() object"

    try:
        NoChoice()
        assert False, "ValueError not raised."
    except ValueError, e:
        assert str(e) == "Choices class declared with no actual choice fields."

def test_choices_filter():
    from dj.choices import Country

    assert len(Country()) == 235
    assert Country(filter=("pl", "gb", "de")) == [(73, u'Germany'),
        (153, u'Poland'), (202, u'United Kingdom')]

def test_shifted_basic():
    from dj.choices import Choices

    class InvitationStatus(Choices):
        _ = Choices.Choice

        blocked = _("Blocked") << {'first_letter': 'b'}
        rejected = _("Rejected") << {'first_letter': 'r'}
        pending = _("Pending") << {'first_letter': 'p'}
        accepted = _("Accepted") << {'first_letter': 'a'}

    assert InvitationStatus.blocked.first_letter == 'b'
    assert InvitationStatus.rejected.first_letter == 'r'
    assert InvitationStatus.pending.first_letter == 'p'
    assert InvitationStatus.accepted.first_letter == 'a'

def test_shifted_group_inheritance():
    from dj.choices import Choices

    class Colors(Choices):
        _ = Choices.Choice

        NICE = Choices.Group(0) << {'comment': 'Nice!'}
        blue = _("Blue")
        green = _("Green") << {'comment': 'This is it.'}
        brown = _("Brown")

        UGLY = Choices.Group(10) << {'comment': 'Ugly!'}
        pink = _("Pink")
        red = _("Red")
        toxic_waste_green = _("Toxic waste green") << {'comment': 'Yuk!'}

    assert Colors.blue.comment == 'Nice!'
    assert Colors.green.comment == 'This is it.'
    assert Colors.brown.comment == 'Nice!'
    assert Colors.pink.comment == 'Ugly!'
    assert Colors.red.comment == 'Ugly!'
    assert Colors.toxic_waste_green.comment == 'Yuk!'

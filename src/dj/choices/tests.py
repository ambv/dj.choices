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


from django.test import TestCase


class SimpleTest(TestCase):
    def test_dummy(self):
        """Just see if the import works as expected."""
        from dj import choices

    def test_choices_basic(self):
        from dj.choices import Choices

        class Colors(Choices):
            _ = Choices.Choice

            white = _("White")
            yellow = _("Yellow")
            red = _("Red")
            green = _("Green")
            black = _("Black")

        self.assertEqual(Colors(), [(1, "White"), (2, "Yellow"), (3, "Red"),
                (4, "Green"), (5, "Black")])
        self.assertEqual(Colors.white.id, 1)
        self.assertEqual(Colors.white.desc, "White")
        self.assertEqual(Colors.white.name, "white")
        self.assertEqual(Colors.from_id(1), Colors.white)
        self.assertEqual(Colors.name_from_id(1), Colors.white.name)
        self.assertEqual(Colors.desc_from_id(1), Colors.white.desc)
        self.assertEqual(Colors.raw_from_id(1), Colors.white.raw)
        self.assertEqual(Colors.from_name("white"), Colors.white)
        self.assertEqual(Colors.id_from_name("white"), Colors.white.id)
        self.assertEqual(Colors.desc_from_name("white"), Colors.white.desc)
        self.assertEqual(Colors.raw_from_name("white"), Colors.white.raw)
        self.assertEqual(Colors.yellow.id, 2)
        self.assertEqual(Colors.yellow.desc, "Yellow")
        self.assertEqual(Colors.yellow.name, "yellow")
        self.assertEqual(Colors.from_id(2), Colors.yellow)
        self.assertEqual(Colors.name_from_id(2), Colors.yellow.name)
        self.assertEqual(Colors.desc_from_id(2), Colors.yellow.desc)
        self.assertEqual(Colors.raw_from_id(2), Colors.yellow.raw)
        self.assertEqual(Colors.from_name("yellow"), Colors.yellow)
        self.assertEqual(Colors.id_from_name("yellow"), Colors.yellow.id)
        self.assertEqual(Colors.desc_from_name("yellow"), Colors.yellow.desc)
        self.assertEqual(Colors.raw_from_name("yellow"), Colors.yellow.raw)
        self.assertEqual(Colors.red.id, 3)
        self.assertEqual(Colors.red.desc, "Red")
        self.assertEqual(Colors.red.name, "red")
        self.assertEqual(Colors.from_id(3), Colors.red)
        self.assertEqual(Colors.name_from_id(3), Colors.red.name)
        self.assertEqual(Colors.desc_from_id(3), Colors.red.desc)
        self.assertEqual(Colors.raw_from_id(3), Colors.red.raw)
        self.assertEqual(Colors.from_name("red"), Colors.red)
        self.assertEqual(Colors.id_from_name("red"), Colors.red.id)
        self.assertEqual(Colors.desc_from_name("red"), Colors.red.desc)
        self.assertEqual(Colors.raw_from_name("red"), Colors.red.raw)
        self.assertEqual(Colors.green.id, 4)
        self.assertEqual(Colors.green.desc, "Green")
        self.assertEqual(Colors.green.name, "green")
        self.assertEqual(Colors.from_id(4), Colors.green)
        self.assertEqual(Colors.name_from_id(4), Colors.green.name)
        self.assertEqual(Colors.desc_from_id(4), Colors.green.desc)
        self.assertEqual(Colors.raw_from_id(4), Colors.green.raw)
        self.assertEqual(Colors.from_name("green"), Colors.green)
        self.assertEqual(Colors.id_from_name("green"), Colors.green.id)
        self.assertEqual(Colors.desc_from_name("green"), Colors.green.desc)
        self.assertEqual(Colors.raw_from_name("green"), Colors.green.raw)
        self.assertEqual(Colors.black.id, 5)
        self.assertEqual(Colors.black.desc, "Black")
        self.assertEqual(Colors.black.name, "black")
        self.assertEqual(Colors.from_id(5), Colors.black)
        self.assertEqual(Colors.name_from_id(5), Colors.black.name)
        self.assertEqual(Colors.desc_from_id(5), Colors.black.desc)
        self.assertEqual(Colors.raw_from_id(5), Colors.black.raw)
        self.assertEqual(Colors.from_name("black"), Colors.black)
        self.assertEqual(Colors.id_from_name("black"), Colors.black.id)
        self.assertEqual(Colors.desc_from_name("black"), Colors.black.desc)
        self.assertEqual(Colors.raw_from_name("black"), Colors.black.raw)

    def test_choices_groups(self):
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

        self.assertEqual(Groupies(), [(1, u'entry1'), (2, u'entry2'),
                (3, u'entry3'), (11, u'entry4'), (12, u'entry5'),
                (13, u'entry6'), (21, u'entry7'), (22, u'entry8'),
                (23, u'entry9')])
        self.assertEqual(Groupies.entry1.group, Groupies.GROUP1)
        self.assertEqual(Groupies.entry2.group, Groupies.GROUP1)
        self.assertEqual(Groupies.entry3.group, Groupies.GROUP1)
        self.assertEqual(Groupies.entry4.group, Groupies.GROUP2)
        self.assertEqual(Groupies.entry5.group, Groupies.GROUP2)
        self.assertEqual(Groupies.entry6.group, Groupies.GROUP2)
        self.assertEqual(Groupies.entry7.group, Groupies.GROUP3)
        self.assertEqual(Groupies.entry8.group, Groupies.GROUP3)
        self.assertEqual(Groupies.entry9.group, Groupies.GROUP3)
        self.assertEqual(Groupies.GROUP1.choices, [Groupies.entry1,
                Groupies.entry2, Groupies.entry3])
        self.assertEqual(Groupies.GROUP2.choices, [Groupies.entry4,
                Groupies.entry5, Groupies.entry6])
        self.assertEqual(Groupies.GROUP3.choices, [Groupies.entry7,
                Groupies.entry8, Groupies.entry9])

    def test_choices_validation(self):
        from dj.choices import Choices

        class NoChoice(Choices):
            not_a_choice = "Not a Choice() object"

        try:
            NoChoice()
            self.fail("ValueError not raised.")
        except ValueError, e:
            self.assertEqual(str(e), "Choices class declared with no actual "
                    "choice fields.")

    def test_choices_filter(self):
        from dj.choices import Country

        self.assertEqual(len(Country()), 235)
        self.assertEqual(Country(filter=("pl", "gb", "de")), [(73, u'Germany'),
            (153, u'Poland'), (202, u'United Kingdom')])

    def test_shifted_basic(self):
        from dj.choices import Choices

        class InvitationStatus(Choices):
            _ = Choices.Choice

            blocked = _("Blocked") << {'first_letter': 'b'}
            rejected = _("Rejected") << {'first_letter': 'r'}
            pending = _("Pending") << {'first_letter': 'p'}
            accepted = _("Accepted") << {'first_letter': 'a'}

        self.assertEqual(InvitationStatus.blocked.first_letter, 'b')
        self.assertEqual(InvitationStatus.rejected.first_letter, 'r')
        self.assertEqual(InvitationStatus.pending.first_letter, 'p')
        self.assertEqual(InvitationStatus.accepted.first_letter, 'a')

    def test_shifted_group_inheritance(self):
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

        self.assertEqual(Colors.blue.comment, 'Nice!')
        self.assertEqual(Colors.green.comment, 'This is it.')
        self.assertEqual(Colors.brown.comment, 'Nice!')
        self.assertEqual(Colors.pink.comment, 'Ugly!')
        self.assertEqual(Colors.red.comment, 'Ugly!')
        self.assertEqual(Colors.toxic_waste_green.comment, 'Yuk!')

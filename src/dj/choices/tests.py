#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (C) 2012-2013 by Łukasz Langa
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

import six


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
        self.assertTrue(isinstance(Colors.white, Choices.Choice))
        self.assertTrue(isinstance(Colors.white, int))
        self.assertEqual(Colors.white, 1)
        self.assertEqual(Colors.white.id, 1)
        self.assertEqual(Colors.white.desc, "White")
        self.assertEqual(six.text_type(Colors.white), "White")
        self.assertEqual(Colors.white.name, "white")
        self.assertEqual(Colors.from_id(1), Colors.white)
        self.assertEqual(Colors.name_from_id(1), Colors.white.name)
        self.assertEqual(Colors.desc_from_id(1), Colors.white.desc)
        self.assertEqual(Colors.raw_from_id(1), Colors.white.raw)
        self.assertEqual(Colors.from_name("white"), Colors.white)
        self.assertEqual(Colors.id_from_name("white"), Colors.white.id)
        self.assertEqual(Colors.desc_from_name("white"), Colors.white.desc)
        self.assertEqual(Colors.raw_from_name("white"), Colors.white.raw)
        self.assertTrue(isinstance(Colors.yellow, Choices.Choice))
        self.assertTrue(isinstance(Colors.yellow, int))
        self.assertEqual(Colors.yellow, 2)
        self.assertEqual(Colors.yellow.id, 2)
        self.assertEqual(Colors.yellow.desc, "Yellow")
        self.assertEqual(six.text_type(Colors.yellow), "Yellow")
        self.assertEqual(Colors.yellow.name, "yellow")
        self.assertEqual(Colors.from_id(2), Colors.yellow)
        self.assertEqual(Colors.name_from_id(2), Colors.yellow.name)
        self.assertEqual(Colors.desc_from_id(2), Colors.yellow.desc)
        self.assertEqual(Colors.raw_from_id(2), Colors.yellow.raw)
        self.assertEqual(Colors.from_name("yellow"), Colors.yellow)
        self.assertEqual(Colors.id_from_name("yellow"), Colors.yellow.id)
        self.assertEqual(Colors.desc_from_name("yellow"), Colors.yellow.desc)
        self.assertEqual(Colors.raw_from_name("yellow"), Colors.yellow.raw)
        self.assertTrue(isinstance(Colors.red, Choices.Choice))
        self.assertTrue(isinstance(Colors.red, int))
        self.assertEqual(Colors.red, 3)
        self.assertEqual(Colors.red.id, 3)
        self.assertEqual(Colors.red.desc, "Red")
        self.assertEqual(six.text_type(Colors.red), "Red")
        self.assertEqual(Colors.red.name, "red")
        self.assertEqual(Colors.from_id(3), Colors.red)
        self.assertEqual(Colors.name_from_id(3), Colors.red.name)
        self.assertEqual(Colors.desc_from_id(3), Colors.red.desc)
        self.assertEqual(Colors.raw_from_id(3), Colors.red.raw)
        self.assertEqual(Colors.from_name("red"), Colors.red)
        self.assertEqual(Colors.id_from_name("red"), Colors.red.id)
        self.assertEqual(Colors.desc_from_name("red"), Colors.red.desc)
        self.assertEqual(Colors.raw_from_name("red"), Colors.red.raw)
        self.assertTrue(isinstance(Colors.green, Choices.Choice))
        self.assertTrue(isinstance(Colors.green, int))
        self.assertEqual(Colors.green, 4)
        self.assertEqual(Colors.green.id, 4)
        self.assertEqual(Colors.green.desc, "Green")
        self.assertEqual(six.text_type(Colors.green), "Green")
        self.assertEqual(Colors.green.name, "green")
        self.assertEqual(Colors.from_id(4), Colors.green)
        self.assertEqual(Colors.name_from_id(4), Colors.green.name)
        self.assertEqual(Colors.desc_from_id(4), Colors.green.desc)
        self.assertEqual(Colors.raw_from_id(4), Colors.green.raw)
        self.assertEqual(Colors.from_name("green"), Colors.green)
        self.assertEqual(Colors.id_from_name("green"), Colors.green.id)
        self.assertEqual(Colors.desc_from_name("green"), Colors.green.desc)
        self.assertEqual(Colors.raw_from_name("green"), Colors.green.raw)
        self.assertTrue(isinstance(Colors.black, Choices.Choice))
        self.assertTrue(isinstance(Colors.black, int))
        self.assertEqual(Colors.black, 5)
        self.assertEqual(Colors.black.id, 5)
        self.assertEqual(Colors.black.desc, "Black")
        self.assertEqual(six.text_type(Colors.black), "Black")
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

        self.assertEqual(Groupies(), [(1, six.text_type('entry1')), (2, six.text_type('entry2')),
                (3, six.text_type('entry3')), (11, six.text_type('entry4')), (12, six.text_type('entry5')),
                (13, six.text_type('entry6')), (21, six.text_type('entry7')), (22, six.text_type('entry8')),
                (23, six.text_type('entry9'))])
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
        except ValueError as e:
            self.assertEqual(str(e), "Choices class declared with no actual "
                    "choice fields.")

    def test_choices_filter(self):
        from dj.choices import Country

        self.assertEqual(len(Country()), 235)
        self.assertEqual(Country(filter=("pl", "gb", "de")), [(73, six.text_type('Germany')),
            (153, six.text_type('Poland')), (202, six.text_type('United Kingdom'))])

    def test_shifted_basic(self):
        from dj.choices import Choices

        class InvitationStatus(Choices):
            _ = Choices.Choice

            blocked = _("Blocked").extra(first_letter='b')
            rejected = _("Rejected").extra(first_letter='r')
            pending = _("Pending").extra(first_letter='p')
            accepted = _("Accepted").extra(first_letter='a')

        self.assertEqual(InvitationStatus.blocked.first_letter, 'b')
        self.assertEqual(InvitationStatus.rejected.first_letter, 'r')
        self.assertEqual(InvitationStatus.pending.first_letter, 'p')
        self.assertEqual(InvitationStatus.accepted.first_letter, 'a')

    def test_shifted_group_inheritance(self):
        from dj.choices import Choices

        class Colors(Choices):
            _ = Choices.Choice

            NICE = Choices.Group(0).extra(comment='Nice!')
            blue = _("Blue")
            green = _("Green").extra(comment='This is it.')
            brown = _("Brown")

            UGLY = Choices.Group(10).extra(comment='Ugly!')
            pink = _("Pink")
            red = _("Red")
            toxic_waste_green = _("Toxic waste green").extra(comment='Yuk!')

        self.assertEqual(Colors.blue.comment, 'Nice!')
        self.assertEqual(Colors.green.comment, 'This is it.')
        self.assertEqual(Colors.brown.comment, 'Nice!')
        self.assertEqual(Colors.pink.comment, 'Ugly!')
        self.assertEqual(Colors.red.comment, 'Ugly!')
        self.assertEqual(Colors.toxic_waste_green.comment, 'Yuk!')

    def test_choicefield(self):
        from dj._choicestestproject.app.models import Favourites, Color,\
                MusicGenre, Sports
        judy = Favourites.create(name='Judy')
        self.assertEqual(judy.color, Color.green)
        self.assertEqual(judy.music, MusicGenre.banjo)
        self.assertEqual(judy.sport, Sports.poker)
        self.assertEqual(judy.nullable, None)
        judy.color = Color.blue
        judy.music = MusicGenre.rock
        judy.sport = Sports.mountaineering
        judy.save()
        judy2 = Favourites.objects.get(name='Judy')
        # Check the type to make sure field's to_python is getting called
        self.assertEqual(type(judy2.color), type(Color.blue))
        self.assertEqual(judy2.color, Color.blue)
        self.assertEqual(judy2.music, MusicGenre.rock)
        self.assertEqual(judy2.sport, Sports.mountaineering)
        tom = Favourites.create(name='Tom', sport=Sports.mountaineering)
        self.assertEqual(Favourites.objects.filter(sport=102).count(), 2)
        self.assertEqual(Favourites.objects.filter(
            sport=Sports.mountaineering).count(), 2)
        self.assertEqual(Favourites.objects.filter(
            sport__gt=10).count(), 2)
        self.assertEqual(Favourites.objects.filter(
            color__lte=2).count(), 1)
        tom.color = 1
        tom.save()
        tom2 = Favourites.objects.get(name='Tom')
        self.assertEqual(tom2.color, Color.red)
        tom_and_judy = Favourites.objects.filter(color__in=(Color.blue, Color.red))
        self.assertEqual(tom_and_judy.count(), 2)
        self.assertEqual(set(obj.name for obj in tom_and_judy), set(['Judy', 'Tom']))
        self.assertEqual(tom2.get_sport_display(), 'Mountaineering')

    def test_form_with_choicefields(self):
        from dj._choicestestproject.app.models import Favourites, Color,\
                MusicGenre, Sports
        from dj._choicestestproject.app.forms import FavouritesForm
        empty_form = FavouritesForm()
        self.assertFalse(empty_form.is_valid())
        self.assertEqual(empty_form._bound_value('color'), Color.green.id)
        self.assertEqual(empty_form._bound_value('music'), None)
        self.assertEqual(empty_form._bound_value('sport'), None)
        self.assertEqual(empty_form._bound_value('name'), None)
        self.assertEqual(empty_form._bound_value('nullable'), None)
        empty_form_data = FavouritesForm(data={
                'color': 1, 'music': 2, 'sport': 3, 'name': 'Richard'})
        self.assertTrue(empty_form_data.is_valid())
        self.assertEqual(empty_form_data._bound_value('color'), Color.red.id)
        self.assertEqual(empty_form_data._bound_value('music'),
                MusicGenre.country.id)
        self.assertEqual(empty_form_data._bound_value('sport'), Sports.baseball.id)
        self.assertEqual(empty_form_data._bound_value('name'), 'Richard')
        self.assertEqual(empty_form_data._bound_value('nullable'), None)
        judy = Favourites.create(name='Judy')
        judy_form = FavouritesForm(instance=judy)
        self.assertFalse(judy_form.is_valid()) # because it's not bound
        self.assertEqual(judy_form._bound_value('color'), Color.green.id)
        self.assertEqual(judy_form._bound_value('music'), MusicGenre.banjo.id)
        self.assertEqual(judy_form._bound_value('sport'), Sports.poker.id)
        self.assertEqual(judy_form._bound_value('name'), 'Judy')
        self.assertEqual(judy_form._bound_value('nullable'), None)
        data_for_form = dict(judy_form.initial)
        data_for_form.update({'nullable': Color.red})
        judy_form_data = FavouritesForm(instance=judy, data=data_for_form)
        self.assertTrue(judy_form_data.is_valid())
        self.assertEqual(judy_form_data._bound_value('color'), Color.green.id)
        self.assertEqual(judy_form_data._bound_value('music'), MusicGenre.banjo.id)
        self.assertEqual(judy_form_data._bound_value('sport'), Sports.poker.id)
        self.assertEqual(judy_form_data._bound_value('name'), 'Judy')
        self.assertEqual(judy_form_data._bound_value('nullable'), Color.red.id)
        invalid_data_for_form = dict(judy_form.initial)
        invalid_data_for_form.update({'color': -1, 'music': '', 'sport': None,
                'nullable': ''})
        judy_form_invalid_data = FavouritesForm(instance=judy,
                data=invalid_data_for_form)
        self.assertFalse(judy_form_invalid_data.is_valid())
        self.assertEqual(set(judy_form_invalid_data.errors.keys()),
                set(['color', 'music', 'sport']))
        self.assertTrue('not a valid choice' in
                judy_form_invalid_data.errors['color'][0])
        self.assertTrue('cannot be null' in
                judy_form_invalid_data.errors['music'][0])
        self.assertTrue('cannot be null' in
                judy_form_invalid_data.errors['sport'][0])

    def test_regularintegers(self):
        from dj._choicestestproject.app.models import Color, RegularIntegers
        from dj._choicestestproject.app.forms import RegularIntegersForm
        rint = RegularIntegers.create()
        self.assertEqual(rint.color, Color.green.id)
        rint_invalid = RegularIntegers.create(color=-1)
        self.assertEqual(rint_invalid.color, -1)
        empty_form = RegularIntegersForm()
        self.assertFalse(empty_form.is_valid()) # because it's not bound
        valid_form = RegularIntegersForm(data={'color': 1})
        self.assertTrue(valid_form.is_valid())
        invalid_form = RegularIntegersForm(data={'color': -1})
        self.assertFalse(invalid_form.is_valid())
        self.assertTrue('color' in invalid_form.errors)
        self.assertTrue('Select a valid choice' in
                invalid_form.errors['color'][0])
        invalid_type_form = RegularIntegersForm(data={'color': 'aaa'})
        self.assertFalse(invalid_type_form.is_valid())
        self.assertTrue('color' in invalid_type_form.errors)
        self.assertTrue('Select a valid choice' in
                invalid_type_form.errors['color'][0])

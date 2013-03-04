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

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from django.db import models
from dj.choices import Choices
from dj.choices.fields import ChoiceField


class Color(Choices):
    _ = Choices.Choice

    red = _("Red")
    green = _("Green")
    blue = _("Blue")


class MusicGenre(Choices):
    _ = Choices.Choice

    banjo = _("Banjo")
    country = _("Country")
    pop = _("Pop")
    rap = _("Rap")
    rock = _("Rock")


class Sports(Choices):
    _ = Choices.Choice

    TEAM_SPORTS = Choices.Group(0, 'Team Sports')
    soccer = _("Soccer")
    basketball = _("Basketball")
    baseball = _("Baseball")

    INDIVIDUAL = Choices.Group(100, 'Individual Sports')
    swimming = _("Swimming")
    mountaineering = _("Mountaineering")
    bicycling = _("Bicycling")

    NOT_REALLY = Choices.Group(200, 'Fake Sports')
    chess = _("Chess")
    bridge = _("Bridge")
    poker = _("Poker")


class Favourites(models.Model):
    name = models.CharField(max_length=100)
    color = ChoiceField(choices=Color, default=Color.green)
    music = ChoiceField(choices=MusicGenre, filter=('rock', 'country',
        'banjo'))
    sport = ChoiceField(choices=Sports, grouped=True)
    nullable = ChoiceField(choices=Color, default=None, null=True, blank=True)

    @classmethod
    def create(cls, **kwargs):
        defaults = {
            'music': MusicGenre.banjo,
            'sport': Sports.poker,
            'color': Color.green,
            'nullable': None,
        }
        defaults.update(kwargs)
        return cls.objects.create(**defaults)


class RegularIntegers(models.Model):
    """A helper model to help test behaviour of the regular IntegerFields."""
    color = models.IntegerField(choices=Color(), default=Color.green.id)

    @classmethod
    def create(cls, **kwargs):
        defaults = {
            'color': Color.green.id,
        }
        defaults.update(kwargs)
        return cls.objects.create(**defaults)

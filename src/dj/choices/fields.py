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

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from django import forms
from django.core import exceptions
from django.db import models
from django.db.models.fields import IntegerField
from django.utils.text import capfirst
from django.utils.translation import ugettext_lazy as _
from dj.choices import unset, Choices


class ChoiceField(IntegerField):
    description = _("Integer")
    __metaclass__ = models.SubfieldBase

    def __init__(self, *args, **kwargs):
        if 'choices' not in kwargs:
            raise exceptions.ImproperlyConfigured("No choices class specified.")
        else:
            try:
                if not issubclass(kwargs['choices'], Choices):
                    raise TypeError()
            except TypeError:
                raise exceptions.ImproperlyConfigured("dj.choices class "
                        "required as `choices` argument.")
        self.choice_class = kwargs['choices']
        self.item_getter = kwargs.get('item', lambda x: (x.id,))
        kwargs['choices'] = self.choice_class(item=kwargs.get('item', unset),
            filter=kwargs.get('filter', (unset,)), grouped=kwargs.get('grouped',
                False))
        if 'default' in kwargs and not isinstance(kwargs['default'], int):
            kwargs['default'] = self.item_getter(kwargs['default'])[0]
        for arg in 'filter', 'grouped', 'item':
            if arg in kwargs:
                del kwargs[arg]
        super(ChoiceField, self).__init__(*args, **kwargs)

    def get_internal_type(self):
        return "IntegerField"

    def to_python(self, value):
        value = super(ChoiceField, self).to_python(self.get_prep_value(value))
        if value is None:
            return value
        try:
            return self.choice_class.from_id(value)
        except (TypeError, ValueError):
            raise exceptions.ValidationError(self.error_messages['invalid'])

    def get_prep_value(self, value):
        if value is None:
            return None
        if isinstance(value, unicode):
            return int(value)
        if isinstance(value, (int, long)):
            return value
        return self.item_getter(value)[0]

    def get_prep_lookup(self, lookup_type, value):
        value = self.get_prep_value(value)
        return super(ChoiceField, self).get_prep_lookup(lookup_type, value)

    def validate(self, value, model_instance):
        return super(ChoiceField, self).validate(self.get_prep_value(value),
                model_instance)

    def formfield(self, form_class=forms.CharField, **kwargs):
        """Has to be defined as a whole without doing super() because of
        Django bug #9245."""
        defaults = {'required': not self.blank, 'label': capfirst(self.verbose_name), 'help_text': self.help_text}
        if self.has_default():
            if callable(self.default):
                defaults['initial'] = self.default
                defaults['show_hidden_initial'] = True
            else:
                defaults['initial'] = self.get_default()
        if self.choices:
            # Fields with choices get special treatment.
            include_blank = self.blank or not (self.has_default() or 'initial' in kwargs)
            defaults['choices'] = self.get_choices(include_blank=include_blank)
            defaults['coerce'] = self.get_prep_value # XXX: changed
            if self.null:
                defaults['empty_value'] = None
            form_class = _TypedChoiceField # XXX: changed
            # Many of the subclass-specific formfield arguments (min_value,
            # max_value) don't apply for choice fields, so be sure to only pass
            # the values that TypedChoiceField will understand.
            for k in kwargs.keys():
                if k not in ('coerce', 'empty_value', 'choices', 'required',
                             'widget', 'label', 'initial', 'help_text',
                             'error_messages', 'show_hidden_initial'):
                    del kwargs[k]
        defaults.update(kwargs)
        return form_class(**defaults)

    def value_to_string(self, obj):
        value = self._get_val_from_obj(obj)
        return self.get_db_prep_value(value)


class _TypedChoiceField(forms.TypedChoiceField):
    def clean(self, value):
        return self.coerce(value)

    def prepare_value(self, value):
        return self.coerce(value)

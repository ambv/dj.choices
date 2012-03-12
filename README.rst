dj.choices
==========

This is a much clearer way to specify choices for fields in models and forms.
A basic example::

    >>> from dj.choices import Choices
    >>> class Gender(Choices):
    ...   _ = Choices.Choice
    ...   
    ...   male = _("Male")
    ...   female = _("Female")
    ... 
    >>> Gender()
    [(1, u'Male'), (2, u'Female')]
    >>> Gender.male
    <Choice: male (id: 1)>
    >>> Gender.female
    <Choice: female (id: 2)>
    >>> Gender.male.id
    1
    >>> Gender.male.desc
    u'Male'
    >>> Gender.male.raw
    'Male'
    >>> Gender.male.name
    u'male'
    >>> Gender.from_name("male")
    <Choice: male (id: 1)>
    >>> Gender.id_from_name("male")
    1
    >>> Gender.raw_from_name("male")
    'Male'
    >>> Gender.desc_from_name("male")
    u'Male'
    >>> Gender.name_from_id(2)
    'female'
    >>> Gender.name_from_id(3)
    Traceback (most recent call last):
    ...
    ValueError: Nothing found for '3'.
    >>> Gender.from_name("perez")
    Traceback (most recent call last):
    ...
    ValueError: Nothing found for 'perez'.

You define a class of choices, specifying each choice as a class attribute.
Those attributes automatically get indexes (starting with 1). The class provides
several features which support the DRY principle:

 * An object created from the choices class is basically a list of ``(id,
   localized_description)`` pairs straight for consumption by Django.

 * Each attribute defined can be retrieved directly from the class.
   
 * Metadata (e.g. attribute name, raw and localized description, numeric ID) of
   each attribute is accessible.

 * Choices which are suffixed by ``_`` to avoid clashing with Python keywords
   have this suffix automatically removed in their ``.name`` attributes

 * Lookup functions are available to help getting attributes or their metadata.

.. note::   
    The ``_ = Choices.Choice`` trick makes it possible for ``django-admin.py
    makemessages`` to find each choice description and include it in ``.po``
    files for localization. It masks ugettext only in the scope of the class so
    the rest of the module can safely use ugettext or ugettext_lazy. Having to
    specify ``_`` each time is not a particularly pretty solution but it's
    explicit. Suggestions for a better approach are welcome.

Grouping choices
~~~~~~~~~~~~~~~~

One of the worst problems with choices is their weak extensibility. For
instance, an application defines a group of possible choices like this::

    >>> class License(Choices):
    ...   _ = Choices.Choice
    ...   
    ...   gpl = _("GPL")
    ...   bsd = _("BSD")
    ...   proprietary = _("Proprietary")
    ... 
    >>> License()
    [(1, u'GPL'), (2, u'BSD'), (3, u'Proprietary')]
   
All is well until the application goes live and after a while the developer
wants to include LGPL. The natural choice would be to add it after ``gpl`` but
when we do that, the indexing would break. On the other hand, adding the new
entry at the end of the definition looks ugly and makes the resulting combo
boxes in the UI sorted in a counter-intuitive way. Grouping lets us solve this
problem by explicitly defining the structure within a class of choices::

    >>> class License(Choices):
    ...   _ = Choices.Choice
    ...   
    ...   COPYLEFT = Choices.Group(0)
    ...   gpl = _("GPL")
    ...   
    ...   PUBLIC_DOMAIN = Choices.Group(100)
    ...   bsd = _("BSD")
    ...   
    ...   OSS = Choices.Group(200)
    ...   apache2 = _("Apache 2")
    ...   
    ...   COMMERCIAL = Choices.Group(300)
    ...   proprietary = _("Proprietary")
    ... 
    >>> License()
    [(1, u'GPL'), (101, u'BSD'), (201, u'Apache 2'), (301, u'Proprietary')]

This enables the developer to include more licenses of each group later on::

    >>> class License(Choices):
    ...   _ = Choices.Choice
    ...   
    ...   COPYLEFT = Choices.Group(0)
    ...   gpl_any = _("GPL, any")
    ...   gpl2 = _("GPL 2")
    ...   gpl3 = _("GPL 3")
    ...   lgpl = _("LGPL")
    ...   agpl = _("Affero GPL")
    ...   
    ...   PUBLIC_DOMAIN = Choices.Group(100)
    ...   bsd = _("BSD")
    ...   public_domain = _("Public domain")
    ...   
    ...   OSS = Choices.Group(200)
    ...   apache2 = _("Apache 2")
    ...   mozilla = _("MPL")
    ...   
    ...   COMMERCIAL = Choices.Group(300)
    ...   proprietary = _("Proprietary")
    ... 
    >>> License()
    [(1, u'GPL, any'), (2, u'GPL 2'), (3, u'GPL 3'), (4, u'LGPL'),
     (5, u'Affero GPL'), (101, u'BSD'), (102, u'Public domain'),
     (201, u'Apache 2'), (202, u'MPL'), (301, u'Proprietary')]

Note the behaviour:

 * the developer renamed the GPL choice but its meaning and ID remained stable

 * BSD, Apache and proprietary choices have their IDs unchanged

 * the resulting class is self-descriptive, readable and extensible

As a bonus, the explicitly specified groups can be used when needed::

    >>> License.COPYLEFT
    <ChoiceGroup: COPYLEFT (id: 0)>
    >>> License.gpl2 in License.COPYLEFT.choices
    True
    >>> [(c.id, c.desc) for c in License.COPYLEFT.choices]
    [(1, u'GPL, any'), (2, u'GPL 2'), (3, u'GPL 3'), (4, u'LGPL'),
     (5, u'Affero GPL')]

Advanced functionality
~~~~~~~~~~~~~~~~~~~~~~

The developer can specify all possible choices for future use and then filter
out only the currently applicable values on choices creation::

    >>> class Language(Choices):
    ...   _ = Choices.Choice
    ...   
    ...   de = _("German")
    ...   en = _("English")
    ...   fr = _("French")
    ...   pl = _("Polish")
    ... 
    >>> Language()
    [(1, u'German'), (2, u'English'), (3, u'French'), (4, u'Polish')]
    >>> Language(filter=("en", "pl"))
    [(2, u'English'), (4, u'Polish')]
    
This has the great advantage of keeping the IDs and sorting intact.

One can also change how the pairs are constructed by providing a factory
function. For instance, to use the class of choices defined above for the
``LANGUAGES`` setting in ``settings.py``, one could specify::

    >>> Language(item=lambda choice: (choice.name, choice.raw))
    [(u'de', 'German'), (u'en', 'English'), (u'fr', 'French'),
     (u'pl', 'Polish')]

Predefined choices
~~~~~~~~~~~~~~~~~~

There are several classes of choices which are very common in web applications
so they are provided already: ``Country``, ``Gender`` and ``Language``.

How do I run the tests?
~~~~~~~~~~~~~~~~~~~~~~~

The easiest way would be to run::

  $ DJANGO_SETTINGS_MODULE="dj._choicestestproject.settings" django-admin.py test

Change Log
==========

0.8.1
~~~~~

* old accessors temporarily restored for backward compatibility (undocumented
  and to be removed in 1.0)

* minor documentation fixes

0.8.0
~~~~~

* code separated from ``lck.django``

* PEP8-fied the accessor APIs

Authors
=======

Glued together by `Łukasz Langa <mailto:lukasz@langa.pl>`_.

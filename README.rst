==========================
collective.downloadtracker
==========================

A Plone add-on that tracks which registered user has downloaded a file
(ATFile) at which time. It displays this value in a viewlet below File's title.
Administrators are able to delete tracked records.

* `Source code @ GitHub <https://github.com/pabo3000/collective.downloadtracker>`_
* `Releases @ PyPI <http://pypi.python.org/pypi/collective.downloadtracker>`_
* `Documentation @ ReadTheDocs <http://collectivedownloadtracker.readthedocs.org>`_
* `Continuous Integration @ Travis-CI <http://travis-ci.org/pabo3000/collective.downloadtracker>`_

How it works
============

* collective.downloadtracker adds a LinesField to ATFile via ATSchemaExtender
* Download records are appended as jsonfied dictionaries in this field.
* A viewlet appears under the title. It shows a table with the username of the
  downloader and the time.


Installation
============

To install `collective.downloadtracker` you simply add ``collective.downloadtracker``
to the list of eggs in your buildout, run buildout and restart Plone.
Then, install `collective.downloadtracker` using the Add-ons control panel.


Configuration
=============

...


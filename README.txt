Introduction
============

collective.downloadtracker is a simple Plone add-on. It tracks who has 
downloaded when the file attachment. It displays this value in a viewlet below 
File's title.
Administrators are able to delete tracked records.


Installing
==========

This package requires Plone 4.0 or later (tested on 4.1.2).

Installing without buildout
---------------------------

Install this package in either your system path packages or in the lib/python
directory of your Zope instance. You can do this using either easy_install or
via the setup.py script.

Installing with buildout
------------------------

If you are using `buildout` to manage your instance installing
collective.downloadtracker is even simpler. You can install
collective.downloadtracker by adding it to the eggs line for your instance::

    [instance]
    eggs = collective.downloadtracker

After updating the configuration you need to run the ''bin/buildout'', which
will take care of updating your system.

Go to the 'Site Setup' page in the Plone interface and click on the 'Add/Remove Products' link.

Choose the product (check its checkbox) and click the 'Install' button.



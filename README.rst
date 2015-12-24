torrentdiff finds files existing in one directory that are not required by any
torrents in another directory.

This is particularly useful to find old/unneeded files in an rTorrent data
directory that aren't served by any loaded torrents any more.

Usage
-----

::

    $ torrentdiff -s session-dir -d data-dir

Installation
------------

To install the latest stable version from PyPi:

.. code::

    pip install -U torrentdiff

To install the latest development version directly from GitHub:

.. code::

    pip install -U git+https://github.com/cdown/torrentdiff.git@develop

Testing
-------

|travis| |coveralls|

.. |travis| image:: https://travis-ci.org/cdown/torrentdiff.svg?branch=develop
  :target: https://travis-ci.org/cdown/torrentdiff
  :alt: Test status

.. |coveralls| image:: https://coveralls.io/repos/cdown/torrentdiff/badge.svg?branch=develop&service=github
  :target: https://coveralls.io/github/cdown/torrentdiff?branch=develop
  :alt: Coverage

.. code::

   tox -e quick

.. _Tox: https://tox.readthedocs.org

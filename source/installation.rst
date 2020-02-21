Installation
============

Notes
-----

.. note:: HLTV.ORG-API is supported on the following Python versions

+----------------------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+
|**Python**            |**3.8**|**3.7**|**3.6**|**3.5**|**3.4**|**3.3**|**3.2**|**2.7**|**2.6**|**2.5**|**2.4**|
+----------------------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+
|HLTV.ORG-API **0.1.0**|  Yes  |  Yes  |  Yes  |  Yes  |  Yes  |       |       |       |       |       |       |
+----------------------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+

Warnings
--------

.. warning:: HLTV.ORG-API is in a developpement phase. Some features may not work properly on your computer or on your web-browser configuration. Please submit the issues you encounter on the project's `Github page <https://github.com/jclge/HLTV.ORG-API>`_.

.. warning:: HLTV.ORG-API and its creators can not be held responsible of any inconvenience. Include it in your projects at your own risk.

Basic Installation
------------------

Linux Installation
^^^^^^^^^^^^^^^^^^

We provide a classic installation for most of Linux based distributions::

    pip install hltvorg-api

External Libraries
------------------

Most of HLTV.ORG-API requires external libraries. All bellow are required, for now.

* **selenium** provides web scrolling.

  * HLTV.ORG-API has been tested with selenium version **3.141.0**.

* **pyvirtualdisplay** provides the screen emulation to make selenium hidden.

  * HLTV.ORG-API has been tested with PyVirtualDisplay version **0.2.4** and **O.2.5**.
  * This library is mandatory for now but will be optional in a near future (from HLTV.ORG-API version **0.1.5** and above).

External Dependencies
---------------------

.. note:: For now, only *Firefox* is supported. Please refer to the **basic documentation** to know how to use another web browser.

You need a web-browser to run the API. Here are the ones we recommand.

* **Firefox**

  * HLTV.ORG-API (and selenium) has been tested with Firefox version **72.0**.
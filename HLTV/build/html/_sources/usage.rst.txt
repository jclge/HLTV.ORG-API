Overview
========

Notes
-----
.. note:: HLTV.ORG-API has been made with Selenium due to the website's limitations instead of beautifulsoup, as example, because **hltv** uses CloudFare to protect itself from DDOS & malicious attacks. It may be slow and I disencourage you to use it in real-time dynamic apps or progams. (=Selenium simulates a human hand on a real webdriver)

.. note:: This project has been tested on a computer on Arch Linux ; some features may not be compatible with non-Linux OS' or different kernels.

Warnings
--------

.. warning:: HLTV.ORG-API is **not** an official API for the website HLTV.ORG. We are not responsible for the content present on the website.

Function Prototypes
-------------------

Teams Module
^^^^^^^^^^^^

**GetTopTeams**:
    *GetTopTeams(self, string, int/string, string)*

    GetTopTeams(self, [location(default="World")], [size(default=30)], [date(default=Today)])

    **Return value**: GetTopTeams object

**TeamContent**:
    *TeamContent(self, string)*

    TeamContent(self, team)

    **Return value**: TeamContent object

News Module
^^^^^^^^^^^

**NewsContentByURL**
    *NewsContentByURL(self, string)*

    NewsContentByURL(self, url)

    **Return value**: NewsContentByURL object

**NewsContentByDate**
    *NewsContentByDate(self, string, string, string)*

    NewsContentByDate(self, title, year, month)

    **Return value**: NewsContentByDate object

**GetNewsByDate**
    *GetNewsByDate(self, string, string)*

    GetNewsByDate(self, year, month)

    **Return value**: GetNewsByDate object

**GetTodayNews**
    *GetTodayNews(self)*

    GetTodayNews(self)

    **Return value**: GetTodayNews object

**TodayNewsContent**
    *GetTodayNews(self, string)*

    GetTodayNews(self, title)

    **Return value**: TodayNewsContent object

Matches Module
^^^^^^^^^^^^^^

**OnGoingMatches**
    *OnGoingMatches(self)*

    OnGoingMatches(self)

    **Return value**: OnGoingMatches object

Use HLTV.ORG-API in your programs
---------------------------------

Import
^^^^^^

To properly use HLTV.ORG-API in your projects, you only need to import it the following way::

    import HLTV
    create_class_object = HLTV.Teams()
    print(create_class_object.GetTopTeams().teams)

You also can import each method separately::

    from HLTV import Teams
    get_content = Teams().GetTopTeams()
    print(get_content.teams)

.. note:: All of the above example display the same output

Content of HLTV objects
^^^^^^^^^^^^^^^^^^^^^^^

Any HLTV object has natively its function description::

    >>> from HLTV import Teams
    >>> print(Teams().GetTopTeams)
    <function Teams.GetTopTeams.<locals>.top_teams at [address]>

But contains number of elements inherents to its function::

    >>> from HLTV import Teams
    >>> print(Teams().GetTopTeams(size=1).teams)
    ['Astralis']
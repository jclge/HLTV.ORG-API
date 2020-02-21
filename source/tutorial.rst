Tutorial & Examples
===================



Team Module
-----------



GetTopTeams() - Basic usage
^^^^^^^^^^^^^^^^^^^^^^^^^^^

The GetTopTeams() function allows to get the current top 30 teams. You can also specify a continent or country, a date and size

Get current top 30 of the teams in the world::

    from HLTV import Teams
    top_teams = Teams().GetTopTeams().teams

.. note:: The **teams** attribute is a list

Get their score::

    from HLTV import Teams
    score_team = Teams().GetTopTeams().score

.. note:: The **score** attribute is a list

Get the players of each team::

    from HLTV import Teams
    players_from_teams = Teams().GetTopTeams().players

.. note:: The **players** attribute is a two-dimentional list




GetTopTeams() - Advanced usage
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Get current top 1 of the teams in the world::

    from HLTV import Teams
    top_team = Teams().GetTopTeams(size=1)

.. note:: The size argument cannot be bigger than 30 or lower than 1

Get current top 30 of the teams in europe::

    from HLTV import Teams
    top_eu_teams = Teams().GetTopTeams(location="Europe")

.. note:: The locations currently supported are: Europe, North America, South America, CIS, Asia, Oceania, World (default)

Get top 30 of the teams from a given date::

    from HLTV import Teams
    import datetime
    teams_ago = Teams().GetTopTeams(date=str(datetime.datetime.now()).teams

The above example will exit with an error because the date is today, this will work::

    teams_ago = Teams().GetTopTeams(date="2016-03-21").teams

.. note:: GetTopTeams will not search for the classment close to your date. Be careful that the date is a monday on which a classment came out.

.. note:: GetTopTeams supports the complete format **datetime.datetime** of dates turned into a string. Otherwise **it will wait for a date formated this way: YYYY-MM-DD**

You can now use all of the above at the same time::

    from HLTV import Teams
    top_team = Teams().GetTopTeams("Europe", 1, "2016-03-21")
    print(top_team.teams, top_team.score, top_team.players)

Which, for instance, will display::

    ['fnatic'] [1000] ['olofmeister dennis flusha JW KRIMZ']


TeamContent() - Usage
^^^^^^^^^^^^^^^^^^^^^

TeamContent() function takes **one** parameter, the team name::

    from HLTV import Teams
    Teams().TeamContent("[TeamName]")

The following attributes included in the TeamContent object are strings:

    **country** = country of the team

    **name** = name of the team

    **current_rank** = current rank on the HLTV ranking

    **weeks_in_top_30** = duration in the top 30 ; in weeks

    **peak** = the highest rank they peaked at

    **time_at_peak** = time spent at highest rank

    **current_form** = Last six results (Victory/Lose)

    **team_logo** = link to the team logo

    **players_age** = the average of the players' age

The following attributes included in the TeamContent object are lists of strings:

    **players** = the five players of the team

And are all callable the following way::

    from HLTV import Teams
    Teams().TeamContent("[TeamName]").[attribute]

**Example**::

    >>> from HLTV import Teams
    >>> astralis = Teams().TeamContent("Astralis")
    >>> astralis.name
    Astralis
    >>> astralis.peak
    1
    >>> astralis.team_logo
    https://static.hltv.org/images/team/logo/6665


News Module
-----------

NewsContentByURL() - Usage
^^^^^^^^^^^^^^^^^^^^^^^^^^

NewsContentByURL() takes **one** parameter, the url given as a string::

    import HLTV
    HLTV.News().NewsContentByURL("https://www.hltv.org/[...]")

The following attributes included in the TeamContent object are strings:

    **content** = content of the article (text only)

    **author** = name of the author of the article

    **title** = title of the article

    **date** = date of the article

The following attributes included in the TeamContent object are lists of strings:

    **images** = the images embed in the article

And are all callable the following way::

    from HLTV import News
    News().NewsContentByURL("[URL]").[attribute]


**Example**::

    >>> from HLTV import News
    >>> news_content = News().NewsContentByURL("https://www.hltv.org/news/[...]")
    >>> news_content.title
    Article title
    >>> news_content.images
    ["link_to_image.jpeg", "another_link.jpeg"]

NewsContentByDate() - Usage
^^^^^^^^^^^^^^^^^^^^^^^^^^^

NewsContentByDate() takes **three** parameters, the title given as a string, the year and the month, both given as strings or integers::

    from HLTV import News
    News().NewsContentByDate([title], [year], [month])

.. note:: The date has to be between September 2005 and Today. The month has to be mentionned.

The attributes of NewsContentByDate are the same as NewsContentByURL, please refer to it.

**Example**::

    >>> from HLTV import News
    >>> news_content = News().NewsContentByDate("title", "2012", "02")
    >>> news_content.title
    Article title
    >>> news_content.images
    ["link_to_image.jpeg", "another_link.jpeg"]

.. warning:: The **News** module uses the HLTV's official search engine. If the search result is irrelevant, try another query.

TodayNewsContent() - Usage
^^^^^^^^^^^^^^^^^^^^^^^^^^

TodayNewsContent() take one parameter, the title you're looking for, given as a string::

    from HLTV import News
    News().TodayNewsContent("title")

The attributes of NewsContentByDate are the same as NewsContentByURL and NewsContentByDate, please refer to it.

**Example**::

    >>> from HLTV import News
    >>> news_content = News().TodayNewsContent("title")
    >>> news_content.title
    Article title
    >>> news_content.images
    ["link_to_image.jpeg", "another_link.jpeg"]

GetNewsByDate() - Usage
^^^^^^^^^^^^^^^^^^^^^^^

GetNewsByDate() takes **two** parameters, the year and the month. Both can be given as string or numbers::

    from HLTV import News
    News().GetNewsByDate([year], [month])

.. note:: The date has to be between September 2005 and Today. The month has to be mentionned.

**The attributes**
All the bellow attributes are stored and returned as lists of strings:

    **news_titles** = all the news' titles

    **time** = how many time ago this news was written

    **comments** = number of comments

**Example**::

    >>> from HLTV import News
    >>> tmp = News().GetNewsByDate("2016", "08")
    >>> print(tmp.comments)
    ["n° of comments on first article", "[...] on second article", ...]

GetTodayNews() - Usage
^^^^^^^^^^^^^^^^^^^^^^

GetTodayNews() don't take any parameter.

The attributes of GetTodayNews() are the same as GetNewsByDate, please refer to it.

**Example**::

    >>> from HLTV import News
    >>> tmp = News().GetTodayNews()
    >>> tmp.news_titles
    ["first title", "second title", ...]

Matches Module
--------------

OnGoingMatches() - Usage
^^^^^^^^^^^^^^^^^^^^^^^^

OnGoingMatches() don't take any parameter::

    from HLTV import Matches
    Matches().OnGoingMatches()

The following attributes in the returned OnGoingMatches object are lists of strings:

    **stars** = the number of stars given by HLTV to the match

    **events** = in which event this match takes place

    **format** = the format of the match (BO1, BO3, etc.)

The following attributes in the returned OnGoinGMatches object are lists of lists of strings:

    **maps** = the maps we'll see during the match

    **teams** = the two teams of each match

    **scores** = the general scores of each team on each match

And are all callable the following way::

    from HLTV import Matches
    Matches().OnGoinGMatches().[attribute]

**Example**::

    >>> from HLTV import Matches
    >>> res = Matches().OnGoinGMatches()
    >>> res.teams
    [["team 1", "team 2"], ["team 1", "team 2"]]
    >>> res.format
    ["bo3", "bo1"]
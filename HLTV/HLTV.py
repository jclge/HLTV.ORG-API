from selenium import webdriver
from pyvirtualdisplay import Display
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
from time import sleep
import calendar
import datetime
from logging import error
import sys
import atexit
import os.path

sys.path.append(os.path.join(os.path.dirname("hltvorg"), '..'))

class hltv:
    url = ""
    def __init__(self):
        self.display = Display(visible=0, size=(800, 600))
        self.display.start()
        self.browser = webdriver.Firefox()

    def __del__(self):
        self.browser.close()
        self.display.stop()

class Teams(hltv):
    def GetTopTeams(self, location="World", size=30, date=""):
        if (size > 30):
            size = 30
        countries = ["europe", "north%20america", "south%20america", "cis", "asia", "oceania", "world"]
        month = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]
        def check_future(date_bis, date_tmp):
            if (int(date_bis[0]) > int(date_tmp[0])):
                return(1)
            elif (int(date_bis[1]) > int(date_tmp[1]) and int(date_bis[0]) == int(date_tmp[0])):
                return(1)
            elif (int(date_bis[2]) >= int(date_tmp[2]) and int(date_bis[1]) == int(date_tmp[1])):
                return(1)
            else:
                return(0)

        def check_past(date_bis):
            if (int(date_bis[0]) < 2015):
                return(1)
            elif (int(date_bis[0]) == 2015 and int(date_bis[1]) < 10):
                return(1)
            else:
                return(0)

        def sort(html, size):
            i = 0
            html = html.split('\n')
            while (html[i] != '#1'):
                i+=1
            res = [''] * (size + 1)
            u = 2
            i+=1
            while (u != (size + 3) and i < len(html) - 1):
                res[u - 2] = html[i]
                tmp = '#' + str(u)
                while (html[i] != tmp and i < len(html) - 1):
                    i+=1
                i+=1
                u+=1
            return(res)

        def players(html, size):
            i = 0
            html = html.split('\n')
            while (html[i] != '#1'):
                i+=1
            res = [''] * (size + 1)
            u = 3
            i+=3
            y = i
            tmp = ""
            while (i != y + 4):
                tmp = tmp + html[i] + " "
                i+=1
            tmp = tmp + html[i]
            res[0] = tmp
            i += 5
            while (u != (size + 3) and i < len(html) - 1):
                res[u - 2] = html[i]
                tmp = '#' + str(u)
                while (html[i] != tmp and i < len(html) - 1):
                    i+=1
                i+=2
                u+=1
            return(res)

        def top_teams():
            pass
        url = 'https://www.hltv.org/ranking/teams'
        if (date != ""):
            date_bis = date.split(' ')
            date_bis = date_bis[0].split('-')
            date_tmp = str(datetime.datetime.today())
            date_tmp = date_tmp.split(' ')
            date_tmp = date_tmp[0].split('-')
            if (date_bis == date_tmp):
                error("GetTopTeams: Date is today. Exit with error 1")
                exit(1)
            elif (check_future(date_bis, date_tmp) == 1):
                error("GetTopTeams: Date is in the future or does not exist. Exit with error 1")
                exit(1)
            elif (check_past(date_bis) == 1):
                error("GetTopTeams: Top teams classments started on October, 2015. Please check the date. Exit with error 1")
                exit(1)
            elif (calendar.weekday(int(date_bis[0]), int(date_bis[1]), int(date_bis[2])) != 0):
                error("GetTopTeams: Date is not valid. No classment came out on that day. Exit with error 1")
                exit(1)
            url = url + '/' + date_bis[0]
            url = url + '/' + month[int(date_bis[1]) - 1]
            url = url + '/' + date_bis[2]
        self.browser.get(url)
        location = location.lower()
        location = location.replace(" ", "%20")
        if (location[0] == 'u' and location[1] == 'r' and location[2] == 'l' and location[3] == ':'):
            location = location.replace('url:', '')
            self.browser.get(location)
        elif (location not in countries):
            error("GetTopTeams: Unkown location. Exit with error 1")
            exit(1)
        else:
            if (location != "world"):
                url = self.browser.current_url + "/country/" + location
            else:
                url = self.browser.current_url
            self.browser.get(url)
        page = self.browser.find_element_by_class_name("ranking").text
        players = players(page, size)
        page = sort(page, size)
        i = 0
        classment = [-1] * (size + 1)
        teams = [''] * (size + 1)
        while (page[i] != '' and i != len(page) - 1):
            tmp = page[i].split('(')
            classment[i] = int(tmp[1].replace(' points)', ''))
            teams[i] = tmp[0]
            i+=1
        teams.pop(len(teams) - 1)
        classment.pop(len(classment) - 1)
        players.pop(len(players) - 1)
        setattr(top_teams, 'teams', teams)
        setattr(top_teams, 'score', classment)
        setattr(top_teams, 'players', players)
        return(top_teams)

    def TeamContent(self, team=""):
        def teamdata():
            pass

        if (team == ""):
            error("Team not precised. Exit with error code 1.")
            exit(1)
        url = 'https://www.hltv.org/search?query=' + team
        self.browser.get(url)
        try:
            self.browser.find_element_by_class_name('team-logo').click()
        except ElementNotInteractableException:
            error("TeamContent: No team found. Exit with error 1")
            exit(1)
        page = self.browser.find_element_by_class_name('teamProfile').text
        page = page.split('\n')
        i = 0
        players = [""] * 5
        images = self.browser.find_elements_by_tag_name('img')
        for image in images:
            if (image.get_attribute('src')[-4:].isdigit()):
                team_pic = image.get_attribute('src')
                break
        while (page[i+2] != 'World ranking'):
            players[i] = page[i]
            i+=1
        setattr(teamdata, 'country', page[i])
        i+=1
        setattr(teamdata, 'name', page[i])
        i+=2
        page[i] = page[i].replace('#', '')
        setattr(teamdata, 'current_rank', page[i])
        i+=2
        setattr(teamdata, 'weeks_in_top_30', page[i])
        i+=2
        if ('Average player age' in page):
            setattr(teamdata, 'players_age', page[i])
        else:
            setattr(teamdata, 'players_age', 0)
        while (page[i] != 'Current form'):
            i+=1
        i+=1
        win = 0
        lose = 0
        while (page[i] != 'For core'):
            if (page[i] == 'W'):
                win+=1
            if (page[i] == 'L'):
                lose+=1
            i+=1
        results = [win, lose]
        if ("Peak" in page):
            while (page[i] != 'Peak'):
                i+=1
            i+=1
            page[i] = page[i].replace('#', '')
            setattr(teamdata, 'peak', page[i])
            i+=2
            setattr(teamdata, 'time_at_peak', page[i])
        else:
            setattr(teamdata, 'peak', '0')
            setattr(teamdata, 'time_at_peak', '0 weeks')
        setattr(teamdata, 'current_form', results)
        setattr(teamdata, 'team_logo', team_pic)
        setattr(teamdata, 'players', players)
        return(teamdata)

# MATCHES

class Matches(hltv):
    def FutureMatches(self):
        def matchesdata():
            pass

        url = "https://www.hltv.org/matches"
        self.browser.get(url)

        matches = self.browser.find_element_by_class_name('match-day').text
        return(matchesdata)

    def OnGoingMatches(self):

        def matchesdata():
            pass

        url = "https://www.hltv.org/matches"
        self.browser.get(url)
        matches = self.browser.find_element_by_class_name('live-matches')
        matches = matches.get_attribute('innerHTML')
        matches = matches.replace('  ', '')
        matches = matches.split('\n')
        matches.pop(0)
        i = 0
        tmp = ['']
        tmp_teams = ['', '']
        tmp_maps = []
        tmp_score = ['', '']
        stars = []
        teams = []
        maps = []
        events = []
        scores = []
        bestof = []
        while (i != len(matches) - 2):
            if (matches[i][:24] == '<div class="event-name">'):
                matches[i] = matches[i].replace('<div class="event-name">', '')
                matches[i] = matches[i].replace('</div>', '')
                tmp[0] = matches[i]
                events = events + tmp
                i+=2
                tmp[0] = str(matches[i].count('<i class="fa fa-star star">'))
                stars = stars + tmp
                while (matches[i][:19] != '<td class="bestof">'):
                    i+=1
                matches[i] = matches[i].replace('<td class="bestof">', '')
                matches[i] = matches[i].replace('</td>', '')
                tmp[0] = matches[i]
                bestof = bestof + tmp
                i+=1
                while (matches[i][:18] != '<td class="total">'):
                    matches[i] = matches[i].replace('<td class="map ">', '')
                    matches[i] = matches[i].replace('</td>', '')
                    tmp[0] = matches[i]
                    tmp_maps = tmp_maps + tmp
                    i+=1
                maps.append(tmp_maps)
                tmp_maps = []
                while (matches[i] != '<td class="teams">'):
                    i+=1
                i+=3
                matches[i] = matches[i].replace('<span class="team-name">', '')
                matches[i] = matches[i].replace('</span></div>', '')
                tmp_teams[0] = matches[i]
                while (matches[i][:18] != '<td class="total">'):
                    i+=1
                i+=0
                matches[i] = matches[i].split('>')
                tmp_score[0] = matches[i][2][:1]
                i += 1
                while (matches[i] != '<td class="teams">'):
                    i+=1
                i+=3
                matches[i] = matches[i].replace('<span class="team-name">', '')
                matches[i] = matches[i].replace('</span></div>', '')
                tmp_teams[1] = matches[i]
                while (matches[i][:18] != '<td class="total">'):
                    i+=1
                matches[i] = matches[i].split('>')
                tmp_score[1] = matches[i][2][:1]
                teams.append(tmp_teams)
                scores.append(tmp_score)
                tmp_teams = ["", ""]
                tmp_score = ["", ""]
                tmp_maps = ["", ""]
            i+=1
        setattr(matchesdata, 'stars', stars)
        setattr(matchesdata, 'events', events)
        setattr(matchesdata, 'format', bestof)
        setattr(matchesdata, 'maps', maps)
        setattr(matchesdata, 'teams', teams)
        setattr(matchesdata, 'scores', scores)
        return(matchesdata)

# NEWS

class News(hltv):
    def NewsContentByURL(self, url=""):
        def newsdata():
            pass

        if (url == ""):
            error("'NewsContentByURL' takes one argument: the url you're looking for. You've given 0. Exit with error 1")
            exit(1)
        elif (url[:20] != 'https://www.hltv.org'):
            error("NewsContentByURL: the argument is not an URL or not a valid link. Exit with error 1")
            exit(1)
        self.browser.get(url)
        images = self.browser.find_elements_by_tag_name("img")
        title = self.browser.find_element_by_tag_name("h1").text
        img = []
        tmp = ['']
        for image in images:
            if (image.get_attribute('src') == None):
                break
            if (image.get_attribute('src')[-5:] == '.jpeg' and 'converted' not in image.get_attribute('src')):
                tmp[0] = image.get_attribute('src')
                img = img + tmp
        res = self.browser.find_element_by_class_name("newsdsl").text
        infos = self.browser.find_element_by_class_name("article-info").text
        setattr(newsdata, 'content', res)
        infos = infos.split('\n')
        setattr(newsdata, 'author', infos[0])
        setattr(newsdata, 'title', title)
        setattr(newsdata, 'date', infos[1])
        setattr(newsdata, 'images', img)
        return(newsdata)

    def NewsContentByDate(self, title="", year="", month=""):
        months = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]
        def newsdata():
            pass

        if (str(month).isdigit() != True and month != ""):
            error("GetNewsByDate: Month is not a number nor a number in a string. Exit with error 1")
            exit(1)
        if (title == ""):
            error("'NewsContentByDate' takes at least one argument: the title or partial title you're looking for. You've given 0. Exit with error 1")
            exit(1)
        url = 'https://www.hltv.org/news/archive/'
        date_tmp = datetime.datetime.now()
        date_tmp = str(date_tmp).split('-')
        if (year == "" and month == ""):
            year = date_tmp[0]
            month = months[int(date_tmp[1]) - 1]
            url = url + str(year) + '/' + str(month)
            error(url)
        else:
            if (month == ""):
                error("NewsContentByDate: Month not mentionned. Exit with error 1")
                exit(1)
            elif (year == ""):
                error("NewsContentByDate: Year not mentionned but month is. Exit with error 1")
                exit(1)
            if (int(year) > int(date_tmp[0])):
                error("NewsContentByDate: Year is in the future. Exit with error 1")
                exit(1)
            elif (int(year) <= 2005 or (int(year) == 2005 and int(month) < 8)):
                error("NewsContentByDate: Date is not valid, must be after September 2005. Exit with error 1.")
                exit(1)
            elif (int(year) == int(date_tmp[0]) and int(month) > int(date_tmp[1])):
                error("NewsContentByDate: Month is in the future. Exit with error 1")
                exit(1)
            else:
                month = months[int(month) - 1]
                url = url + str(year) + '/' + month
        self.browser.get(url)
        try:
            self.browser.find_element_by_partial_link_text(title).click()
        except NoSuchElementException:
            error("NewsContentByDate: News not found. Exit with error 1")
            exit(1)
        images = self.browser.find_elements_by_tag_name('img')
        title = self.browser.find_element_by_tag_name("h1").text
        img = []
        tmp = ['']
        for image in images:
            if (image.get_attribute('src') == None):
                break
            if (image.get_attribute('src')[-5:] == '.jpeg' and 'converted' not in image.get_attribute('src')):
                tmp[0] = image.get_attribute('src')
                img = img + tmp
        res = self.browser.find_element_by_class_name("newsdsl").text
        infos = self.browser.find_element_by_class_name("article-info").text
        setattr(newsdata, 'content', res)
        infos = infos.split('\n')
        setattr(newsdata, 'title', title)
        setattr(newsdata, 'author', infos[0])
        setattr(newsdata, 'date', infos[1])
        setattr(newsdata, 'images', img)
        return(newsdata)

    def GetNewsByDate(self, year="", month=""):
        months = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]

        def newsdata():
            pass

        if (str(month).isdigit() != True and month != ""):
            error("GetNewsByDate: Month is not a number nor a number in a string. Exit with error 1")
            exit(1)

        url = 'https://www.hltv.org/news/archive/'
        date_tmp = datetime.datetime.now()
        date_tmp = str(date_tmp).split('-')
        if (year == "" and month == ""):
            year = date_tmp[0]
            month = months[int(date_tmp[1]) - 1]
            url = url + str(year) + '/' + str(month)
        else:
            if (month == ""):
                error("GetNewsByDate: Month not mentionned. Exit with error 1")
                exit(1)
            elif (year == ""):
                error("GetNewsByDate: Year not mentionned but month is. Exit with error 1")
                exit(1)
            if (int(year) > int(date_tmp[0])):
                error("GetNewsByDate: Year is in the future. Exit with error 1")
                exit(1)
            elif (int(year) <= 2005 or (int(year) == 2005 and int(month) < 8)):
                error("GetNewsByDate: Date is not valid, must be after September 2005. Exit with error 1.")
                exit(1)
            elif (int(year) == int(date_tmp[0]) and int(month) > int(date_tmp[1])):
                error("GetNewsByDate: Month is in the future. Exit with error 1")
                exit(1)
            else:
                month = months[int(month) - 1]
                url = url + str(year) + '/' + month

        self.browser.get(url)
        page = self.browser.find_element_by_class_name("standard-box.standard-list").text
        page = page.split('\n')
        i = 0
        j = 0
        k = 0
        l = 0
        hours = [''] * int(len(page) / 3)
        comments = [''] * int(len(page) / 3)
        news = [''] * int(len(page) / 3)
        while (i < len(page) - 2):
            news[j] = page[i]
            comments[k] = page[i + 2]
            hours[l] = page[i + 1]
            k +=1
            l += 1
            j += 1
            i += 3
        setattr(newsdata, 'news_titles', news)
        setattr(newsdata, 'time', hours)
        setattr(newsdata, 'comments', comments)
        return (newsdata)

    def GetTodayNews(self):
        def newsdata():
            pass

        url = 'https://www.hltv.org'
        self.browser.get(url)
        page = self.browser.find_element_by_class_name("standard-box.standard-list").text
        page = page.split('\n')
        i = 0
        j = 0
        k = 0
        l = 0
        hours = [''] * int(len(page) / 3)
        comments = [''] * int(len(page) / 3)
        news = [''] * int(len(page) / 3)
        while (i < len(page) - 2):
            news[j] = page[i]
            comments[k] = page[i + 2]
            hours[l] = page[i + 1]
            k +=1
            l += 1
            j += 1
            i += 3
        setattr(newsdata, 'news_titles', news)
        setattr(newsdata, 'time', hours)
        setattr(newsdata, 'comments', comments)
        return (newsdata)

    def TodayNewsContent(self, title=""):
        def newsdata():
            pass

        if (title == ""):
            error("'TodayNewsContent' takes one argument: the title or partial title you're looking for. You've given 0. Exit with error 1")
            exit(1)
        url = 'https://www.hltv.org/'
        self.browser.get(url)
        try:
            self.browser.find_element_by_partial_link_text(title).click()
        except NoSuchElementException:
            error("TodayNewsContent: News not found. Exit with error 1")
            exit(1)
        images = self.browser.find_elements_by_tag_name('img')
        title = self.browser.find_element_by_tag_name("h1").text
        img = []
        tmp = ['']
        for image in images:
            if (image.get_attribute('src') == None):
                break
            if (image.get_attribute('src')[-5:] == '.jpeg' and 'converted' not in image.get_attribute('src')):
                tmp[0] = image.get_attribute('src')
                img = img + tmp
        res = self.browser.find_element_by_class_name("newsdsl").text
        infos = self.browser.find_element_by_class_name("article-info").text
        setattr(newsdata, 'content', res)
        infos = infos.split('\n')
        setattr(newsdata, 'author', infos[0])
        setattr(newsdata, 'title', title)
        setattr(newsdata, 'date', infos[1])
        setattr(newsdata, 'images', img)
        return(newsdata)
# myUNSW to Google Calendar Timetable Importer
# More or less written by Chris Lam

try:
  from xml.etree import ElementTree # for Python 2.5 users
except ImportError:
  from elementtree import ElementTree
import gdata.service
import atom.service
import gdata.calendar
import gdata.calendar.service
import atom

from BeautifulSoup import BeautifulSoup
import re
from datetime import date
from datetime import timedelta
import urllib2
import cookielib
import re
import urllib
import socket

import time
import datetime


#THIS IS STUPID. PYTZ SUCKS PENIS. UGHHH
dst_dates = {
   2011:['3/4/2011','2/10/2011'],
   2012:['1/4/2012','7/10/2012'],
   2013:['7/4/2013','6/10/2013'],
   2014:['6/4/2014','5/10/2014'],
   2015:['5/4/2015','4/10/2015'],
   2016:['3/4/2016','2/10/2016'],
   2017:['2/4/2017','1/10/2017'],
   2018:['1/4/2018','7/10/2018'],
   2019:['7/4/2019','6/10/2019'],
   2020:['5/4/2020','4/10/2020'],
   2021:['4/4/2021','3/10/2021']
}

unsw_start_dates = {
   '11s1':'28/2/2011',
   '11s2':'18/7/2011',
   '12s1':'27/2/2012',
   '12s2':'16/7/2012',
   '13s1':'4/3/2013',
   '13s2':'29/7/2013',
   '14s1':'3/3/2014',
   '14s2':'28/7/2014',
   '15s1':'2/3/2015',
   '15s2':'27/7/2015',
   '16s1':'29/2/2016',
   '16s2':'25/7/2016'
}

days = {"Mon":0, "Tue":1, "Wed":2, "Thu":3, "Fri":4}

login_url='https://ssologin.unsw.edu.au/cas/login?service=https%3A%2F%2Fmy.unsw.edu.au%2Famserver%2FUI%2FLogin%3Fmodule%3DISISWSSO%26IDToken1%3D'

timetable_url='https://my.unsw.edu.au/active/studentTimetable/timetable.xml'

def getTimetable(zUser, zPass):
    jar = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(jar))
    stupid_thing = re.findall(r'_cNoOpConversation.*?"', opener.open(login_url).read())[0].replace('"', '')
    data = {'username':zUser, 'password':zPass, '_eventId':'submit', 'lt':stupid_thing}
    opener.open(login_url, urllib.urlencode(data))
    return opener.open(timetable_url).read()

def CreateClassEvent(title, content, where, start_time, end_time):
    event = gdata.calendar.CalendarEventEntry()
    event.title = atom.Title(text=title)
    event.content = atom.Content(text=content)
    event.where.append(gdata.calendar.Where(value_string=where))
    event.when.append(gdata.calendar.When(start_time=start_time, end_time=end_time))
    event.batch_id = gdata.BatchId(text='insert-request')
    return event

def dateCompare(date1, date2):
    if date1.year < date2.year:
        return -1
    elif date1.year == date2.year:
         if date1.month < date2.month:
            return -1
         elif date1.month == date2.month:
            if date1.day < date2.day:
               return -1
            elif date1.day == date2.day:
               return 0
            else:
               return 1
         else:
            return 1
    else:
         return 1

def export(f, gu, gp, zu, zp):
   if not gp or not gu:
       return "Missing Google username and password - if you don't want to upload direct to gcal, use http://www.cse.unsw.edu.au/~szyf396/timetable.html instead"

   if f == 'use-login' and (not zu or not zp):
       return "No zPass details or timetable source"

   if f == 'use-login':
       print "getting timetable"
       f = getTimetable(zu, zp)
       print "got timetable!"

   if "sectionHeading" not in f:
       return "Bad timetable source, possibly incorrect login details or dipshit myunsw general incompetence downtime (12am-2am or whatever)"

   # parsing shit
   s = BeautifulSoup(f.replace("\n",""))

   calendar_service = gdata.calendar.service.CalendarService()
   calendar_service.email = gu
   calendar_service.password = gp

   #logging into google
   try:
      calendar_service.ProgrammaticLogin()
   except socket.sslerror:
      return "Probably out of quota. Wait until quota resets (socket.sslerror)"
   except gdata.service.BadAuthentication:
      return "Bad groogle username or password"

   ####################################################
   #  LOOK EVERYONE, I'M THROWING YOUR PASSWORDS AWAY #
   ####################################################
   zp = ''
   gp = ''

   name = re.sub('@.*', '', gu)
   sem = re.sub(u'.*Semester (\S+) \S\S(\S+).*', u'\\2s\\1', s.find("option", {'selected':'true'}).text)
   title = name + "'s " + sem + " Timetable"


   # make gcal calendar
   calendar = gdata.calendar.CalendarListEntry()
   calendar.title = atom.Title(text=title)
   calendar.hidden = gdata.calendar.Hidden(value='false')
   calendar.timezone = gdata.calendar.Timezone(value='Australia/Sydney')

   try:
      calendar = calendar_service.InsertCalendar(new_calendar=calendar)
   except gdata.calendar.service.RequestError:
      return "Failed to create new calendar " + title


   batch_request_feed = gdata.calendar.CalendarEventFeed()

   week_after_midsem_break = int(s.find(text="N1").findNext("table").findNext("td").text)

   courses = [x.contents[0] for x in s.findAll("td", {"class":"sectionHeading"})]

   print "Parsing calendar to make events"

   for course in courses:
       classes = s.find(text=course).findNext("table").findAll("tr", {"class":re.compile("data")})
       ctype, code, day, tim, weeks, place, t = ['' for x in xrange(7)]
       for c in classes:
           a = [(x.contents[0] if x.contents else "") for x in c.findAll("td", recursive=False)]
           g = (t for t in a)
        
           t = g.next()

           if t.strip() != "&nbsp;":
               ctype = t

           t = g.next()
           if t.strip() not in days:
               code = t
               day = g.next().strip()
           else:
               day = t.strip()
           tim = g.next()
           weeks = g.next()
           place = g.next()
           t = ' '.join(g.next().findAll(text=True))

           if tim.find(" - ") == -1:
               continue
           start, end = tim.split(" - ")
           start = datetime.datetime.strptime(unsw_start_dates[sem] + ' ' + start,"%d/%m/%Y %I:%M%p")
           end = datetime.datetime.strptime(unsw_start_dates[sem] + ' ' + end,"%d/%m/%Y %I:%M%p")        
   
           course = course.split()[0]
        

           w = []
           for r in weeks.split(","):
               if "N" in r:
                   print "Did not process %s %s %s because of non-integer week"
                   continue
               if "-" in r:
                   w+=range(int(r.split("-")[0]), int(r.split("-")[1])+1)
               else:
                   w+=[int(r)]
                
           weeks = w
        
           for w in weeks:
               if w < week_after_midsem_break:
                   w -= 1
               thisStart = start + datetime.timedelta(7 * w + days[day])
               thisEnd = end + datetime.timedelta(7 * w + days[day])
            
               fmt = "%d/%m/%Y"
               if dateCompare(thisStart, datetime.datetime.strptime(dst_dates[start.year][0], fmt)) >= 0 and dateCompare(thisStart, datetime.datetime.strptime(dst_dates[start.year][1], fmt)) < 0:
                  tzdelta = -10
               else:
                  tzdelta = -11

               thisStart += datetime.timedelta(hours=tzdelta)
               thisEnd += datetime.timedelta(hours=tzdelta)
               thisEvent = CreateClassEvent('%s %s' % (course, ctype), "Instructor: %s Code:%s"%(t.strip(), code), place, thisStart.strftime('%Y-%m-%dT%H:%M:%S.000Z'), thisEnd.strftime('%Y-%m-%dT%H:%M:%S.000Z'))
               batch_request_feed.AddInsert(entry=thisEvent)            

   print "Uploading events"
   try:
      calendar_service.ExecuteBatch(batch_request_feed, 'https://www.google.com/calendar/feeds/' + re.sub('.*/', '', calendar.id.text) + '/private/full/batch')
   except gdata.calendar.service.RequestError:
      return "Error. Most likely a google api failure. Try again. If it happens lots, raise a bug"
   print "Probably success!"


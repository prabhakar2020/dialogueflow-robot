from __future__ import print_function
from future.standard_library import install_aliases
install_aliases()

from urllib.parse import urlparse, urlencode
from urllib.request import urlopen, Request
from urllib.error import HTTPError

import json
import os

from flask import Flask
from flask import request
from flask import Flask, make_response, request
import json
import sqlite3 as sq


# A very simple Flask Hello World app for you to get started with...

from flask import Flask, make_response, request
import json
import sqlite3 as sq

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from Flask!'
@app.route("/webhook",methods = ['POST'])
def webhook():
    if request.method == 'POST':
        req = request.get_json(silent=True, force=True)
        print ("#"*50)
        print (req)
        res = processRequest(req)
        res = json.dumps(res, indent=4)
        r = make_response(res)
        r.headers["Content-Type"] = 'application/json'
        return r
@app.route("/get")
def get():
    con = sq.connect("database.db")
    cur = con.cursor()
    cur.execute("select command from data where mode !='respect'")
    data = cur.fetchone() or "ok"
    cur.execute("delete from data where mode !='respect'")
    con.commit()
    con.close()
    return str(data)

def processRequest(req):
    query_response = req.get("queryResult",{})


    entities = {
        "thanks": ["thanks","thank u","thank you","thank q"],
        "jira":["jira","jeera","jila","zera","zara","jara","dera","genetic code","gira","genetic","zehra","jehra","dear","my ticket",'issue','tissue','defect','defeat','repeat','differenc','defense'],
        "lock":["lock","luck","look","lack"],
        "call_me": ["call me","called me","callme","calledme"],
        "build": ["bill","build","bold","bad","bald",'github', 'git hub', 'great hut','great hub','deploy', 'guitar', 'get on','get all', 'bill status','guild','boogie status','diplomat','brother', 'daily status','ability','daily','politics', 'plug in','plug-in','plumb'],
        'code_smell': ['code smell', 'code small', 'coat smell','goat smell','goat small','great small', 'great smell', 'code issue','quality issue', 'core smell','code small','core issue','kodesh verse','quote', 'sports','quality shoe', 'coat', 'tissue','good qual'],
        'velocity': ['team velocity', 'velocity','veternity', 'elocity', 'capacity'],
        "play_video": ["play video","play vid","play the video","play the vid","some video","a video","the video"],
        "stop_video": ["stop video","stop vid","stop the video","stop the v", "stop a v","stop some v", "close the video","close a video","close a v","close the v"],
        "open_jira": ["open jira","open jeera","open dera","open jila","open zera","open zara","open jara","open genetic code","open gira","open genetic","open zehra","open jehra","open dear","open my ticket",'open issue','open tissue','open defect','open defeat','open repeat','open differenc','open defense'],
        "mail": ['open mail', 'opal mail', 'open male', 'opal male', 'open made', 'opal made','open my mail', 'opal my mail', 'open my male', 'opal my male', 'open my made', 'opal my made'],
        "calendar": ["calendar","kalandar"]
        }

    responses = {
        "thanks": "I am here to help you <<respect>>!.",
        "jira": "<<respect>>, you have 2 JIRA stories assigned as of now. Do you need anything else?",
        "lock": "<<respect>>, I have placed request to lock your computer. Anything else?",
        "call_me": "Okay, I will call you <<respect>>. How may I help you today?",
        "build": "<<respect>>, your GitHub build status is succeed with 82% test coverage. Do you need anything else?",
        "code_smell": "Here is your project code coverage",
        "velocity": "<<respect>>, here is your team velocity. Initial commitment 40%, Final commitment 40% and Completed work 20%",
        "play_video": "<<respect>>, Let me play video for you",
        "stop_video": "Okay, I have placed a request for stoping the video",
        "open_jira": "Okay <<respect>>, I am opening JIRA on browser. Do you need anything else?",
        "mail": "fine <<respect>>, I am opening your mailbox on browser. Please check it",
        "calendar": "<<respect>>, <<calendar>>"
        }


    text = query_response.get('queryText','')
    speech = "I cant find right answer for your question right now"
    for entity,values in entities.items():
        for ent in values:
            if str(ent) in text.lower():

                if str(entity) == "lock":
                    insert_data("lock","lock")
                if str(entity) == "call_me":
                    data = str(text).split("call me")
                    respect = data[-1]
                    insert_data(str(respect),"respect", True)
                if str(entity) == "play_video":
                    insert_data("play","play")
                if str(entity) == "stop_video":
                    insert_data("stop","stop")
                if str(entity) == "mail":
                    insert_data("mail","mail")
                
                speech = responses.get(str(entity),"ok").replace("<<respect>>",str(get_respect()).title())

                if str(entity) == "open_jira":
                    insert_data("open_jira","open_jira")
                    speech = responses.get(str(entity),"ok")
                if str(entity) == "calendar":
                    import google_calendar    
                    calendars = google_calendar.main(True)
                    speech = responses.get(str(entity),"ok").replace("<<calendar>>",str(calendars))
                break


    # text = query_response.get('queryText',None)
    # parameters = query_response.get('parameters',None)
    # res = get_data()
    return {
        "fulfillmentText": str(speech).replace("<<respect>>",str(get_respect()).title())
        }

def get_data():
    speech = "Response from webhook "
    return {
        "fulfillmentText": speech,
    }

def insert_data(command,mode,fresh_copy = False):
    con = sq.connect("database.db")
    cur = con.cursor()
    cur.execute("create table if not exists data(command text, mode text)")
    cur.execute("delete from data where mode !='respect'")
    if fresh_copy:
        cur.execute("delete from data")
    con.commit()
    cur.execute("insert into data values('"+str(command)+"','"+str(mode)+"')")
    con.commit()
    con.close()

def get_respect():
    try:
        con = sq.connect("database.db")
        cur = con.cursor()
        cur.execute("select command from data where mode='respect'")
        data = cur.fetchone()
        if data:
            data = data[0]
        else:
            data = "Prabhakar"
        con.close()
        return str(data)
    except:
        return "Prabhakar"


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    app.run(debug=False, port=port, host='0.0.0.0')

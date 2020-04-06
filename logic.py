model_or = {
    "thanks": ["thanks","thank u","thank you","thank q"],
    "bye": ["bye","buy","bay"],
    "jira":["jira","jeera","jila","zera","zara","jara","dera","genetic code","gira","genetic","zehra","jehra","dear","my ticket","issue","tissue","defect","defeat","repeat","differenc","defense"],
    "lock":["lock","luck","look","lack"],
    "call_me": ["call me","called me","callme","calledme"],
    "build": ["bill","build","bold","bad","bald","github", "git hub", "great hut","great hub","deploy", "guitar", "get on","get all", "bill status","guild","boogie status","diplomat","brother", "daily status","ability","daily","politics", "plug in","plug-in","plumb"],
    "code_smell": ["code smell", "code small", "coat smell","goat smell","goat small","great small", "great smell", "code issue","quality issue", "core smell","code small","core issue","kodesh verse","quote", "sports","quality shoe", "coat", "tissue","good qual"],
    "velocity": ["team velocity", "velocity","veternity", "elocity", "capacity"],
    "play_video": ["play video","play vid","play the video","play the vid","some video","a video","the video"],
    "stop_video": ["stop video","stop vid","stop the video","stop the v", "stop a v","stop some v", "close the video","close a video","close a v","close the v"],
    "open_jira": ["open jira","open jeera","open dera","open jila","open zera","open zara","open jara","open genetic code","open gira","open genetic","open zehra","open jehra","open dear","open my ticket","open issue","open tissue","open defect","open defeat","open repeat","open differenc","open defense"],
    "mail": ["open mail", "opal mail", "open male", "opal male", "open made", "opal made","open my mail", "opal my mail", "open my male", "opal my male", "open my made", "opal my made"]
}
model_and = {
    "thanks": [],
    "jira":["ticket"],
    "build": [],
    "lock":["comput"],
    "velocity": ["team"]
}

and_entities = [("jira","check"),("find","jira"),("tell","jira")]
or_entities = [("ticket","issues")]
t = "Can you tell me my jira tickets"
t = "can you help me to find my salary detailsckets"
t = "can you help me to get my jira tickets"
t = "can you please lock my computer"
t = "what is my github status"
t = "thanks for your help"
t = "wht is my team velocity"
t = "can you plz open my jira tickets"
t = "can you plz open my mail box"
t = "bye"

def check_or_condition():
    print ("*"*100)
    status = False
    entity_key = ''
    for key,values in model_or.items():
        b = [' "'+j+'" in "'+t+'"' for j in values]
        condition = ' or '.join(b)
        
        print (condition)
        print (key,eval(condition))
        if eval(condition):
            status = True
            entity_key = key
            break
    return status,entity_key
        
def check_and_condition():
    print ("="*100)
    status = False
    entity_key = ''
    for key,values in model_and.items():
        b = [' "'+j+'" in "'+t+'"' for j in values]
        print (values,">>>>")
        if not values:
            print (key,"^^^"*100)
            continue
        condition = ' and '.join(b)
        print ("&"*100)
        print (condition)
        print ("#"*100)
        # print (key,eval(condition))
        if eval(condition):
            status = True
            entity_key = key
            break
    return status,entity_key

def check_and(entity_key, entities):
    # print ("="*100)
    # print (entities)
    if not entities:
        return entity_key, True
    # for key,values in model_and.items():
    b = [' "'+j+'" in "'+t+'"' for j in entities]
    condition = ' and '.join(b)
    # print ("&"*100)
    # print (condition)
    # print ("#"*100)
    # print (key,eval(condition))
    if eval(condition):
        print (">>>>>>>",condition)
        return entity_key, True
    return entity_key, False

def check_or(entity_key, entities):
    # print ("="*100)
    # print (entities)
    if not entities:
        return 'fallback', True
    # for key,values in model_and.items():
    b = [' "'+j+'" in "'+t+'"' for j in entities]
    condition = ' or '.join(b)
    # print ("&"*100)
    # print (condition)
    # print ("#"*100)
    # print (key,eval(condition))
    if eval(condition):
        print ("@@@@@@",condition)
        return entity_key, True
    return entity_key, False

def check_condition():
    all_entities = model_and.keys() + model_or.keys()
    all_entities = list(set(all_entities))
    print (all_entities)
    is_result_found = False
    for entity in all_entities:
        # data = model_and.get(str(entity), [])
        and_key, and_cmd = check_and(entity, model_and.get(str(entity), []))
        or_key, or_cmd = check_or(entity, model_or.get(str(entity), []))
        print (entity,"AND :",and_cmd) 
        print (entity,"OR :",or_cmd) 
        # raw_input("??????")
        if and_cmd and or_cmd:
            print ("AND"*10)
            print (and_key, or_key, entity)
            is_result_found = True
            break
        # if and_cmd or or_cmd:
        #     print ("OR"*10)
        #     print (and_key, or_key, entity)
        #     is_result_found = True
        #     break
    if not is_result_found:
        print ("----- Call Fallback")
        # if and_cmd:
        #     break
    # for key,entities in 
    # and_cmd = check_and_condition()
    # # or_cmd = check_or_condition()
    # print ("AND :",and_cmd)
    # # print ("OR :",or_cmd)
check_condition()
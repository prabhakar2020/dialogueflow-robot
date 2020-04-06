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



class PROCESS(object):
    def __init__(self, sentence):
        self.sentence = sentence
        pass
    
    def check_and(self, entity_key, entities):
        if not entities:
            return 'fallback', True
        b = [' "'+j+'" in "'+self.sentence+'"' for j in entities]
        condition = ' and '.join(b)
        if eval(condition):
            return entity_key, True
        return entity_key, False

    def check_or(self, entity_key, entities):
        if not entities:
            return 'fallback', True
        b = [' "'+j+'" in "'+self.sentence+'"' for j in entities]
        condition = ' or '.join(b)
        if eval(condition):
            return entity_key, True
        return entity_key, False

    def check_condition(self):
        all_entities = model_and.keys() + model_or.keys()
        all_entities = list(set(all_entities))
        print (all_entities)
        is_result_found = False
        for entity in all_entities:
            # data = model_and.get(str(entity), [])
            and_key, and_cmd = self.check_and(entity, model_and.get(str(entity), []))
            or_key, or_cmd = self.check_or(entity, model_or.get(str(entity), []))
            # print (entity,"AND :",and_cmd) 
            # print (entity,"OR :",or_cmd) 
            # raw_input("??????")
            if and_cmd and or_cmd:
                print (and_key, or_key, entity)
                is_result_found = True
                break
        if not is_result_found:
            print ("----- Call Fallback")


inputs = [
    "Can you tell me my jira tickets", 
    "can you help me to find my salary detailsckets",
    "can you help me to get my jira tickets",
    "can you please lock my computer",
    "what is my github status",
    "thanks for your help",
    "wht is my team velocity",
    "can you plz open my jira tickets",
    "can you plz open my mail box",
    "thank you"
]

for i in inputs:
    print (i)
    raw_input("....")
    PROCESS(i).check_condition()
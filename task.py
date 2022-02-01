#task
import datetime
from speak import speak

#the task is divided in two parts

#1st is non input based like - telling time,date

#2nd is input based like - google search, opening any application

# Non input tasks

def time():
    time = datetime.datetime.now().strftime("%H:%m")
    speak(time)

def date():
    date = datetime.date.today()    
    speak(date)

def NItas(query):      #ni -non input task execution

    query = str(query)

    if "time" in query:
        time()

    elif "date" in query:
        date()    



#input excution tasks


    
# from itertools import Predicate
import random
import json
from tokenize import Name, Special
import  torch
from Brain import NueralNat
from neuralnet import bag_of_words,tokenize

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
with open("intents.json",'r') as json_data:
    intents = json.load(json_data)

FILE = "TrainData.pth"    
data = torch.load(FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words =data["all_words"]
tags = data["tags"]
model_state = data["model_state"]

model =NueralNat(input_size,hidden_size,output_size).to(device)
model.load_state_dict(model_state)
model.eval()



#-----------------------------------------------------------------------------------------------#

Name = "Friday"
from speak import speak
from listen import listen
from task import NItaskexecution, time

def Main():

    query = listen()

    if  query == "bye":
        exit()

    query = tokenize(query)    
    X = bag_of_words(query,all_words)
    X = X.reshape(1,X.shape[0])
    X = torch.from_numpy(X).to(device)

    output = model(X)

    _ , Predicated = torch .max(output,dim=1)

    tag = tags[Predicated.item()]

    probs = torch.softmax(output,dim=1)
    prob = probs[0][Predicated.item()]

    if prob.item() > 0.75:
        for intent in intents['intents']:
            if tag == intent['tag']:
                reply = random.choice(intent["response"])

                if "time" in reply:
                    pass

                if "date" in reply:
                    pass
                else:
                    speak(reply)

while True:         
    Main()              






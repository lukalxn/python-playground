import tkinter as tk
from tkinter import *
from langchain.llms import OpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
import pyfiglet
import sys

llm1=OpenAI(temperature=0.9)

sub=""

root=Tk()
root.title("FluentAi")
root.geometry('640x480')

tag=Label(root, text="Your Language Learning Companion", wraplength=500, justify="center")
tag.pack(pady=20)

intro=Label(root, text="Please specify what language you want to practice", wraplength=500, justify="center")
intro.pack(pady=20)

langinput = Entry(root,
                   width = 20)

inputskill = Entry(root,
                   width = 20)

inputanswer = Entry(root,
                    width = 20)
  
langinput.pack()

s1 = "Sure, I'm happy to help you practice "

s2 = ". Please specify your competency level."

prawmptuh = PromptTemplate(
   input_variables=["firstinput"],
   template="""{firstinput} am a person that only speaks English who has come to you for guidance on how to speak """ +langinput.get()+ """.
    You are a fluent speaker of """ +langinput.get()+ """ and an expert instructor that can work around any individual challenges I
    might have as a beginner to help me learn """ +langinput.get()+ """.
    Contruct an exercise for me at the skill level of """ +inputskill.get()+ """. Instruct me to answer the
    question. When I answer, take my response and let me know if my response was correct or not, then give me another exercise based 
    on fuzzy logic regarding how well I understood the previous question. Ensure that all of your questions have to do with this subject
    matter: """ +sub+ """."""
)

convo = ConversationChain(
    llm=OpenAI(temperature=0),
   memory=ConversationBufferMemory()
)

lang = langinput.get()

ques = convo.run(prawmptuh.format(firstinput="I"))

ques2 = convo.run(inputanswer.get())

question=Label(root, text=ques, wraplength=500, justify="center")


def lang1():
   tag["text"] = s1 + langinput.get() + s2
   langinput.pack_forget()
   B.pack_forget()
   intro.pack_forget()
   inputskill.pack()
   B2.pack(pady=20)

def lang2():
   tag["text"] = "Let's practice " + langinput.get() + " at the " + inputskill.get() + " level together. Please select an exercise to begin!"
   inputskill.pack_forget()
   B2.pack_forget()
   greetings.pack()
   food.pack()
   work.pack()
   culture.pack()
   day2day.pack()

def g1():
   tag["text"] = "Let's practice greetings in " + langinput.get() + " together."
   global sub
   sub = "greetings"
   greetings.pack_forget()
   food.pack_forget()
   work.pack_forget()
   culture.pack_forget()
   day2day.pack_forget()
   question.pack()
   inputanswer.pack()
   ans.pack()

def f1():
   tag["text"] = "Let's practice dining and food in " + langinput.get() + " together."
   global sub
   sub = "food and dining"
   greetings.pack_forget()
   food.pack_forget()
   work.pack_forget()
   culture.pack_forget()
   day2day.pack_forget()
   question.pack()
   inputanswer.pack()
   ans.pack()

def w1():
   tag["text"] = "Let's practice workplace lingo in " + langinput.get() + " together."
   global sub
   sub = "talking in the workplace"
   greetings.pack_forget()
   food.pack_forget()
   work.pack_forget()
   culture.pack_forget()
   day2day.pack_forget()
   question.pack()
   inputanswer.pack()
   ans.pack()

def c1():
   tag["text"] = "Let's practice discussing popular culture in " + langinput.get() + " together."
   global sub
   sub = "popular culture"
   greetings.pack_forget()
   food.pack_forget()
   work.pack_forget()
   culture.pack_forget()
   day2day.pack_forget()
   question.pack()
   inputanswer.pack()
   ans.pack()

def d2d1():
   tag["text"] = "Let's practice talking about day to day life in " + langinput.get() + " together."
   global sub
   sub = "discussing day to day life"
   greetings.pack_forget()
   food.pack_forget()
   work.pack_forget()
   culture.pack_forget()
   day2day.pack_forget()
   question.pack()
   inputanswer.pack()
   ans.pack()

def answer():
   tag["text"] = "Let's keep learning " + langinput.get() + " together."
   question["text"] = ques2


B = Button(root, text='Specify Language', command=lang1)
B2 = Button(root, text='Specify Competency', command=lang2)

greetings = Button(root, text='Greetings', command=g1)
food = Button(root, text='Food', command=f1)
work = Button(root, text='Work', command=w1)
culture = Button(root, text='Culture', command=c1)
day2day = Button(root, text='Daily Life', command=d2d1)

ans = Button(root, text='Answer', command=answer)

B.pack(pady=20)
root.mainloop()
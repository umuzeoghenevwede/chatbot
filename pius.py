import streamlit as st
import difflib


def pius(user_input):
    phares =['he', 'hello', 'hi','afa',
             'ml mean', 'define ml', 'what is ml', 'define machine learning', 'meaning of ml',
            'meaning of machine learning', 'explain ml',
             'who is the founder of machine learning', 'founder of machine learning', 'who is the founder', 'founder of ml', 'who made ml',
             'what is the history of machine learning', 'history of ml','highlight history of ml','explain the of ml',
             'what is the type of machine learrning', 'type of ml','list the type of ml','highlight type ml','explain the type of ml','exmaples of ml','type of ml',
             'which year did machine learning come into existence','year ml was founded','what year was machine learning first introduced',
             'what is the important of ml','The important of ml','highlight important of ml','tell me the important of machine learning','tell me the important of ml','explain the important of ml',
             'important of ml','tell me more on important of machine learning', 'more important of ml','more imprtant',
            'introduction to machine learning','explain introduction ml','what is introduction', 'highligth introduction','introduction on ml',
             'Can i learn machine learning without coding?','can i without coding?',
             'what is datatype','explain datatype','highligth datatype','datatype on ml']

    closes = difflib.get_close_matches(user_input.lower(),phares, n=1, cutoff=0.5)

    if closes:
        close_matches = closes[0]
        if close_matches in ['he', 'hello', 'hi','afa']:
            return "Hello,what can i do for you?"
        elif close_matches  in ['ml mean', 'define ml','what is ml','define machine learning','meaning of ml','meaning of machine learning','explain ml']:
            return "Machine learning is a alogrithms that learn from data to make prediction"
        elif close_matches  in ['who is the founder of machine learning', 'founder of machine learning', 'who is the founder', 'founder of ml', 'who made ml']:
            return "The founder is Arthur Samule"
        elif close_matches in ['what is the history of machine learning', 'history of ml','highlight history of ml','explain the of ml']:
            return "It is the evolution from ealy AI"
        elif close_matches in ['what is the type of machine learrning', 'type of ml','list the type of ml','highlight type ml','explain the type of ml','exmaples of ml','type of ml']:
            return "Type of Machine Learning: Supervised, Semi_Supervised, Unsupervised, reinforcement"
        elif close_matches  in ['which year did machine learning come into existence','year ml was founded','what year was machine learning first introduced']:
            return "1952"
        elif close_matches in ['what is the important of ml','The important of ml','highlight important of ml','tell me the important of machine learning','tell me the important of ml','explain the important of ml','important of ml']:
            return "machine learning allows the user to feed a computer algorithm an immense amount of data and have the computer analyze and make data-driven recommendations and decisions based on only the input data"
        elif close_matches in ['tell me more on important of machine learning', 'more important of ml','more imprtant']:
            return " data and algorithm."
        elif close_matches in ['introduction to machine learning','explain introduction ml','what is introduction', 'highligth introduction','introduction on ml']:
            return "A machine learning model is a type of mathematical model that, after being ['trained'] on a given dataset, can be used to make predictions or classifications on new data"
        elif close_matches  in ['Can i learn machine learning without coding?','can i without coding?']:
            return"The no-code machine learning approach, on the other hand, uses point-and-click interfaces to build models without any code."
        elif close_matches  in ['what is data type','explain data type','highligth data type','datatype on ml']:
            return "integer, float, string, and booleans"
        else:
            return "Sorry the information is not there"


st.header('machine learning')
w = st.text_input('pius')
st.sidebar.image('robot.jpg',caption='chatbot')

if w:
    response = pius(w)
    st.write(f'Chatbot:{response}')

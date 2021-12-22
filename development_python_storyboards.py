# !/usr/bin/python3

import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import WIN_CLOSED, Exit, button_color_to_tuple

import random
import webbrowser
import datetime
import os
import os.path




EXTERNAL_EDITOR = "code"  # command to start the external editor to edit markdown files


#TODO fix negotiation text so that it shows only the randomly selected text list_box doesn't work
#TODO add vocabulary column
#TODO set text file to open code and local file

#done set default image size to 150x150
#done load only images with thumbnail in the name
image_list = []


verbs_list = []
nouns_list = []
adjectives_list =[]

#negotiations
prepare_0_list = []
agenda_01_list = []
making_proposals_02_list = []
suggestions_03_list = []
agreeing_04_list = []
objecting_05_list = []
prioritizing_06_list = []
clarification_07_list = []
compromising_08_list = []
bargaining_09_list = []
postponing_10_list = []
concluding_11_list = []
seal_the_deal_12_list = []


### pros and cons
sum_of_pros= 0
sum_of_cons= 0
pros_cons_issues = []




### random function

import random
def primary():
    f = open("/home/dgd/Desktop/python_storyboard_flashcards/word_lists/adjectives.txt")
    quotes = f.readlines()
    f.close()

    sampling = random.sample(quotes, 1)
    for sample in sampling: print(sample)
primary()

# print(random_adjectives)




def reset_tenses():
    """
    clear the background color of the text objects
    """
    window["past_simple"].update(background_color = "lightblue")
    window["past_continuous"].update(background_color = "lightblue")
    window["past_perfect_continuous"].update(background_color = "lightblue")
    window["past_perfect"].update(background_color = "lightblue")
    window["present_simple"].update(background_color = "lightblue")
    window["present_continuous"].update(background_color = "lightblue")
    window["present_perfect_continuous"].update(background_color = "lightblue")
    window["present_perfect"].update(background_color = "lightblue")
    window["future_simple"].update(background_color = "lightblue")
    window["future_continuous"].update(background_color = "lightblue")
    window["future_perfect_continuous"].update(background_color = "lightblue")
    window["future_perfect"].update(background_color = "lightblue")



def split_filename(original_filename):
#TODO finish stripping prefixes
    """
    This will split a file name by _ so that a space will appear
    returns a string minus the file extension
    display only the text after the last slash

    """
    #DENNIS! complex words must be first eg. noun_animal_ BEFORE noun
    list_of_unwanted_words = ["idiom_",
                                "adjective_",
                                "noun_clothing_",
                                "noun_animal_",
                                "noun_food_",
                                "noun_",
                                "verb_"]

    #strip the last four chars from the text
    text = os.path.split(original_filename)[1]
    text = text[:-14]
    for unwanted in list_of_unwanted_words:
        if text.startswith(unwanted):
            text=text[len(unwanted):]
            break
    # if text.endswith("_thumbnail")

    return text.replace("_", " ")

def read_list_from_file():
    #TODO refactor this mess
    verbs_list.clear()
    nouns_list.clear()
    adjectives_list.clear()
    # negotations
    prepare_0_list.clear()      
    agenda_01_list.clear()
    making_proposals_02_list.clear()
    suggestions_03_list.clear()
    agreeing_04_list.clear()
    objecting_05_list.clear()
    
    prioritizing_06_list.clear()
    
    clarification_07_list.clear()
    
    compromising_08_list.clear()
    
    bargaining_09_list.clear()
    
    postponing_10_list.clear()
    
    concluding_11_list.clear()
    
    seal_the_deal_12_list.clear()
    # pros and cons
    pros_cons_issues.clear()
    
   

      
 
###tenses
    with open("word_lists/verbs.txt") as myfile:
        for line in myfile.readlines():
            verbs_list.append(line.strip())
    with open("/home/dgd/Desktop/python_storyboard_flashcards/word_lists/nouns.md") as myfile:
        for line in myfile.readlines():
            nouns_list.append(line.strip())
    with open("word_lists/adjectives.txt") as myfile:
        for line in myfile.readlines():
            adjectives_list.append(line.strip())
###start negotiations
    with open("negotiations_tab/prepare_0.md") as myfile:
        for line in myfile.readlines():
            prepare_0_list.append(line.strip())

    
    with open("negotiations_tab/agenda_01.md") as myfile:
        for line in myfile.readlines():
            agenda_01_list.append(line.strip())

    
    with open("negotiations_tab/making_proposals_02.md") as myfile:
        for line in myfile.readlines():
            making_proposals_02_list.append(line.strip())

    
    with open("negotiations_tab/suggestions_03.md") as myfile:
        for line in myfile.readlines():
            suggestions_03_list.append(line.strip())

    
    with open("negotiations_tab/agreeing_04.md") as myfile:
        for line in myfile.readlines():
            agreeing_04_list.append(line.strip())

    
    with open("negotiations_tab/objecting_05.md") as myfile:
        for line in myfile.readlines():
            objecting_05_list.append(line.strip())

    
    with open("negotiations_tab/prioritizing_06.md") as myfile:
        for line in myfile.readlines():
            prioritizing_06_list.append(line.strip())

    
    with open("negotiations_tab/clarification_07.md") as myfile:
        for line in myfile.readlines():
            clarification_07_list.append(line.strip())

    
    with open("negotiations_tab/compromising_08.md") as myfile:
        for line in myfile.readlines():
            compromising_08_list.append(line.strip())

    
    with open("negotiations_tab/bargaining_09.md") as myfile:
        for line in myfile.readlines():
            bargaining_09_list.append(line.strip())

    
    with open("negotiations_tab/postponing_10.md") as myfile:
        for line in myfile.readlines():
            postponing_10_list.append(line.strip())

    
    with open("negotiations_tab/concluding_11.md") as myfile:
        for line in myfile.readlines():
            concluding_11_list.append(line.strip())

    
    with open("negotiations_tab/seal_the_deal_12.md") as myfile:
        for line in myfile.readlines():
            seal_the_deal_12_list.append(line.strip())
### start pros and cons
    with open("pros_cons_tab/pros_cons_events.md") as myfile:
        for line in myfile.readlines():
            seal_the_deal_12_list.append(line.strip())


# TODO 
# try except to make sure the folder exists
# load the files from the target directory
# load only images with thumbnail in the name

for root, dirs, files in os.walk("/home/dgd/Desktop/python_storyboard_flashcards/random_images"):
   for name in files:
       if name.endswith("_thumbnail.png"):
           print(os.path.join(root, name))
           image_list.append(os.path.join(root, name))

#call the function
read_list_from_file()
# print(verbs_list)

# set the theme color
sg.ChangeLookAndFeel('GreenTan')

# ------ Menu Definition ------ #
menu_def = [['&File', ['&Open', '&Save', 'E&xit', 'Properties']],
            ['&Edit', ['Paste', ['Special', 'Normal', ], 'Undo'], ],
            ['&Help', 'help','&Open_docs'], ]

# ------ Column Definition ------ #
# column1 = [[sg.Text('Column 1', background_color='lightblue', justification='center', size=(10, 1))],
#            [sg.Spin(values=('Spin Box 1', '2', '3'), initial_value='Spin Box 1',key = "Spin1",enable_events=True)],
#            [sg.Spin(values=('Spin Box 1', '2', '3'), initial_value='Spin Box 2')],
#            [sg.Spin(values=('Spin Box 1', '2', '3'), initial_value='Spin Box 3')]]

# the vocab will go here
# vocabulary_column = [sg.Multiline(default_text='This is the default Text should you decide not to type anything', size=(35, 3)),
#      sg.Multiline(default_text='A second multi-line', size=(35, 3))]
#header Vocabulary

# column_vocab = sg.Column([
#                         sg.Multiline(default_text='A second multi-line', size=(5, 5))
#                           ])

timeline_column_one = sg.Column([
                                [sg.Text("timeline column one",
                                key="past1",
                                size = (20,2),
                                enable_events=True,
                                tooltip='Past events1')],

###
                                [sg.Text("past2 column one",
                                key="past2",
                                size = (20,2),
                                enable_events=True,
                                tooltip='Past events2')], 
###
                                [sg.Text("past3",
                                key="past3",
                                size = (20,2),
                                enable_events=True,
                                tooltip='past3 column one')],
###
                                [sg.Text("now column one",
                                key="now_event",
                                size = (20,2),
                                enable_events=True,
                                tooltip='now column one')],
###
                                [sg.Text("timeline column one",
                                key="future1",
                                size = (20,2),
                                enable_events=True,
                                tooltip='future1 event')],
###
                                [sg.Text("timeline column one",
                                key="future2",
                                size = (20,2),
                                enable_events=True,
                                tooltip='future2 event')],
###
                                [sg.Text("timeline column one",
                                key="future3",
                                size = (20,2),
                                enable_events=True,
                                tooltip='future3 event')],

                                ])



timeline_column_two = sg.Column([
                                [sg.Text("timeline column one",
                                key="event1",
                                size = (30,2),
                                enable_events=True,
                                tooltip='This is a tool tip timeline column one')],

###
                                [sg.Text("past2 column one",
                                key="event2",
                                size = (30,2),
                                enable_events=True,
                                tooltip='This is a tool tip timeline column one')], 
###
                                [sg.Text("eventpast3",
                                key="event3",
                                size = (30,2),
                                enable_events=True,
                                tooltip='This is a tool tip timeline column one')],
###
                                [sg.Text("now column one",
                                key="event4",
                                size = (30,2),
                                enable_events=True,
                                tooltip='This is a tool tip timeline column one')],
###
                                [sg.Text("timeline column one",
                                key="event5",
                                size = (30,2),
                                enable_events=True,
                                tooltip='This is a tool tip timeline column one')],
###
                                [sg.Text("timeline column one",
                                key="event6",
                                size = (30,2),
                                enable_events=True,
                                tooltip='This is a tool tip timeline column one')],
###
                                [sg.Text("timeline column one",
                                key="event7",
                                size = (30,2),
                                enable_events=True,
                                tooltip='This is a tool tip timeline column one')],

                                ])


timeline_column_three = sg.Column([
                                [sg.Text("timeline column one",
                                key="adverb1",
                                size = (30,2),
                                enable_events=True,
                                tooltip='This is a tool tip for adverb1')],

###
                                [sg.Text("past2 column one",
                                key="adverb2",
                                size = (30,2),
                                enable_events=True,
                                tooltip='This is a tool tip for adverb2')], 
###
                                [sg.Text("eventpast3",
                                key="adverb3",
                                size = (30,2),
                                enable_events=True,
                                tooltip='This is a tool tip timeline column one')],
###
                                [sg.Text("now column one",
                                key="adverb4",
                                size = (30,2),
                                enable_events=True,
                                tooltip='This is a tool tip timeline column one')],
###
                                [sg.Text("timeline column one",
                                key="adverb5",
                                size = (30,2),
                                enable_events=True,
                                tooltip='This is a tool tip timeline column one')],
###
                                [sg.Text("timeline column one",
                                key="adverb6",
                                size = (30,2),
                                enable_events=True,
                                tooltip='This is a tool tip timeline column one')],
###
                                [sg.Text("timeline column one",
                                key="adverb7",
                                size = (30,2),
                                enable_events=True,
                                tooltip='This is a tool tip timeline column one')],

                                ])


timeline_column_four = sg.Column([
                                ###
                                [
                                    sg.Button("place holder",
                                                key = "adverb1change",
                                                size = (10,2),

                                                ),                            
                                ],  
[
                                    sg.Button("place holder",
                                                key = "adverb2change",
                                                size = (10,2),
                                                ),                            
                                ],[
                                    sg.Button("place holder",
                                                key = "adverb3change",
                                                size = (10,2),
                                                ),                            
                                ],[
                                    sg.Button("place holder",
                                                key = "adverb4change",
                                                size = (10,2),
                                                ),                            
                                ],[
                                    sg.Button("place holder",
                                                key = "adverb5change",
                                                size = (10,2),
                                                ),                            
                                ],
                                
                                [
                                    sg.Button("place holder",
                                                key = "adverb6change",
                                                size = (10,2),
                                                ),                            
                                ],

                                [
                                    sg.Button("place holder 7",
                                                key = "adverb7change",
                                                size = (10,2),
                                                ),                            
                                ],

                                ])





tenses_tab_column_left = sg.Column([
                            #header
                            [sg.Text("past simple",
                            key="past_simple",
                            enable_events=True,
                            
                            tooltip='Past Simple - I built a new garage last month.')],

                            [sg.Text("past continuous",
                            key="past_continuous", 
                            enable_events=True,

                            tooltip='Past Continuous - I was building a wall yesterday.')],
                            
                            [sg.Text("past perfect",
                            key="past_perfect",
                            enable_events=True,

                            tooltip='Past Perfect - By the time my last company went bust we had already built the new shopping center.')],

                            [sg.Text("past perfect continuous",
                            key="past_perfect_continuous",
                            enable_events=True,
                            tooltip= 'Past Perfect Continuous - We had been building the new\n shopping center for 2 months when we heard about the bankruptcy.'
                            )],

                            [sg.Multiline('text', 
                            key= "text1a",
                            size=(17,1), 
                            font=("Helvetica", 12)) 
                            ],

                            [sg.Image(filename="",
                            key='canvas1a')
                            ],
#####################                            
                            [sg.Multiline('text', 
                            key= "text1b",
                            size=(17,1), 
                            font=("Helvetica", 12)), 
                            ],

                        
                            [sg.Image(filename="",
                            key='canvas1b'),]
                        ])

tenses_tab_column_center = sg.Column([
                            #header
                            [sg.Text("present simple",
                            key="present_simple",
                            enable_events=True,
                            tooltip='Present Simple - I usually build commercial buildings.',
                            )],


                            [sg.Text("present continuous",
                            key="present_continuous",
                            enable_events=True,
                            tooltip='Present Continuous - It is Monday morning and I am building a wall.',
                            )],


                            [sg.Text("present perfect",
                            key="present_perfect",
                            enable_events=True,
                            tooltip='Present Perfect Simple - I have already built two shopping centers this year.',                            
                            )],


                            [sg.Text("present perfect continuous",
                            key="present_perfect_continuous",
                            enable_events=True,
                            tooltip='Present Perfect Continuous - I have been building this shopping centre since we won the contract.'
                            )],

                            [sg.Multiline('\U0001F934', 
                            key= "text2a",
                            size=(17,1), 
                            font=("Helvetica", 12)) 
                            ],

                            # [sg.Text('\U0001F934', 
                            # key= "text2a",
                            # size=(17,1), 
                            # font=("Helvetica", 12)) 
                            # ],

                            [sg.Image(filename="",
                            key='canvas2a')
                            ],
                            
                            [sg.Multiline('\u0394', 
                            key= "text2b",size=(17,1), 
                            font=("Helvetica", 12)), 
                            ],

                        
                            [sg.Image(filename="",
                            key='canvas2b'),]

                            ])

tenses_tab_column_right = sg.Column([ #header
                            [sg.Text("future simple",
                            key="future_simple",
                            enable_events=True,
                            tooltip="""Future Simple - I think I'll build my own\n house when I can afford to.""",)],

                            [sg.Text("future continuous",
                            enable_events=True,
                            key="future_continuous",
                            tooltip="""Future Continuous - I'm building a new garage tomorrow.""")],
                            
                            [sg.Text("future perfect",
                            key="future_perfect",
                            enable_events=True,
                            tooltip="""Future Perfect Simple - I hope I will have already built my \nown house by the time I am 40.""")],
                            
                            [sg.Text("future perfect continuous",
                            key="future_perfect_continuous",
                            enable_events=True,
                            tooltip="""Future Perfect Continuous - This time next week I will have\n been building this shopping center for two months.""")],

                            [sg.Multiline('\u0394', 
                            key= "text3a",
                            size=(17,1), 
                            font=("Helvetica", 12)) 
                            ],

                            [sg.Image(filename="",
                            key='canvas3a')
                            ],
                            
                            [sg.Multiline('\u0394', 
                            key= "text3b",
                            size=(17,1), 
                            font=("Helvetica", 12)), 
                            ],

                        
                            [sg.Image(filename="",
                            key='canvas3b'),]
                        ])

tab_one= sg.Tab ("adj noun reg verb", [
    #trying to get random text to display here
    # It's not working
    [sg.Text(primary(),size=(17,1)),sg.Text("adj",size=(17,1)),sg.Text("noun",size=(17,1)),],

    [sg.Text("verb",size=(17,1)),sg.Text("adj",size=(17,1)),sg.Text("noun",size=(17,1)),],

        [  # sg.Text(verbs_list,key="verbs_list_box",enable_events=True,size=(15,15)),
            sg.Listbox(verbs_list,key="verbs_list_box",enable_events=True,change_submits=True,size=(15,15)),
            sg.Listbox(adjectives_list,key="adjectives_list_box",enable_events=True,change_submits=True,size=(15,15)),
            sg.Listbox(nouns_list,key="nouns_list_box",enable_events=True,change_submits=True,size=(15,15)),
            
            sg.Button("reload"),sg.Button("randomize"),
        
        ],
    

    ])

tab_two= sg.Tab ("tenses tab", [
        #create button
    [sg.Button("shuffle the images",
                key = "image_shuffle",
                ),
   
    sg.Button("comparatives"),
    sg.Button("idioms"),
    sg.Button("prepositional phrases"),
    sg.Button("conditionals"),
    sg.Button("modals"),

                ],


    [tenses_tab_column_left, tenses_tab_column_center,tenses_tab_column_right],

    ])

#### negotiation TAB
#TODO add edit button so I can quickly go in and add entries

tab_three = sg.Tab("negotiation",
[
        
[
    sg.Text("prepare_0"),
    sg.Text(
            text= "Have your prepared enough?!",
            key="prepare_0_list_box",
            enable_events=True,
            font=("Helvetica", 14),
            justification = "center",
            size=(55,1)
            ),
    sg.Button('edit prepare_0'),

],

[
    sg.Text("agenda_01"),
    sg.Text(
            text= "Have your prepared enough?!",
            key="agenda_01_list_box",
            enable_events=True,
            font=("Helvetica", 14),
            justification = "center",
            size=(55,1)
            ),
    sg.Button('edit agenda_01'),

],

[
    sg.Text("making_proposals_02"),
    sg.Text(
            text= "Have your prepared enough?!",
            key="making_proposals_02_list_box",
            enable_events=True,
            font=("Helvetica", 14),
            justification = "center",
            size=(55,1)
            ),
    sg.Button('edit making_proposals_02'),

],

[
    sg.Text("suggestions_03"),
    sg.Text(
            text= "Have your prepared enough?!",
            key="suggestions_03_list_box",
            enable_events=True,
            font=("Helvetica", 14),
            justification = "center",
            size=(55,1)
            ),
    sg.Button('edit suggestions_03'),

],

[
    sg.Text("agreeing_04"),
    sg.Text(
            text= "Have your prepared enough?!",
            key="agreeing_04_list_box",
            enable_events=True,
            font=("Helvetica", 14),
            justification = "center",
            size=(55,1)
            ),
    sg.Button('edit agreeing_04'),

],

[
    sg.Text("objecting_05"),
    sg.Text(
            text= "Have your prepared enough?!",
            key="objecting_05_list_box",
            enable_events=True,
            font=("Helvetica", 14),
            justification = "center",
            size=(55,1)
            ),
    sg.Button('edit objecting_05'),

],

[
    sg.Text("prioritizing_06"),
    sg.Text(
            text= "Have your prepared enough?!",
            key="prioritizing_06_list_box",
            enable_events=True,
            font=("Helvetica", 14),
            justification = "center",
            size=(55,1)
            ),
    sg.Button('edit prioritizing_06'),

],

[
    sg.Text("clarification_07"),
    sg.Text(
            text= "Have your prepared enough?!",
            key="clarification_07_list_box",
            enable_events=True,
            font=("Helvetica", 14),
            justification = "center",
            size=(55,1)
            ),
    sg.Button('edit clarification_07'),

],

[
    sg.Text("compromising_08"),
    sg.Text(
            text= "Have your prepared enough?!",
            key="compromising_08_list_box",
            enable_events=True,
            font=("Helvetica", 14),
            justification = "center",
            size=(55,1)
            ),
    sg.Button('edit compromising_08'),

],

[
    sg.Text("bargaining_09"),
    sg.Text(
            text= "Have your prepared enough?!",
            key="bargaining_09_list_box",
            enable_events=True,
            font=("Helvetica", 14),
            justification = "center",
            size=(55,1)
            ),
    sg.Button('edit bargaining_09'),

],

[
    sg.Text("postponing_10"),
    sg.Text(
            text= "Have your prepared enough?!",
            key="postponing_10_list_box",
            enable_events=True,
            font=("Helvetica", 14),
            justification = "center",
            size=(55,1)
            ),
    sg.Button('edit postponing_10'),

],

[
    sg.Text("concluding_11"),
    sg.Text(
            text= "Have your prepared enough?!",
            key="concluding_11_list_box",
            enable_events=True,
            font=("Helvetica", 14),
            justification = "center",
            size=(55,1)
            ),
    sg.Button('edit concluding_11'),

],

[
    sg.Text("seal_the_deal_12"),
    sg.Text(
            text= "Have your prepared enough?!",
            key="seal_the_deal_12_list_box",
            enable_events=True,
            font=("Helvetica", 14),
            justification = "center",
            size=(55,1)
            ),
    sg.Button('edit seal_the_deal_12'),

],
###
    
]


)

####################################3
timeline_tab= sg.Tab ("timeline tenses tab", 
        #create button
    [
    
    [sg.Text('set start date YYYY,DD,MM e.g. 2020, 1, 30', size =(15, 1)), sg.InputText(key="input_user_start_date"),sg.Text('set end date YYYY,DD,MM e.g. 2020, 1, 30', size =(20, 1)), sg.InputText(key="input_user_end_date")],
    [sg.Button("change time"), sg.Button("randomize events"),   ],
    [timeline_column_one,timeline_column_two,timeline_column_three,timeline_column_four],
    



    ])
####################
### pros_cons_tab

pros_cons_tab= sg.Tab ("pros cons", 
        #create button
    [

        [sg.Text("pros and cons issues goes here",size=(40,1),key="pros_cons_issues",enable_events=True,font=("helvetica",20)),sg.Button("edit pros cons issues")],


[
        sg.Text('pros', size =(4, 1)), sg.InputText(key="pros_0",size=(40,1)), sg.Slider(enable_events=True,key= "slider_pros_0", orientation = "horizontal",size = (6,10),),
        
        sg.Text('cons', size =(4, 1)), sg.InputText(key="cons_0",size=(40,1)), sg.Slider(enable_events=True,key= "slider_cons_0", orientation = "horizontal",size = (6,10),),
        ],
[
        sg.Text('pros', size =(4, 1)), sg.InputText(key="pros_1",size=(40,1)), sg.Slider(enable_events=True,key= "slider_pros_1", orientation = "horizontal",size = (6,10),),
        
        sg.Text('cons', size =(4, 1)), sg.InputText(key="cons_1",size=(40,1)), sg.Slider(enable_events=True,key= "slider_cons_1", orientation = "horizontal",size = (6,10),),
        ],
[
        sg.Text('pros', size =(4, 1)), sg.InputText(key="pros_2",size=(40,1)), sg.Slider(enable_events=True,key= "slider_pros_2", orientation = "horizontal",size = (6,10),),
        
        sg.Text('cons', size =(4, 1)), sg.InputText(key="cons_2",size=(40,1)), sg.Slider(enable_events=True,key= "slider_cons_2", orientation = "horizontal",size = (6,10),),
        ],
[
        sg.Text('pros', size =(4, 1)), sg.InputText(key="pros_3",size=(40,1)), sg.Slider(enable_events=True,key= "slider_pros_3", orientation = "horizontal",size = (6,10),),
        
        sg.Text('cons', size =(4, 1)), sg.InputText(key="cons_3",size=(40,1)), sg.Slider(enable_events=True,key= "slider_cons_3", orientation = "horizontal",size = (6,10),),
        ],
[
        sg.Text('pros', size =(4, 1)), sg.InputText(key="pros_4",size=(40,1)), sg.Slider(enable_events=True,key= "slider_pros_4", orientation = "horizontal",size = (6,10),),
        
        sg.Text('cons', size =(4, 1)), sg.InputText(key="cons_4",size=(40,1)), sg.Slider(enable_events=True,key= "slider_cons_4", orientation = "horizontal",size = (6,10),),
        ],
[
        sg.Text('pros', size =(4, 1)), sg.InputText(key="pros_5",size=(40,1)), sg.Slider(enable_events=True,key= "slider_pros_5", orientation = "horizontal",size = (6,10),),
        
        sg.Text('cons', size =(4, 1)), sg.InputText(key="cons_5",size=(40,1)), sg.Slider(enable_events=True,key= "slider_cons_5", orientation = "horizontal",size = (6,10),),
        ],
        [
        sg.Text('pros', size =(4, 1)), sg.InputText(key="pros_6",size=(40,1)), sg.Slider(enable_events=True,key= "slider_pros_6", orientation = "horizontal",size = (6,10),),
        
        sg.Text('cons', size =(4, 1)), sg.InputText(key="cons_6",size=(40,1)), sg.Slider(enable_events=True,key= "slider_cons_6", orientation = "horizontal",size = (6,10),),
        ],

### summary of slider
        [sg.Text("",size=(44,1)), sg.Text("Sum of pros",justification="left", size= (10,1)), sg.Text("?",key="sum_of_pros"),
sg.Text("",size=(34,1)), sg.Text("Sum of cons",justification="left", size=(10,1)), sg.Text("?",key="sum_of_cons"),
        ],

### analysis
        [sg.Multiline(key="analysis",size =(40,10),font =("helvetica", 14)), sg.Button("save to CSV")],
        



    ])





layout = [
    
    #TODO column with image and text 
    [sg.Menu(menu_def, tearoff=True)],
    # [sg.Canvas(size=(500, 200), key='canvas')],
    #done use image resizer on images
    
    [sg.TabGroup([[tab_one,tab_two,tab_three,timeline_tab, pros_cons_tab]],key="tabgroup")],
    

    
]
    


window = sg.Window('Development! Learn English with Dennis', 
                    
                    layout, 
                    background_color="lightblue",
                    size = (1100,600),
                    location=(2000, 1700),
                    default_element_size=(35, 1), 
                    grab_anywhere=True)

while True:


    event, values = window.read()


    if event == "Open_docs":
        webbrowser.open("https://pysimplegui.readthedocs.io/en/latest/",new=1,autoraise=True )
        # pass

# pros and cons events
    #shuffle events
    if event == "pros_cons_issues":
        read_list_from_file()
        with open("/home/dgd/Desktop/python_storyboard_flashcards/pros_cons_tab/pros_cons_events.md") as myfile:
            lines = myfile.readlines()
        window["pros_cons_issues"].update(random.choice(lines).strip()  )


    #edit items
    if event == "edit pros cons issues":
        os.system("{} {}".format(EXTERNAL_EDITOR, "/home/dgd/Desktop/python_storyboard_flashcards/pros_cons_tab/pros_cons_events.md"))



    # fire on all sliders
    if "slider" in event:
        sum_of_pros = values["slider_pros_0"] + values["slider_pros_1"]+ values["slider_pros_2"]+ values["slider_pros_3"]+ values["slider_pros_4"]+ values["slider_pros_5"]+ values["slider_pros_6"]
        sum_of_cons = values["slider_cons_0"] + values["slider_cons_1"]+ values["slider_cons_2"]+ values["slider_cons_3"]+ values["slider_cons_4"]+ values["slider_cons_5"]+ values["slider_cons_6"]
        # sg.PopupOK(sum_of_pros)
        window["sum_of_pros"].update(sum_of_pros)
        window["sum_of_cons"].update(sum_of_cons)



# shuffle images

    if event == "image_shuffle":
        random.shuffle(image_list)
        window["canvas1a"].update(filename=image_list[0])
        window["canvas1b"].update(filename=image_list[1])
        window["canvas2a"].update(filename=image_list[2])
        window["canvas2b"].update(filename=image_list[3])
        window["canvas3a"].update(filename=image_list[4])
        window["canvas3b"].update(filename=image_list[5])
        window["text1a"].update(split_filename(image_list[0]))
        window["text1b"].update(split_filename(image_list[1]))
        window["text2a"].update(split_filename(image_list[2]))
        window["text2b"].update(split_filename(image_list[3]))
        window["text3a"].update(split_filename(image_list[4]))
        window["text3b"].update(split_filename(image_list[5]))
        
# button in left tab
    if event == 'reload':
        read_list_from_file()
        window["verbs_list_box"].update(values=verbs_list)
        window["nouns_list_box"].update(values=nouns_list)
        window["adjectives_list_box"].update(values=adjectives_list)

# button in left tab
    if event == 'randomize':
        window["verbs_list_box"].update(set_to_index=random.randint(0,len(verbs_list)-1))
        window["nouns_list_box"].update(set_to_index=random.randint(0,len(nouns_list)-1))
        window["adjectives_list_box"].update(set_to_index=random.randint(0,len(adjectives_list)-1))
        # (set_to_index=random.randint(0,len(verbs_list)-1))



### Horst's random selection


    if event == 'easy':
        reset_tenses()
        window[random.choice(["past_simple","past_continuous"])].update(background_color = 'white')
        window[random.choice(["present_simple","present_continuous"])].update(background_color = 'white')
        window[random.choice(["future_simple","future_continuous"])].update(background_color = 'white')



    if event == 'medium':
        reset_tenses()
        window[random.choice(["past_simple","past_continuous",])].update(background_color = 'white')
        window[random.choice(["present_simple","present_perfect","present_continuous",])].update(background_color = 'white')
        window[random.choice(["future_simple","future_continuous",])].update(background_color = 'white')
        
    if event == 'hard':
        reset_tenses()
        window[random.choice(["past_simple",   "past_continuous",  "past_perfect","past_perfect_continuous",]) ].update(background_color = 'white')
        window[random.choice(["present_simple",   "present_continuous",   "present_perfect",]) ].update(background_color = 'white')
        window[random.choice(["future_simple",   "future_continuous",  "future_perfect",]) ].update(background_color = 'white')
    
    if event == 'elite':
        reset_tenses()
        window[random.choice(["past_simple",   "past_continuous",  "past_perfect", "past_perfect_continuous"])].update(background_color = 'white')
        window[random.choice(["present_simple",   "present_continuous","present_perfect_continuous",  "present_perfect",]) ].update(background_color = 'white')
        window[random.choice(["future_simple",   "future_continuous",  "future_perfect","future_perfect_continuous"]) ].update(background_color = 'white')



#menu items
    if event == 'help':
    #     sg.popup_notify("Some text",location = (900,900))
    #if event == "edit making_proposals_02":
        os.system("{} {}".format(EXTERNAL_EDITOR, "/home/dgd/Desktop/python_storyboard_flashcards/README.md"))


### past tense events


    if event == "past_simple":
        webbrowser.open("https://docs.google.com/spreadsheets/d/1NkmOcQcNU8Dirk_rM04yEF5CS9yaSnYGip0Tyq0AkIU/edit?usp=sharing",new=1,autoraise=True )


    if event == "past_continuous":
        webbrowser.open("https://docs.google.com/spreadsheets/d/14FxeIfy6HA1nFK1HA-t301v-7x2Hf4BoYxnu1hKtm1M/edit?usp=sharing",new=1,autoraise=True )

    if event == "past_perfect_continuous":
        webbrowser.open("https://docs.google.com/spreadsheets/d/1eQYZQA9qWQLEjEwwgBv6hupkzLELxVWXwZEukJ2He2I/edit?usp=sharing",new=1,autoraise=True )

    if event == "past_perfect":
        webbrowser.open("https://docs.google.com/spreadsheets/d/1KzJ68cM0VBsthrfsGJRIXCV4MWXcSIcDdDWfH-Gfl3M/edit?usp=sharing",new=1,autoraise=True )

### present events
    
    if event == "present_simple":
        webbrowser.open("https://docs.google.com/spreadsheets/d/1xv0ZFe6_l66spkXWPyWrzu5k1KPNb3OWKL52Xg71DuE/edit?usp=sharing",new=1,autoraise=True )


    if event == "present_continuous":
        webbrowser.open("https://docs.google.com/spreadsheets/d/1SKgIK56P0qla0l2KEuii35AjPWrg4YJGYqw2prV7BIw/edit?usp=sharing",new=1,autoraise=True )

    if event == "present_perfect_continuous":
        webbrowser.open("https://docs.google.com/spreadsheets/d/1mQoBCdNpjYee6lX5sxwz1oS2xpmkVeimY-CVUnRgxoA/edit?usp=sharing",new=1,autoraise=True )

    if event == "present_perfect":
        webbrowser.open("https://docs.google.com/spreadsheets/d/1vAlXCM5dD8EVvt9W_YYz7ZNN6UZumT0MClnazfF7oGY/edit?usp=sharing",new=1,autoraise=True )


### future tenses


    if event == "future_simple":
        webbrowser.open("https://docs.google.com/spreadsheets/d/1ipHIxokBppXG_BXsVZ02J-HbXtzA5xLLPSm6prZlZ2Q/edit?usp=sharing",new=1,autoraise=True )


    if event == "future_continuous":
        webbrowser.open("https://docs.google.com/spreadsheets/d/1ggv9CToDdZBcjTjDF92r5AYOzAzvFhWZSFuraUdT5mE/edit?usp=sharing",new=1,autoraise=True )

    if event == "future_perfect_continuous":
        webbrowser.open("https://docs.google.com/spreadsheets/d/1ePg18VgsvrrIv1JKcuF6KDTak3jQ46A1ALyv4ElHI5U/edit?usp=sharing",new=1,autoraise=True )

    if event == "future_perfect":
        webbrowser.open("https://docs.google.com/spreadsheets/d/1aq_OhW0JRTGNrowS7Q4RCl52cHx7S9Upha7z9VYp-3o/edit?usp=sharing",new=1,autoraise=True )

    
    if event == "comparatives":
        webbrowser.open("https://docs.google.com/spreadsheets/d/150r972lV3ogmCmlmpjkHNOoX6tIO26Gd4EYzdfCGUW4/edit?usp=sharing",new=1,autoraise=True )

    if event == "idioms":
        webbrowser.open("https://docs.google.com/spreadsheets/d/15u8oWVJNmjvfkOOvF696E1o-Tz6lBZkr7ctJ6CBLYVk/edit?usp=sharing",new=1,autoraise=True )


    if event == "prepositional phrases":
        webbrowser.open("https://docs.google.com/spreadsheets/d/1R3rYYL7H7wC86Z8HeNFy_QzCvqXJSv6w8tKb3wsM30E/edit?usp=sharing",new=1,autoraise=True )

    if event == "conditionals":
        webbrowser.open("https://docs.google.com/spreadsheets/d/1VKcLMETbyEnWpVEeXc5j5NjEa_UF0ydMBInS-ljoWhs/edit?usp=sharing",new=1,autoraise=True )


    if event == "modals":
        webbrowser.open("https://docs.google.com/document/d/1KrQamEPrHG4bMQrHc4XJtys-P23iaRC-8iDWXL8sbfY/edit?usp=sharing",new=1,autoraise=True )


### timeline events



    if event == "edit timeline events":
                os.system("{} {}".format(EXTERNAL_EDITOR, "/home/dgd/Desktop/python_storyboard_flashcards/timeline_support_tab/timeline_events.md"))

    if event == "edit adverbs of time phrases":
                os.system("{} {}".format(EXTERNAL_EDITOR, "/home/dgd/Desktop/python_storyboard_flashcards/timeline_support_tab/grammar_adverbs_of_time.md"))

    if event == "adverb1":
        with open("/home/dgd/Desktop/python_storyboard_flashcards/timeline_support_tab/grammar_adverbs_of_time.md") as myfile:
            lines = myfile.readlines()
        window["adverb1"].update(random.choice(lines).strip()  )


    if event == "adverb2":
            with open("/home/dgd/Desktop/python_storyboard_flashcards/timeline_support_tab/grammar_adverbs_of_time.md") as myfile:
                lines = myfile.readlines()
            window["adverb2"].update(random.choice(lines).strip()  )


    if event == "adverb3":
            with open("/home/dgd/Desktop/python_storyboard_flashcards/timeline_support_tab/grammar_adverbs_of_time.md") as myfile:
                lines = myfile.readlines()
            window["adverb3"].update(random.choice(lines).strip()  )


    if event == "adverb4":
            with open("/home/dgd/Desktop/python_storyboard_flashcards/timeline_support_tab/grammar_adverbs_of_time.md") as myfile:
                lines = myfile.readlines()
            window["adverb4"].update(random.choice(lines).strip()  )


    if event == "adverb5":
            with open("/home/dgd/Desktop/python_storyboard_flashcards/timeline_support_tab/grammar_adverbs_of_time.md") as myfile:
                lines = myfile.readlines()
            window["adverb5"].update(random.choice(lines).strip()  )


    if event == "adverb6":
            with open("/home/dgd/Desktop/python_storyboard_flashcards/timeline_support_tab/grammar_adverbs_of_time.md") as myfile:
                lines = myfile.readlines()
            window["adverb6"].update(random.choice(lines).strip()  )


    if event == "adverb7":
            with open("/home/dgd/Desktop/python_storyboard_flashcards/timeline_support_tab/grammar_adverbs_of_time.md") as myfile:
                lines = myfile.readlines()
            window["adverb7"].update(random.choice(lines).strip()  )

    if event == "event1":
        with open("/home/dgd/Desktop/python_storyboard_flashcards/timeline_support_tab/timeline_events.md") as myfile:
            lines = myfile.readlines()
        window["event1"].update(random.choice(lines).strip()  )


    if event == "event2":
            with open("/home/dgd/Desktop/python_storyboard_flashcards/timeline_support_tab/timeline_events.md") as myfile:
                lines = myfile.readlines()
            window["event2"].update(random.choice(lines).strip()  )


    if event == "event3":
            with open("/home/dgd/Desktop/python_storyboard_flashcards/timeline_support_tab/timeline_events.md") as myfile:
                lines = myfile.readlines()
            window["event3"].update(random.choice(lines).strip()  )


    if event == "event4":
            with open("/home/dgd/Desktop/python_storyboard_flashcards/timeline_support_tab/timeline_events.md") as myfile:
                lines = myfile.readlines()
            window["event4"].update(random.choice(lines).strip()  )


    if event == "event5":
            with open("/home/dgd/Desktop/python_storyboard_flashcards/timeline_support_tab/timeline_events.md") as myfile:
                lines = myfile.readlines()
            window["event5"].update(random.choice(lines).strip()  )


    if event == "event6":
            with open("/home/dgd/Desktop/python_storyboard_flashcards/timeline_support_tab/timeline_events.md") as myfile:
                lines = myfile.readlines()
            window["event6"].update(random.choice(lines).strip()  )


    if event == "event7":
            with open("/home/dgd/Desktop/python_storyboard_flashcards/timeline_support_tab/timeline_events.md") as myfile:
                lines = myfile.readlines()
            window["event7"].update(random.choice(lines).strip()  )








    if event == "edit prepare_0":
        os.system("{} {}".format(EXTERNAL_EDITOR, "/home/dgd/Desktop/python_storyboard_flashcards/negotiations_tab/prepare_0.md"))

    if event == "change time":
        now =datetime.date.today().strftime("%Y %B %d")
        window["now_event"].update(now)
        #past
        delta1= random.randint(1,7)
        delta2= random.randint(10,30)
        delta3= random.randint(30,90)
        past3 = datetime.date.today()-datetime.timedelta(delta1)
        window["past3"].update(past3.strftime("%Y %B %d"))
        past2 =  past3 -datetime.timedelta(delta2)
        window["past2"].update(past2.strftime("%Y %B %d"))
        past1 =  past2 -datetime.timedelta(delta3)
        window["past1"].update(past1.strftime("%Y %B %d"))
        #future
        delta1= random.randint(1,7)
        delta2= random.randint(10,30)
        delta3= random.randint(30,90)
        future1 =   datetime.date.today()+datetime.timedelta(delta1)
        window["future1"].update(future1.strftime("%Y %B %d"))
        future2 =   future1 + datetime.timedelta(delta2)
        window["future2"].update(future2.strftime("%Y %B %d"))
        future3 =   future2 + datetime.timedelta(delta3)
        window["future3"].update(future3.strftime("%Y %B %d"))

    if event == "randomize events":
        with open("/home/dgd/Desktop/python_storyboard_flashcards/timeline_support_tab/timeline_events.md") as myfile:
            lines = myfile.readlines()
        random.shuffle(lines)
        # print(lines)
        window["event1"].update(lines[0].strip())
        window["event2"].update(lines[1].strip())
        window["event3"].update(lines[2].strip())
        window["event4"].update(lines[3].strip())
        window["event5"].update(lines[4].strip())
        window["event6"].update(lines[5].strip())
        window["event7"].update(lines[6].strip())



### negotiation events

###prepare_0
    if event == "prepare_0_list_box":
            with open("/home/dgd/Desktop/python_storyboard_flashcards/negotiations_tab/prepare_0.md") as myfile:
                lines = myfile.readlines()
            window["prepare_0_list_box"].update(random.choice(lines).strip()  )
    ###


    ###agenda_01
    if event == "agenda_01_list_box":
            with open("/home/dgd/Desktop/python_storyboard_flashcards/negotiations_tab/agenda_01.md") as myfile:
                lines = myfile.readlines()
            window["agenda_01_list_box"].update(random.choice(lines).strip()  )
    ###


    ###making_proposals_02
    if event == "making_proposals_02_list_box":
            with open("/home/dgd/Desktop/python_storyboard_flashcards/negotiations_tab/making_proposals_02.md") as myfile:
                lines = myfile.readlines()
            window["making_proposals_02_list_box"].update(random.choice(lines).strip()  )
    ###


    ###suggestions_03
    if event == "suggestions_03_list_box":
            with open("/home/dgd/Desktop/python_storyboard_flashcards/negotiations_tab/suggestions_03.md") as myfile:
                lines = myfile.readlines()
            window["suggestions_03_list_box"].update(random.choice(lines).strip()  )
    ###


    ###agreeing_04
    if event == "agreeing_04_list_box":
            with open("/home/dgd/Desktop/python_storyboard_flashcards/negotiations_tab/agreeing_04.md") as myfile:
                lines = myfile.readlines()
            window["agreeing_04_list_box"].update(random.choice(lines).strip()  )
    ###


    ###objecting_05
    if event == "objecting_05_list_box":
            with open("/home/dgd/Desktop/python_storyboard_flashcards/negotiations_tab/objecting_05.md") as myfile:
                lines = myfile.readlines()
            window["objecting_05_list_box"].update(random.choice(lines).strip()  )
    ###


    ###prioritizing_06
    if event == "prioritizing_06_list_box":
            with open("/home/dgd/Desktop/python_storyboard_flashcards/negotiations_tab/prioritizing_06.md") as myfile:
                lines = myfile.readlines()
            window["prioritizing_06_list_box"].update(random.choice(lines).strip()  )
    ###


    ###clarification_07
    if event == "clarification_07_list_box":
            with open("/home/dgd/Desktop/python_storyboard_flashcards/negotiations_tab/clarification_07.md") as myfile:
                lines = myfile.readlines()
            window["clarification_07_list_box"].update(random.choice(lines).strip()  )
    ###


    ###compromising_08
    if event == "compromising_08_list_box":
            with open("/home/dgd/Desktop/python_storyboard_flashcards/negotiations_tab/compromising_08.md") as myfile:
                lines = myfile.readlines()
            window["compromising_08_list_box"].update(random.choice(lines).strip()  )
    ###


    ###bargaining_09
    if event == "bargaining_09_list_box":
            with open("/home/dgd/Desktop/python_storyboard_flashcards/negotiations_tab/bargaining_09.md") as myfile:
                lines = myfile.readlines()
            window["bargaining_09_list_box"].update(random.choice(lines).strip()  )
    ###


    ###postponing_10
    if event == "postponing_10_list_box":
            with open("/home/dgd/Desktop/python_storyboard_flashcards/negotiations_tab/postponing_10.md") as myfile:
                lines = myfile.readlines()
            window["postponing_10_list_box"].update(random.choice(lines).strip()  )
    ###


###concluding_11
    if event == "concluding_11_list_box":
            with open("/home/dgd/Desktop/python_storyboard_flashcards/negotiations_tab/concluding_11.md") as myfile:
                lines = myfile.readlines()
            window["concluding_11_list_box"].update(random.choice(lines).strip()  )
    ###


###seal_the_deal_12
    if event == "seal_the_deal_12_list_box":
            with open("/home/dgd/Desktop/python_storyboard_flashcards/negotiations_tab/seal_the_deal_12.md") as myfile:
                lines = myfile.readlines()
            window["seal_the_deal_12_list_box"].update(random.choice(lines).strip()  )
###

    if event == "edit agenda_01":
                os.system("{} {}".format(EXTERNAL_EDITOR, "/home/dgd/Desktop/python_storyboard_flashcards/negotiations_tab/agenda_01.md"))
                


    if event == "edit making_proposals_02":
                os.system("{} {}".format(EXTERNAL_EDITOR, "/home/dgd/Desktop/python_storyboard_flashcards/negotiations_tab/making_proposals_02.md"))
                


    if event == "edit suggestions_03":
                os.system("{} {}".format(EXTERNAL_EDITOR, "/home/dgd/Desktop/python_storyboard_flashcards/negotiations_tab/suggestions_03.md"))
                


    if event == "edit agreeing_04":
                os.system("{} {}".format(EXTERNAL_EDITOR, "/home/dgd/Desktop/python_storyboard_flashcards/negotiations_tab/agreeing_04.md"))
                


    if event == "edit objecting_05":
                os.system("{} {}".format(EXTERNAL_EDITOR, "/home/dgd/Desktop/python_storyboard_flashcards/negotiations_tab/objecting_05.md"))
                


    if event == "edit prioritizing_06":
                os.system("{} {}".format(EXTERNAL_EDITOR, "/home/dgd/Desktop/python_storyboard_flashcards/negotiations_tab/prioritizing_06.md"))
                


    if event == "edit clarification_07":
                os.system("{} {}".format(EXTERNAL_EDITOR, "/home/dgd/Desktop/python_storyboard_flashcards/negotiations_tab/clarification_07.md"))
                


    if event == "edit compromising_08":
                os.system("{} {}".format(EXTERNAL_EDITOR, "/home/dgd/Desktop/python_storyboard_flashcards/negotiations_tab/compromising_08.md"))
                


    if event == "edit bargaining_09":
                os.system("{} {}".format(EXTERNAL_EDITOR, "/home/dgd/Desktop/python_storyboard_flashcards/negotiations_tab/bargaining_09.md"))
                


    if event == "edit postponing_10":
                os.system("{} {}".format(EXTERNAL_EDITOR, "/home/dgd/Desktop/python_storyboard_flashcards/negotiations_tab/postponing_10.md"))
                


    if event == "edit concluding_11":
                os.system("{} {}".format(EXTERNAL_EDITOR, "/home/dgd/Desktop/python_storyboard_flashcards/negotiations_tab/concluding_11.md"))
                


    if event == "edit seal_the_deal_12":
                os.system("{} {}".format(EXTERNAL_EDITOR, "/home/dgd/Desktop/python_storyboard_flashcards/negotiations_tab/seal_the_deal_12.md"))
                









    if event == sg.WIN_CLOSED or event == "Cancel" or event == 'Exit' :
        break

window.close()

# sg.Popup('Title',
#          'The results of the window.',
#          'The button clicked was "{}"'.format(event),
#          'The values are', values)
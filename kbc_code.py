import random
from matplotlib import pyplot as plt
import pandas as pd

print("WELCOME TO KAUN BANEGA CROREPATI...LET'S PLAY")
print("Hello" ,input("Enter Your Name\t"))

# total prize for each question
amount_won=[1000,2000,3000,5000,10000,20000,40000,80000,160000,320000,640000,1250000,2500000,5000000,10000000,70000000]
#Options for 50:50 lifeline
op1=['     ','        ','    ','Srinagar','     ','Cricket','1920','     ','    ','        ','   ','Cricket','       ','Kolkata',
         'Wrestling','          ','       ','     ','China','Thar','         ','      ','Israel',
         '      ','           ','Arjan Singh','Parliament of India','       ','     ','Mohd Hamid Ansari ',
    '    ','Mahatma Gandhi','Hanuman']

op2=['AB De Villiers','     ','9','       ','      ','    ','1928','     ','Cricket','Yuvraj Singh','Cricket','Football','West Indies','Mumbai',
        'Swimming','             ','      ','        ','       ','Sahara','Mahishmati','       ','Jordan',
         '       ','Che Guevera','               ','       ','      ','     ','     ',
    '    ','    ','              ']

op3=['Shahid Afridi','Dishonest','   ','Amritsar','Sindhi','      ','    ','Pakistan','     ','MS Dhoni','    ','       ','South Africa','    ',
        '      ','Henry Becquarrel','Tephrosia','Dermatitis','Japan','    ','       ','Bypass','         ',
         'Mridangam','         ','             ','     ','darjeeling','Japanese Encephalitis ','Mohd Hidayatullah ',
    'Saina Nehwal','      ','Shiva']

op4=['        ','Miserly','8','       ','English','Hockey','     ','Australia','Football','       ','Polo','     ','      ','     ',
        '       ','None of these','Indigofera','Cholera','        ','        ','Badami','Debridement','     ',
         'Dafli','Vladimir Lenin','Aspy Engineer','Mangalyaan','Kohima','Plague','       ',
    'Jwala Gutta','Mother Teresa','   ']

op=[op1,op2,op3,op4]

list_life=[1,2,3,4]                                    #list of lifelines



def lifeline(ran,opts,op):
    
    m=1
    
    lifelines=['Audience Poll','Fifty Fifty','Double dip','Flip the question']
    print("Lifelines are \t",lifelines[0],'\t',lifelines[1],'\t',lifelines[2],'\t',lifelines[3],'\n\n')
    if list_life==[]:
        print("You don't have lifelines remaining\t")
        return None
    print("Press 1 for audience,2 for 50:50, 3 for double dip or 4 for flip the quesion\t")
    
    while(m!=0):
        get=int(input())
        if get==1:
            if get in list_life:
                m=0
                list_life.remove(1)
                great=audience(ran,opts)
                
            else:
                print("You don't have audience poll\t")
        elif get==2:
            if get in list_life:
                m=0
                great=fifty(ran,op)
                list_life.remove(2)
                
            else:
                print("You don't have 50:50 \t")
        elif get==3:
            if get in list_life:
                m=0
                great=doubleDip(ran)
                list_life.remove(3)
            else:
                print("You don't have double dip\t")
        elif get==4:
            if get in list_life:
                m=0
                great=flip()
                list_life.remove(4)
            else:
                print("You don't have lifeline to flip the question\t")
        else:
            print("Choose correct option")
    
    
    return great
    

def audience(ran,opts):
    #graphical audience poll using pandas
    print("According to audience\n")
    
    s = pd.Series([opt1[ran],opt2[ran],opt3[ran],opt4[ran]], index=['1','2','3','4'])

    s.plot.bar(figsize=(20,10))
    plt.xlabel('Options')
    plt.ylabel('%')
    plt.title("Audience Poll")
    plt.show()
    
    
    print('1.',opts[0][ran],"%",'\t','2.',opts[1][ran],"%",'\t','3.',opts[2][ran],"%",'\t','4.',opts[3][ran],"%",'\nenter your choice\t')
    print("Would you like to take lifeline again,if yes then press 9 or Press 0 to Quit\t")
    choice=int(input())
    if choice==9:
        great=lifeline(ran,opts,op)
        return great
    elif choice==answer[ran]:
        great=1
        print("Correct answer,well done!..")
    elif choice==0:
        great=-2
    else:
        great=0
        print("Incorrect")
        print("Correct Answer is :", options[answer[ran]-1][ran])
        
    return great

def fifty(ran,op):
    print("Q."+questions[ran])
    for num,option in enumerate(op):
        print(str(num+1)+"."+option[ran])
    choice_fifty=int(input("enter your choice \t"))
    
    if choice_fifty==answer[ran]:
        print("Correct Answer.....")
        great=1
    else:
        great=0
        print("wrong answer")
        print("Correct Answer is :",options[answer[ran]-1][ran])
    return great
    

def doubleDip(ran):
    print("Select two options\n")                #double dip gives 2 chances
    trial1=int(input())
    if answer[ran]==trial1:
        great=1
        print("Correct Answer,well done....")
    else:
        print("Your first trial is wrong, choose another\t")
        trial2=int(input())
        if answer[ran]==trial2:
            great=1
            print("Correct Answer\t")
        else:
            print("Your second trial is also wrong..Better luck next time..\t")
            print("Correct Answer is :",options[answer[ran]-1][ran])
            great=0
    return great
    
def flip():
    return -1
    
    

def amount(correct_ans):
    print(amount_won[correct_ans-1])
    if amount_won[correct_ans-1]==10000:
        print("Completed 1st stage")
    elif amount_won[correct_ans-1]==320000:
        print("Completed 2st stage")
    elif amount_won[correct_ans-1]==70000000:
        print("You have won Rs 7 CRORE")
    return amount_won[correct_ans-1]

questions=['In ODI Cricket, who created the record of scoring the fastest century in just 31 balls ?',
           ' If you call someone ‘Makkhichoos’ then what are you calling him ?',
           'How many players of a Kho-Kho team can play on the field during the match ?',
           'Which of these Indian cities is closest to the Pakistani city of Lahore ?',
            'The language spoken by the people by Pakistan is ?',
          'The term“Googly” is associated with ?',
          'India first took part in the olympic games in the year ?',
           'Who are Kangaroos ?', 
           'Oval stadium in England is associated with ?', 
           'In 2011 India won the World Cup. Who was adjudicated as the man of the series in the tournament ? ',
           'Eden Gardens in Kolkata is ----- stadium.? ',
           'Ronaldo is associated with ? ',
           'Icc’s 2007, the World Cup Cricket was held in ? ',
           'Wankhede Stadium is at ? ',
           'World’s most ancient game is ? ',
           'Stethoscope was invented by ?',
           'A dye is prepared from ',
           'Which disease is caused by the fungi? ',
           'Which is the Land of the Rising Sun? ',
           'The desert that lies on the boundary between India and Pakistan is ',
           ' In which kingdom is the story of the ‘Bahubali’ series of films mainly set?',
           'What is the common name for surgery conducted on coronary arteries that supply blood to the heart ?',
           ' In July 2017, Narendra Modi Become the first Indian Prime Minister to visit which country ?',
           'Which of these musical instrument is held in one hand and played with the other ?',
           ' On the last day of his life Bhagat Singh was reading a book about the Ideology of which revolutionary ?',
           'Which Air force officer had the unique honour of leading the fly-post over the Red fort in Delhi on 15 August 1947 ?',
           'Which image appears on the flip side of the new 2000 Rs Note, launched in 2016?',
           'Which Indian hill station gets its name from the Tibetan words that mean ‘land of the thunderbolt’?',
           'Which of these diseases is transmitted by mosquitoes?',
           'Who among these has served as the Ambassador of India to the United Nations?',
           ' Who was the first Indian to win the World Junior Badminton Championships?',
           'Which of the following is a recipient of the Nobel Peace Prize?',
           'The cave temples at the historical site of Elephanta are dedicated to which God?'
           
          ]

option1=['Corey Anderson','Evil','10','Srinagar','Hindi','Cricket','1920','Bangladesh','polo','Virat Kohli','Tennis','Cricket','Australia','Kolkata',
         'Wrestling','Bessemer','Sida','Polio','China','Thar','Magadh','Cataract','Israel',
         'Tabla','Antonio Gramsci ','Arjan Singh','Parliament of India','Gangtok','Rabies',' Mohd Hamid Ansari',
        'P V Sindhu','Mahatma Gandhi','Hanuman']

option2=['AB De Villiers','Humble','9','Jaisalmer','Palauan','Football','1928','Kenya','Cricket','Yuvraj Singh','Cricket','Football','West Indies','Mumbai',
        'Swimming','Rane Laennec','Tridax','Malaria','Taiwan','Sahara','Mahishmati','Gastric','Jordan',
         'Santoor','Che Guevera','Pratap Chandra Lal','Tractor','Aizawl','Tetanus',' I K Gujral',
        'Aparna Balan','Swami Vivekananda ','Vishnu']

option3=['Shahid Afridi','Dishonest','7','Amritsar','Sindhi','Badminton','1972','Pakistan','Hockey','MS Dhoni','Hockey','Hockey','South Africa','Delhi',
        'Boxing','Henry Becquarrel','Tephrosia','Dermatitis','Japan','Gobi','Kalinga','Bypass','Saudi Arabia',
         'Mridangam',' Leon Trotsky ','Subroto Mukarjee','Red Fort','darjeeling','Japanese Encephalitis','Mohd Hidayatullah ',
        'Saina Nehwal','Rabindranath Tagore ','Shiva']

option4=['Rohit Sharma','Miserly','8','Udhampur','English','Hockey','1976','Australia','Football','Zaheer Khan','Polo','Tennis','India','Jaipur',
        'Running','None of these','Indigofera','Cholera','Australia','None of these','Badami','Debridement','Qatar',
         'Dafli','Vladimir Lenin','Aspy Engineer','Mangalyaan','Kohima','Plague','Zakir Hussain',
        'Jwala Gutta','Mother Teresa','Kamadeva']

options=[option1,option2,option3,option4]
#answer key
answer=[2,4,2,3,3,1,1,4,2,2,2,2,2,2,1,3,4,3,3,1,2,3,1,4,4,1,4,3,3,1,3,4,3]
wrong=False
correct=0                       #correct variable for total correct answer
total_amt=0
#option list for audience poll
opt1=[30,24,10,0,1,72,99,0,9,2,0,2,10,1,100,1,0,3,2,98,21,35,
         50,40,45,65,50,48,5,70,20,30,20]
opt2=[60,32,80,0,2,5,1,1,91,94,95,87,90,96,0,0,2,12,13,1,60,20,
         30,2,0,20,0,1,10,12,20,20,10]
opt3=[2,4,0,100,97,0,0,1,0,2,5,11,0,3,0,99,2,82,82,0,18,40,
         10,4,1,10,0,50,70,15,35,10,64]
opt4=[8,40,10,0,0,23,0,98,0,2,0,0,0,0,0,0,96,3,3,1,1,5,
         10,54,54,5,50,1,15,3,25,40,6]
opts=[opt1,opt2,opt3,opt4]    

condition,ques_no=1,0
while(wrong!=True):
    ques_no+=1
    ran=random.randint(0,len(questions)-1)
    print("\n\nQ.",ques_no,":-",end="")
    print(questions[ran])
    for num,option in enumerate(options):
        print(str(num+1)+"."+option[ran])
    
    print("Would you like to take lifeline, if yes, press 9\n Choose any option:  or you can quit by pressing 0 \t\t")
    give_answer=int(input())
    if give_answer==9:
            if condition<=4:    #condition variable is to count lifelines used
                condition+=1
                great=lifeline(ran,opts,op)
                if great==0:
                    if total_amt<10000:
                        total_amt=0
                    elif total_amt<320000:
                        total_amt=10000
                    elif total_amt<70000000:
                        total_amt=320000
                    break
                elif great==-1:
                    ques_no-=1
                    pass
                
                elif great==None:
                    print("Choose any option or press 0 to quit\t")
                    give_ansr=int(input())
                    if answer[ran]==give_ansr:
                        print("Correct answer, great")
                        correct+=1
                elif great==-2:
                    break
                else:
                    correct+=1
                    print("You have won Rs=",end="")
                    total_amt=amount(correct)
            else:
                print("You have used your all lifelines\t\n Choose any option:  or you can quit by pressing 0\t\t")
                give_ans=int(input())
                key=answer[ran]
                if give_ans==0:
                    total_amt=amount(correct)
                    break
                elif key==give_ans:
                    print("Correct, You have won Rs. =",end="")
                    correct+=1
                    total_amt=amount(correct)
                else:
                    print("Wrong Answer....")
                    print("Correct Answer is : ",options[answer[ran]-1][ran])
                    if total_amt<10000:
                        total_amt=0
                    elif total_amt<320000:
                        total_amt=10000
                    elif total_amt<70000000:
                        total_amt=32000
                    wrong=True
                
    
    else:
        key=answer[ran]
        if give_answer==0:
            if correct!=0:
                total_amt=amount(correct)
            break
        elif key==give_answer:
            print("Correct answer.., You have won Rs.=",end="")
            correct+=1
            total_amt=amount(correct)
        else:
            print("Wrong Answer...Better luck next time...")
            print("Correct Answer is :",options[answer[ran]-1][ran])
            if total_amt<10000:
                total_amt=0
            elif total_amt<320000:
                total_amt=10000
            elif total_amt<70000000:
                total_amt=320000      
            wrong=True
    if correct==16:                     #total questions are 16
        break
    #delete previous question and its options from list
    del questions[ran]
    del option1[ran]
    del option2[ran]
    del option3[ran]
    del option4[ran]
    del answer[ran]
    del opts[0][ran]
    del opts[1][ran]
    del opts[2][ran]
    del opts[3][ran]
    del op[0][ran]
    del op[1][ran]
    del op[2][ran]
    del op[3][ran]
    options=[option1,option2,option3,option4]
print("Your winning amount is Rs. ",total_amt)


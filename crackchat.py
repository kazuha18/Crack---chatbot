

import os,time
import random
import sys
import f1



name=['what is your name','what is your name?','what are u called?','may i know your name','who are you?','who are you','who r u?']
greeting=['hello','hi','hey','hey there','yo!']
born=['what is your date of birth?', 'when were you made?','what is ur DOB?','what is ur birth date?','when were u made?','when were you created?']
botmaster=['who is your botmaster?', 'who is your creator?', 'who made you?', 'what is your masters name?']
req=['help me?','i want your help']
solve=['which is the biggest star?']
c=['study C','C tutorials','c notes','c','c tutorials online']
cpp=['study C++','C++ tutorials','c++ notes','c++','c++ tutorials online']
j=['study java','java tutorials','java notes','java','java tutorials online']
dsa=['study data structure','ds tutorials','ds notes','data structure','ds tutorials online']
dcn=['study computer networks','dcn tutorials','dcn notes','computer network','dcn tutorials online']
dbms=['study ','dbms tutorials','dbms notes','dbms','dbms tutorials online']
best=['which subjects are most important for placement', 'subjects for placement study']
apti=['best websites to prepare aptitude','how to crack aptitude?']
topmnc=['updated list of top MNCs','top MNCs at present','top mnc']


nameO=['i am called Crack', 'i am Crack','my name is Crack']
greetingO=['HI','Yo!','hello','hey']

def main():
    ques=input('enter query to find links')
    if ques=='':
        print('please select option'+ques)
    if ques=='more':
        print('please select option'+ques)
    elif ques in c:
        f1.trade_spider(1)
        print("Let Us C ::"'https://www.edutechlearners.com/let-us-c-yashavant-kanetkar-pdf/ \n'+"The C Programming Language::"'http://ptgmedia.pearsoncmg.com/images/9780131103627/samplepages/0131103628.pdf \n',"The C Book::"'http://publications.gbdirect.co.uk/c_book/thecbook.pdf')
    elif ques in cpp:
        f1.trade_spider2(1)
        print("https://www.micc.unifi.it/bertini/download/programmazione/C%2B%2B%20A%20Beginner's%20Guide%202nd%20Edition%20(2003).pdf"+'http://fac.ksu.edu.sa/sites/default/files/ObjectOrientedProgramminginC4thEdition.pdf')
    elif ques in j:
        f1.trade_spider3(1)
    elif ques in dsa:
        print("https://www.smartzworld.com/notes/data-structures-notes-pdf/\n"+"https://lecturenotes.in/subject/81/data-structure-using-c\n"+"https://www.smartzworld.com/downloads/download/ds-complete-pdf-notesmaterial-2/")
        f1.trade_spider4(1)

    elif ques in dbms:
        print("https://beginnersbook.com/2015/04/dbms-tutorial/\n"+"https://beginnersbook.com/2015/05/normalization-in-dbms/")
        f1.trade_spider5(1)
    elif ques in dcn:
        print("https://www.tutorialspoint.com/data_communication_computer_network/\n"+"https://www.tutorialspoint.com/data_communication_computer_network/dcn_useful_resources.htm")
        f1.trade_spider6(1)







B='\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n Crack \n Online.......'
print(B)
while(True):
    H=input('=>').strip()
    HLower=H.lower()
    if H=='':
        print('=> Nice talking to you!')
        time.sleep(1)

        break
    elif HLower in name:
        print('=>'+(random.choice(nameO)))
    elif HLower in greeting:
        print('=>' + (random.choice(greetingO)))
        print('I AM HERE TO HELP YOU GET ANSWERS TO ALL PLACEMENT RELATED QUERIES\n','Type HELP ME? to enter into placement section','\nOR','\nType any other question')
    elif HLower in botmaster:
        print('=>' +'My Botmaster is Samy')
    elif HLower in born:
        print('=>' + 'I was activated on 25th Feb, 2017')
    elif HLower in best:
        print('most important subjects for placement are \ndata structures, \ndatabase management system,\n programming language like \n c,\nc++, \njava, networks')
    elif HLower in apti:
        print('FRESHER WORLD:http://placement.freshersworld.com/', '\nINDIABIX.COM:https://www.indiabix.com/')
    elif HLower in topmnc:
        print('https://www.naukri.com/btech-fresher-jobs')
    elif HLower in req:
        print('=>' + 'Yes, sure!')
        main()
    elif HLower in solve:
        print('=>' + 'it is Sun!')
    else:
        main()





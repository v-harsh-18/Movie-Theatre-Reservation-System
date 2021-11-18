import datetime

input=(('Mimi0002121112317', 'INOX C21', 'C21 Mall AB Road Near C-21 Mall Sheetal Nagar, Scheme 54 PU4, Indore, Madhya Pradesh 452010', '7314214003', datetime.timedelta(seconds=61200), datetime.date(2021, 11, 23), '0002', 1), ('Mimi0002221112313', 'INOX C21', 'C21 Mall AB Road Near C-21 Mall Sheetal Nagar, Scheme 54 PU4, Indore, Madhya Pradesh 452010', '7314214003', datetime.timedelta(seconds=46800), datetime.date(2021, 11, 23), '0002', 2), ('Mimi0001221112315', 'PVR Indore', '4th Floor,Treasure Island Mall, 11, Mahatma Gandhi Rd, South Tukoganj, Indore, Madhya Pradesh 452001', '8800900009', datetime.timedelta(seconds=54000), datetime.date(2021, 11, 23), '0001', 2))

theatre=()
temp1=()
temp2={}
tval=0
length=len(input)

for i in range(0,length):
         if(i==0):
          temp1=(input[i][1],input[i][2],input[i][3],input[i][6],input[i][7])
          temp2[input[i][0]]=input[i][4]

         elif(input[i][1]==temp1[0]):
            temp2[input[i][0]]=input[i][4]

         else:
             if(tval==0):
              temp1+=(temp2,)
              theatre=(temp1)
              tval=1


             else: 
              temp1+=(temp2,)
              theatre=((theatre,)+(temp1,))

             temp1=(input[i][1],input[i][2],input[i][3],input[i][6],input[i][7])
             temp2={input[i][0]:input[i][4]}


temp1+=(temp2,)
theatre=((theatre,)+(temp1,))  
bleh=theatre[1][5]

for key,value in theatre[1][5].items():
    print(key)
    print(value)

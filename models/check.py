import datetime

input=(('Mimi0001121112213', 'INOX C21', 'C21 Mall AB Road Near C-21 Mall Sheetal Nagar, Scheme 54 PU4, Indore, Madhya Pradesh 452010', '7314214003', datetime.timedelta(seconds=46800), datetime.date(2021, 11, 21)), ('Mimi0001121112313', 'INOX C21', 'C21 Mall AB Road Near C-21 Mall Sheetal Nagar, Scheme 54 PU4, Indore, Madhya Pradesh 452010', '7314214003', datetime.timedelta(seconds=46800), datetime.date(2021, 11, 23)), ('Mimi0001121110513', 'PVR Indore', '4th Floor,Treasure Island Mall, 11, Mahatma Gandhi Rd, South Tukoganj, Indore, Madhya Pradesh 452001', '8800900009', datetime.timedelta(seconds=46800), datetime.date(2021, 11, 5)))

theatre=()
temp1=()
temp2=set()
temp3=set()
tval=0
length=len(input)

for i in range(0,length):
    if(i==0):
     temp1=(input[i][1],input[i][2],input[i][3])
     temp2.add(input[i][4])
     temp3.add(input[i][5])

    elif(input[i][1]==temp1[0]):
       temp2.add(input[i][4])
       temp3.add(input[i][5])

    else:
        if(tval==0):
         temp1+=(temp2,)
         temp1+=(temp3,)
         theatre=(temp1)
         tval=1


        else: 
         temp1+=(temp2,)
         temp1+=(temp3,)
         theatre=((theatre,)+(temp1,))

        temp1=(input[i][1],input[i][2],input[i][3])
        temp2={input[i][4]}
        temp3={input[i][5]}


temp1+=(temp2,)
temp1+=(temp3,)
theatre=((theatre,)+(temp1,))     
hello=theatre[1][3]

# for val in hello:
#     print(val)

print(theatre)    

# to find number of days above average temperature 
inp = int(input('How many days temperature?'))
days=[]
for i in range(1,inp+1):
    temp = float(input(f"day {i}'s high temp:"))
    days.append(temp)
avg =  int(sum(days))/int(len(days))
print('Average = {}'.format(avg))
print("{} day(s) above average ".format(min(days)))
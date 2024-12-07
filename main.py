print('Concentration options and ID codes')
print('International business= IntBusn')
print('Management Information System= BMIS')
print('Operation Supply Chain= OPS_SCM')
print('Marketing= MKT')
#provides students the avaliable concentrations and their ID code. Does not reflect the full catalog at GU. Further growth and expansion of project can incorporate other concentrations

print('\n')
credits_achieved=int(input("Enter number of credits achieved:\n"))
while credits_achieved <= 128:
  if credits_achieved < 32:
    print('\nFreshman')
  elif credits_achieved < 64:
    print('\nSophomore')
  elif credits_achieved < 96:
    print('\nJunior')
  else:
    print('\nSenior')
  break
#while loop function to determine which grade level a student is in

while credits_achieved <= 128:
  credits_left= 128 - credits_achieved
  print('Credits left:', credits_left)
  break
#while loop to determine the overall amount of credits needed still before reaching the minimum requirement to graduate

print('\n')
ConInput= input('Number of desired concentrations?\n')
if ConInput < '2': 
  print (input('First concentration?\n'))
elif ConInput < '3':
  print(input('First concentration?\n'),
  input('Second concentration?\n'))
else:
  print(input('First concentration?\n'),
  input('Second concentration?\n'),
  input('Third concentration?\n'))
#asks number of concentrations a student desires

print('\n')
print('Business concentrations with corresponding classes')
Concentration_requirements= {
'IntBusn': 'MGMT 355 OPER 440 ECON 311 BFIN 327', 
'BMIS': 'BMIS 331 BMIS 342 BMIS 441 BMIS 444',
'OPS_SCM': 'OPER 347 OPER 346 OPER 345 OPER 348',
'MKT': 'MKTG 315 MKTG 330 MKTG 402 MKTG 419'}
for reqs in Concentration_requirements:
  print('%s requires %s'%(reqs, Concentration_requirements[reqs]))
#Displays the different concentration requirements so students are aware that they all require just four class and what classes are need for each concentration
print('\n')


IntB_single_concentration=['International Business''\n'
  'JuniorA= ECON 311, Elective, Elective, Elective''\n'
  'JuniorB= BFIN 327, Elective, Elective, Elective''\n'
  'SeniorA= OPER 440, Elective, Elective, Elective''\n'
  'SeniorB= MGMT 355, Elective, Elective, Elective''\n']
MKT_single_concentration= ['Marketing''\n'
  'JuniorA= MKTG 315, Elective, Elective, Elective''\n'
  'JuniorB= MKTG 330, Elective, Elective, Elective''\n'
  'SeniorA= MKTG 402, Elective, Elective, Elective''\n'
  'SeniorB= MKTG 419, Elective, Elective, Elective''\n']
OPS_single_concentration=['Operations''\n'
  'JuniorA= OPER 346, Elective, Elective, Elective''\n'
  'JuniorB= OPER 345, Elective, Elective, Elective''\n'
  'SeniorA= OPER 347, Elective, Elective, Elective''\n'
  'SeniorB= OPER 348, Elective, Elective, Elective''\n']
Mis_single_concentration=['Management Information Systems''\n'
  'JuniorA= BMIS 331, Elective, Elective, Elective''\n'
  'JuniorB= BMIS 342, Elective, Elective, Elective''\n'
  'SeniorA= BMIS 441, Elective, Elective, Elective''\n'
  'SeniorB= BMIS 444, Elective, Elective, Elective''\n']
print('Single Concentration catalogue')
print(*IntB_single_concentration)
print(*MKT_single_concentration)
print(*OPS_single_concentration)
print(*Mis_single_concentration)
#two year catalogue for single concentrations

MKT_Mis_Double_concentration=['Marketing and Management Information Systems''\n'
  'JuniorA= BMIS 331, MKTG 315, Elective, Elective''\n'
  'JuniorB= BMIS 342, MKTG 330, Elective, Elective''\n'
  'SeniorA= BMIS 441, MKTG 402, Elective, Elective''\n'
  'SeniorB= BMIS 444, MKTG 419, Elective, Elective''\n']
IntB_MKT_Double_concentration=['International Bussiness and Marketing''\n'
  'JuniorA= MKTG 315, ECON 311, Elective, Elective''\n'
  'JuniorB= MKTG 330, BFIN 327, Elective, Elective''\n'
  'SeniorA= MKTG 402, OPER 440, Elective, Elective''\n'
  'SeniorB= MKTG 419, MGMT 355, Elective, Elective''\n']
IntB_Mis_Double_concentration=['International Business and Management Information Systems''\n'
  'JuniorA= BMIS 331, ECON 311, Elective, Elective''\n'
  'JuniorB= BMIS 342, BFIN 327, Elective, Elective''\n'
  'SeniorA= BMIS 441, OPER 440, Elective, Elective''\n'
  'SeniorB= BMIS 444, MGMT 355, Elective, Elective''\n']
OPS_IB_Double_concentration=['Operations and International Business''\n'
  'JuniorA= OPER 346, ECON 311, Elective, Elective''\n'
  'JuniorB= OPER 345, BFIN 327, Elective, Elective''\n'
  'SeniorA= OPER 347, OPER 440, Elective, Elective''\n'
  'SeniorB= OPER 348, MGMT 355, Elective, Elective''\n']
OPS_MKT_Double_concentration=['Operations and Marketing''\n'
  'JuniorA= OPER 346, MKTG 315, Elective, Elective''\n'
  'JuniorB= OPER 345, MKTG 330, Elective, Elective''\n'
  'SeniorA= OPER 347, MKTG 402, Elective, Elective''\n'
  'SeniorB= OPER 348, MKTG 419, Elective, Elective''\n']
OPS_Mis_Double_concentration=['Operations and Management Information Systems''\n'
  'JuniorA= BMIS 331, OPER 346, Elective, Elective''\n'
  'JuniorB= BMIS 342, OPER 345, Elective, Elective''\n'
  'SeniorA= BMIS 441, OPER 347, Elective, Elective''\n'
  'SeniorB= BMIS 444, OPER 348, Elective, Elective''\n']
#two year catalogue for double concentration
print('\n\n')
print('Double Concentration catalogue')
print(*MKT_Mis_Double_concentration)
print(*IntB_MKT_Double_concentration)
print(*IntB_Mis_Double_concentration)
print(*OPS_IB_Double_concentration)
print(*OPS_MKT_Double_concentration)
print(*OPS_Mis_Double_concentration)

OPS_IntB_Mis_Triple_concentration= ['Operations, International Business, and Management Information Systems''\n'
  'JuniorA= BMIS 331, ECON 311, OPER 346, Elective''\n'
  'JuniorB= BMIS 342, BFIN 327, OPER 345, Elective''\n' 
  'SeniorA= BMIS 441, OPER 440,OPER 347,Elective''\n'
  'SeniorB= BMIS 444, MGMT 355, OPER 348,Elective''\n']
MKT_OPS_IntB_Triple_concentration= ['Marketing, Operations, and International Business''\n'
  'JuniorA= MKTG 315, ECON 311, OPER 346, Elective''\n' 'JuniorB= MKTG 330, BFIN 327, OPER 345, Elective''\n' 'SeniorA= MKTG 402, OPER 440, OPER 347, Elective''\n' 'SeniorB= MKTG 419, MGMT 355, OPER 348, Elective''\n']
Mis_MKT_OPS_Triple_concentration=['Management Information Systems, Marketing, and Operations''\n'
  'JuniorA= BMIS 331, MKTG 315, OPER 346, Elective''\n', 'JuniorB= BMIS 342, MKTG 330, OPER 345, Elective''\n', 'SeniorA= BMIS 441, MKTG 402, OPER 347, Elective''\n','SeniorB= BMIS 444, MKTG 419, OPER 348, Elective''\n']
IntB_Mis_MKT_Triple_concentration= ['International Business, Management Information Systems, and Marketing''\n'
  'JuniorA= BMIS 331, ECON 311, MKTG 315, Elective''\n' 'JuniorB= BMIS 342, BFIN 327, MKTG 330, Elective''\n' 'SeniorA= BMIS 441, OPER 440, MKTG 402, Elective''\n' 'SeniorB= BMIS 444, MGMT 355, MKTG 419, Elective''\n']
#two year catalogue for triple concentration
print('\n\n')
print('Triple Concentration catalogue')
print(*OPS_IntB_Mis_Triple_concentration)
print(*MKT_OPS_IntB_Triple_concentration)
print(*Mis_MKT_OPS_Triple_concentration)
print(*IntB_Mis_MKT_Triple_concentration)
#program looks to aid students depending on how many concentration they so desire. Giving students an idea on how to plan their junior and senior specifically. 
#If student is already a junior or senior they can check to see if their current course completed match the requirements. 
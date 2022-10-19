#Balanced parantheses in an expression
#function that takes an argument
def balance(x):
  exc = ('\)', '\(', '\]', '\[', '\}', '\{')
  lst_p =[]
  x += '@'
  for i in range(1, len(x)):
    for b in exc:
      xi = x[i-1]+x[i]
      if xi == b:
        x = x.replace(xi, '||')
  for i in range(len(x)+1):
    if x[i-1] == ')':
      lst_p.append(-1)
    elif x[i-1] == ']':
      lst_p.append(-3)
    elif x[i-1] == '}':
      lst_p.append(-5)
    elif x[i-1] == '(': 
      lst_p.append(1)
    elif x[i-1] == '[':
      lst_p.append(3)
    elif x[i-1] == '{':
      lst_p.append(5)
      #return false when the parentheses do not have open or close pair
  if lst_p[0] < 0 or 0 > sum(lst_p) or sum(lst_p) > 0 or lst_p[-1] > 0:
    return print('False')
  #return false when have the open or close but 
  else:
      cont = 0
      while cont <= len(lst_p)*4:
        for i in range(1, len(lst_p)):
          x0 = lst_p[i] + lst_p[i-1]
          cont += 1
          if x0 == 0:
            del lst_p[i]
            del lst_p[i-1]
            break
          elif cont == len(lst_p)*4:
            return print('False')
  return print('True')

#prompt the user input misplaced
text = input('Enter an expression: \n').replace('\\\\', '') 

balance(text)


def density (m,Va):
  p = m/Va
  return p
while True:
  print(']---input-data---For-quit-input-QUIT[')
  num0 =(input('material weight: ')) 
  if num0 == 'Quit' or num0 == 'QUIT' or num0 == 'quit':
    break
  try:
    num1 = float(num0)
    while True:
      num2 = float(input('Ìass of material: '))
      if num2 != 0:
        break
      else:
        print("Сan't be zero!")  
    print(round(density(num1,num2),4))

  except ValueError:
    print('Wrong data')  

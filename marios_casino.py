import collections
Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
  ranks = [str(n) for n in range(2, 11)] + list('JQKA')
  suits = 'spades diamonds clubs hearts'.split()

  def __init__(self):
    self._cards = [Card(rank, suit) for suit in self.suits
 for rank in self.ranks]

  def __len__(self):
    return len(self._cards)

  def __getitem__(self, position):
    return self._cards[position]

deck = FrenchDeck()

from random import choice

g=1000
print("To start to play my BLACK JACK, press enter:")
print()
print("You start with U$ ",g,"cash")
enter=input()
while enter=="":
  aux=0
  print("WELCOME TO MARIO'S CASINO!!! press enter to continue")
  print()
  enter=input()
  k=input("How much money do you wanna bet? (minimum: U$ 50; maximum: U$500) type here>>>:")
  print()
  if k=="":
    print("You pressed enter without typing your bet. Press enter to start again")
    enter=input()
    continue
  apo=int(k)      
  if apo>500:
    print("You exceeded the maximum of money! Please, try again!")
    continue
  elif apo<50:
    print("You bet under the minimum of money! Please, try again!")
    continue
  elif apo>g:
    print("You cannot afford for this bet!!! Please choose a lower value if possible")
    continue
  print("IT'S MARIO'S CASINO TURN!!! wait your turn while pressing enter to see my cards")
  enter=input()
  while enter=="":
    st=str(choice(deck))
    print(st)
    if st[11]=='K' or st[11]=='Q' or st[11]=='J' or st[11]=='1':
      b=10
    elif st[11]=='A':
      b=1
    else:
      b=int(st[11])
    aux=aux+b
    if aux>15:
      break
    enter=input()
  if aux>21:
    print()
    print("YOU WIN!!!")
    enter=input()
    g=g+apo
    print("CONGRATULATIONS!!!")
    print()
    print("U$ ",g,"cash")
    print()
    print("To start to play my BLACK JACK AGAIN!!!, press enter: or press any key followed by enter to finish")
    enter=input()
  elif aux<=21:
    print()
    print("MARIO'S CASINO STOPPED")
    print()
    print("YOUR TURN!press enter:")
    enter=input()
    aux2=0
    while enter=="":
      st=str(choice(deck))
      print(st)
      if st[11]=='K' or st[11]=='Q' or st[11]=='J' or st[11]=='1':
        b=10
      elif st[11]=='A':
        b=1
      else:
        b=int(st[11])
      aux2=aux2+b
      if aux2>21:
        print()
        print("YOU LOST, BITCH!!!")
        enter=input()
        print()
        g=g-apo
        print("U$ ",g,"cash")
        break
      if aux2==aux:
        if aux==21:
          print()
          print("DRAW!!!")
          enter=input()
          print()
          print("U$ ",g,"cash")
          c=0
        else:
          c=0
          while c!='yes' and c!='no' and c!='NO' and c!='YES' and c!='Yes' and c!='No':
            print()
            print("DO YOU WANNA CONTINUE???")
            print()
            c=input("Write YES to continue or NO to stop:")
            if c=='yes' or c=='YES' or c=='Yes':
              print()
              print("OK!!!")
              break
            if c=='no' or c=='NO' or c=='No':
              print()
              print("YOU ARE A CHICKEN BRO")
              print()
              enter=input()
              print("DRAW!!!")
              enter=input()
              print()
              print("U$ ",g,"cash")
              break
            else:
              print("Invalid Option!")
              
        if c=='yes' or c=='YES' or c=='Yes':
          continue
        else:
          break
      if aux2>aux:
        print()
        print("YOU WIN!!!")
        enter=input()
        print()
        print("CONGRATULATIONS!!!")
        print()
        g=g+apo
        print("U$ ",g,"cash")
        break
      enter=input()
    print()
    print("To start to play my BLACK JACK AGAIN!!!, press enter: or press any key to finish")
    enter=input()

  
  



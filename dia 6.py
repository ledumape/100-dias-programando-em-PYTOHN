def direita():
  turn_left()
  turn_left()
  turn_left()

while frente_vazia():
  move()
turn_left()

while not at_goal():
  if right_is_clear():
    turn_right()
    move()
  elif frente_vazia():
    move()
  else:
    turn_left()
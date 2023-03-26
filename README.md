# tanks-battle
1. Install Python3.10+. 
2. Install pygame:

   ```pip install pygame```

4. Define tank behaviour in method figthRed() or fightWhite(). Only allowed are:
  - methods move and rotate 
  - properties distToTarget and angleToTarget
5. Here's a tactics example. If the opponent is in front of you (-45 to + 45 degress) then move 10 pixels, otherwise move backwards by 5 pixels and rotate 30 degrees counterclockwise. 

 ```
  if -45 < self.angleToTarget < 45:
      self.move(10)      
  else:
      self.move(-5)
      self.rotate(30)   
  ```
 

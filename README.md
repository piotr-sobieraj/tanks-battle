# tanks-battle
1. Install Python3.10+. 
2. Install pygame:

   ```pip install pygame```

4. Define tank behaviour in method ```figthRed()``` or ```fightWhite()```. Only allowed are:
  - methods ```move``` and ```rotate``` 
  - properties ```distToTarget``` and ```angleToTarget```

5. Method ```move(distance)``` moves the tank by ```distance``` pixels forward. The ```distamce``` is cut down to 10 (or -10), so ```move(15)``` gives the same effect as ```move(10)```. The default value is 10. 
You can use negative values to move the tank backward. 

6. Method ```rotate(angle)``` rotates the tank by ```angle``` degrees counterclockwise. The argument is cut down to 30, so ```rotate(45)``` gives the same effect as ```rotate(30)```. Use negative values to rotate the tank clockwise. 

7. Field ```angleToTarget``` gives information, by which angle the tank must rotate, to have the other tank in front. Positive value means the tank must rotate by negative value. 

8. Field ```distToTarget``` gives information about the distance to the other tank. 


9. Here's a tactics example. If the opponent is in front of you (-45 to + 45 degress) then move 10 pixels, otherwise move backwards by 5 pixels and rotate 30 degrees counterclockwise. 

 ```
  if -45 < self.angleToTarget < 45:
      self.move(10)      
  else:
      self.move(-5)
      self.rotate(30)   
```
Remark: The methods ```move``` and  ```rotate``` can be used only once in the program flow. The above example is correct, because ```move``` is called only one time in the runtime.   
 

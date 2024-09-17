# Maze-Game
Maze game implemented with a .txt based Level Creation system

I created a basic maze game with collision and different object types, I also created a 
level creation system that uses numpy to convert a .txt file with characters in a 16 x 12 
box to a fully playable level.

Python Files:
* runner.py
  * This is the file with the code that provides functionality by using methods and classes from all other files
* Block.py
  * This file contains the Block class that provides the base for the all of the objects shown in the game such as obstacles, walls, and the finish line.
* Level_Creation.py
  * This file contains the implementation for my level creation system using numpy, it scans a txt file and converts it to a list of objects for the runner file to place using pygame.


Block Class Object Types:
* Blocks (walls/walkways)
  * Denoted by "**+**" for walls and "**@**" for walkways
* Obstacles
  * Denoted by "**O**"
* Teleporters
  * Denoted by "**1**" for teleporter 1 (from) and "**2**" for teleporter 2 (to)
* Finish
  * Denoted by "**X**"

level3.txt:

<pre> 
@@@@@+@@@@@@@@@@ 
+@++@+@++O+@+@+@ 
+@++@@@++++@@@+@ 
++@@@++@@@@@+++@ 
+++@++++@O+@@@+@ 
++O@@@@@@+++@+@@ 
+++++@++++OO@O+@ 
+++++@++++O@@@O@ 
+++++@++++O@O@O@ 
++2+++++++O@@@O@ 
++@++++++++O1OO@ 
++X+++++++++++++ </pre>



**__Level 3 Created from level3.txt in Game:__**

![image](https://github.com/user-attachments/assets/90159d52-3e53-4484-ac09-2f6cf582affe)


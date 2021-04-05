# Ph-UI!!!

For lab this week, we focus on the prototyping the physical look and feel of the device. _Make sure you read all the instructions and understand the whole of the laboratory activity before starting!_



## Prep

1. Pull the new Github Repo.
2. Readings: 

* [What do prototypes prototype?](https://www.semanticscholar.org/paper/What-do-Prototypes-Prototype-Houde-Hill/30bc6125fab9d9b2d5854223aeea7900a218f149)

* [Paper prototyping](https://www.uxpin.com/studio/blog/paper-prototyping-the-practical-beginners-guide/) is used by UX designers to quickly develop interface ideas and run them by people before any programming occurs. 

* [Cardboard prototypes](https://www.youtube.com/watch?v=k_9Q-KDSb9o) help interactive product designers to work through additional issues, like how big something should be, how it could be carried, where it would sit. 

* [Tips to Cut, Fold, Mold and Papier-Mache Cardboard](https://makezine.com/2016/04/21/working-with-cardboard-tips-cut-fold-mold-papier-mache/) from Make Magazine.

* [Surprisingly complicated forms](https://www.pinterest.com/pin/50032245843343100/) can be built with paper, cardstock or cardboard.  The most advanced and challenging prototypes to prototype with paper are [cardboard mechanisms](https://www.pinterest.com/helgangchin/paper-mechanisms/) which move and change. 

<img src="https://dysonthedesigner.weebly.com/uploads/2/6/3/9/26392736/427342_orig.jpg"  width="200" > Dyson Vacuum cardboard prototypes


### For lab, you will need:

1. Cardboard (start collecting those shipping boxes!)
1. Cutting board
1. Cutting tools
1. Markers
1. Found objects and materials--like bananas--we're not saying that to be funny.


### Deliverables for this lab are: 
1. Sketches/photos of device designs
1. "Looks like" prototypes: show us what how the device should look, feel, sit, weigh, etc.
3. "Works like" prototypes: show us what the device can do
4. "Acts like" prototypes: videos/storyboards/other means of showing how a person would interact with the device
5. Submit these in the lab 4 folder of your class [Github page], either as links or uploaded files. Each group member should post their own copy of the work to their own Lab Hub, even if some of the work is the same for each person in the group.


## Overview
Here are the parts of the assignment

A) [Capacitive Sensing](#part-a)

B) [OLED screen](#part-b) 

C) [Paper Display](#part-c)

D) [Wizard the device](#part-d-wizard-the-device) 

E) [Costume the device](#part-e-costume-the-device)

F) [Record the interaction](#part-f-record)

## The Report
This readme.md page in your own repository should be edited to include the work you have done. You can delete everything but the headers and the sections between the **stars**. Write the answers to the questions under the starred sentences. 

Include any material that explains what you did in this lab hub folder, and link it in the readme.

Labs are due on Mondays. Make sure this page is linked to on your main class hub page.

### Part A
### Capacitive Sensing, a.k.a. Human Banana Interaction

We wanted to introduce you to the [capacitive sensor](https://learn.adafruit.com/adafruit-mpr121-gator) in your kit. It's one of the most flexible input devices we were able to provide. At boot it measures the capacitance on each of the 12 contacts. Whenever that capacitance changes it considers it a user touch. You can attach any conductive material. In your kit you have conductive fabric and copper tape that will work well, but don't limit yourself! In this lab we will use (go?) bananas!

<p float="left">
<img src="https://cdn-learn.adafruit.com/guides/cropped_images/000/003/226/medium640/MPR121_top_angle.jpg?1609282424" height="150" />
<img src="https://cdn-shop.adafruit.com/1200x900/4401-01.jpg" height="150">
<img src="https://post.healthline.com/wp-content/uploads/2020/08/banana-pink-background-thumb-1-732x549.jpg" height="150">
</p>

Plug in the capacitive sensor board with the qwiic connector. Connect your banana's with either the copper tape or the alligator clips (the clips work better). make sure to install the requirements from `requirements.txt`

![](https://media.discordapp.net/attachments/679721816318803975/823299613812719666/PXL_20210321_205742253.jpg?width=1518&height=1139)

I've connected my banana's* to pads 6 and 10. When you run the code and touch a banana the terminal will print out the following

```
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 4 $ python cap_test.py 
Banana 10 touched!
Banana 6 touched!
```

*\*Some students have noted that their banana's look noticeably different from the ones presented in this demo. We firmly reject the accusation that these are not in fact banana's but Twizzlers™. Due to the challenges of remote teaching we cannot debug banana's at this time. We suggest you bring these issues up with the university or your local produce representative*

### Part B
### OLED screen

We just received some of the small oled screens that we had coped to include in your kit. If you want one feel free to pop into the lab and get one. These don't have colors like the one on the pi but you can move it around on a cable making for more flexible interface design. The way you program this display is almost identical to the pi display. Take a look at `oled_test.py` and some more of the [Adafruit examples](https://github.com/adafruit/Adafruit_CircuitPython_SSD1306/tree/master/examples).

<p float="left">
<img src="https://cdn.sparkfun.com//assets/parts/1/6/1/3/5/17153-SparkFun_Qwiic_OLED_Display__0.91_in__128x32_-01.jpg" height="200" />
<img src="https://cdn.discordapp.com/attachments/679466987314741338/823354087105101854/PXL_20210322_003033073.jpg" height="200">
</p>



### Part C
### Paper Display

Here is an Pi with a paper faceplate on it to turn it into a display:

<img src="https://github.com/FAR-Lab/Developing-and-Designing-Interactive-Devices/blob/2020Fall/images/paper_if.png?raw=true"  width="250"/>


This is fine, but it can be a bit difficult to lay out a great and user friendly display within the constraints of the Pi. Also, it really only works for applications where people can come and stand over the Pi, or where you can mount the Pi to the wall.

Here is another prototype for a paper display:

<img src="https://github.com/FAR-Lab/Developing-and-Designing-Interactive-Devices/blob/2020Fall/images/b_box.png?raw=true"  width="250"/>

It holds a pi and usb power supply, and provides a front stage on which to put writing, graphics, LEDs, buttons or displays.

This design can be made by scoring a long strip of corrugated cardboard of width X, with the following measurements:

| Y height of box <br> <sub><sup>- thickness of cardboard</sup></sub> | Z  depth of box <br><sub><sup>- thickness of cardboard</sup></sub> | Y height of box  | Z  depth of box | H height of faceplate <br><sub><sup>* * * * * (don't make this too short) * * * * *</sup></sub>|
| --- | --- | --- | --- | --- | 

Fold the first flap of the strip so that it sits flush against the back of the face plate, and tape, velcro or hot glue it in place. This will make a H x X interface, with a box of Z x X footprint (which you can adapt to the things you want to put in the box) and a height Y in the back. 

Here is an example:

<img src="https://github.com/FAR-Lab/Developing-and-Designing-Interactive-Devices/blob/2020Fall/images/horoscope.png?raw=true"  width="250"/>


Make a paper display for your project that communicates the state of the Pi and a sensor. Ideally you should design it so that you can slide the Pi out to work on the circuit or programming, and then slide it back in and reattach a few wires to be back in operation.
 
**a. Document the design for your paper display.** (e.g. if you had to make it again from scratch, what information would you need?). Include interim iterations (or at least tell us about them).

**b. Make a video of your paper display in action.**

**c. Explain the rationale for the design.** (e.g. Does it need to be a certain size or form or need to be able to be seen from a certain distance?)

### Part D
### Materiality

**Open Ended**: We are putting very few constraints on this part but we want you to get creative.

Design a system with the Pi and anything from your kit with a focus on form, and materiality. The "stuff" that enclose the system should be informed by the desired interaction. What would a computer made of rocks be like? How would an ipod made of grass behave? Would a roomba made of gold clean your floor any differently?

**a. document the material prototype.** Include candidates that were considered even if they were set aside later.

**b. explain the selection.**

### Part 2.

Following exploration and reflection from Part 1, complete the "looks like," "works like" and "acts like" prototypes for your design.

Reiterating:
### Deliverables for this lab are: 
1. Sketches/photos of device designs
1. "Looks like" prototypes: show us what how the device should look, feel, sit, weigh, etc.
3. "Works like" prototypes: show us what the device can do
4. "Acts like" prototypes: videos/storyboards/other means of showing how a person would interact with the device
5. Submit these in the lab 4 folder of your class [Github page], either as links or uploaded files. Each group member should post their own copy of the work to their own Lab Hub, even if some of the work is the same for each person in the group.
> ### "Looks like"
>
> #### Rationale for Design
> Our design is to bring back nostalgic memories of Mancala boards that fit in a child's lap.  Thus, we decided to make a prototype that models this, having it to be relatively small, light, and ultimately so this game can be brought anywhere.
>
> #### Original Design Idea
> Our original paper display is to show the game "Mancala to the Beat" where the players have to play mancala with the catch of picking up and dropping mancala pieces to the beat of the song.  Each time they do this correctly, they receive a point.  Each time they do not, they lose a point.  Our prototype will look like a Mancala board that has multiple wells and at the ends, there will be bigger containers to hold the beads.  Below is a sketch where the circles are the wells and the rectangles at the ends are for the bigger containers to hold the beads to keep track of each person's points.  The rectangle in the middle is the OLED display that will show the beat to the song.  The screen will also display the name of the game, the points for each respective player on the sides of the screen, and any annunciations in the middle such as "Player 1's Turn" or "Player 2 wins!" throughout the game.  
>
> Here is the sketch of our original design idea:
>
> ![](MancalaGUI_OLD.png)
>
> Here is part of our original prototype with an unused container with wells that would work well: 
>
> ![](Graceprototype1.jpg)
>
> #### New Design
> After gathering feedback from others, we decided to change the game slightly so it would be an "imaginary mancala" because this seemed more fun then just dropping the beads to the beat.  We also realized it would be hard to keep track of all the beads as they are easy to lose and so we will have a display that corresponds to how many beads are in each of the mancala wells. 
>
> The person playing will tap the bottom of the mancala well a certain number of times in order to communicate the type of action he or she is doing as follows:  
> - One tap is dropping a bead
> - Two taps is picking up the bead(s) in the well
>
> Instead of an OLED display in the center, there will be buttons for each player to show when their turn is over. There will be a separate GUI apart from the board to show the players where the beads are based on their taps to help with imagining and keep track of the imaginary mancala beads.
>
> Below is the sketch of the new design:
>
> ![](MancalaGUI.png)
>
> Below is how the paper prototype looks like with what imaginary beads (or bananas) would look like, even though in reality, these wells for the mancala will be empty:
>
> ![](paper_prototype_setup.jpg)
>
> #### Materiality 
> We will use sturdy plastic for each of the mancala wells and strong origami paper boxes for the ends.  We used [this origami tutorial](https://www.youtube.com/watch?v=LUEwM_ZiFIg) to make the paper boxes and it looks aesthetically pleasing since everything is white.  Below is a picture of one of the origami boxes. Note that for our final prototype, we used a total of three boxes where another one of these boxes to put underneath the Mancala board so that it was elevated slightly to not interfere with the capacitive sensor connections.
>
> ![](origami_box.jpg)
>
>We want to have a sturdy material for the wells so that it would not be crushed easily. The container works perfectly as it used to hold mochi ice cream and so each of the wells are the perfect size for this miniature version of mancala.  Below is a picture showing how our final prototype looks like, just as how a mancala board looks like.  The "Works Like" section will go into more technical details of how the prototype was implemented.
>
> ![](final_prototype.jpg)
>
> #### Auditory Enhancements
> If we could extend this prototype to a more finished product, we would like to use smooth wooden board with imaginary marbles, as that is the nostalgia Mancala brings with the set we all played with when we were younger. Being able to "pick up" and "drop" these imaginary marbles on a smooth surface is a satisfying experience so the surface should be smooth, rather than rough.  Due to our limitations, we prototyped using plastic and paper instead of wood.  However, to simulate the sounds of marbles dropping or being picked up, we added those sounds that would be played based on the taps.  This would simulate picking up these rather "ghost marbles" since they make sounds based on the user interaction with the mancala board.
 
> ### "Works Like"
> One of the core aspects of Mancala is the action of interacting with each of the wells, whether by picking up or dropping the beads. We didn’t want to have either of the players change their natural actions while playing, so we decided to take advantage of the fact that a well is used when it has been touched. We placed a circle of fabric at the bottom of each well and lined the walls with conductive copper tape. [Here](https://drive.google.com/file/d/1FThWEq4TNiHbRtA53Mc0GVNptGTeVFxz/view?usp=sharing) is a video of the capacitive touch system working with just the fabric. The terminal prints out whenever the connected object is pressed. This layout was used to ensure that no matter how the well was touched, the [capacitive touch sensor](https://learn.adafruit.com/adafruit-mpr121-gator) would be triggered.
>
> ![](mancala_well.jpeg)
> 
> Six of the sensor’s touchpads were connected to the wells via lines of copper tape. This proved to be a viable yet slightly finicky solution, since any little crease or fold in the tape could either disconnect it or make it trigger constantly. To be sure that no outside electrical signals were being sent to the tape, it was placed directly onto the plastic container when possible (since plastic is an insulator) and otherwise taped onto electrical tape. Any of the QWIIC connectors running between the sensors on-board were also wrapped in electrical tape.
> 
> ![](prototypingprocess.jpg)
> 
> These connections were tested by running the Python program ```cap_test.py```. This code initialized an instance of the adafruit_mpr121 board connected via I2C QWIIC connectors and then ran through each of the touchpad values to see if they had been triggered (set to a high signal). 
> 
> After conducting trials with our paper prototype, we knew we wanted a way to easily discern between players’ individual turns. Two [QWIIC buttons](https://www.sparkfun.com/products/16842) are connected via QWIIC connectors to the capacitive touch sensor, one per player. The intent is to light up one button to indicate it’s the corresponding player’s turn: green for player 1 and red for player 2. 
>
> ![](final_prototype.jpg)
> 
> By default the QWIIC button has an I2C address of 0x6f. In order to be able to control each button individually, one of their I2C addresses had to be changed. We referred to [code from the QWIIC Button Python repository](https://github.com/sparkfun/Qwiic_Button_Py/blob/main/examples/qwiic_button_ex6_changeI2CAddress.py), written in ``change_i2c.py```, to change the red button (player 2) to 0x4f. This code did raise an error that said ```’raw_input’ is not defined``` but a quick search showed that [The NameError: name 'raw_input' is not defined error is raised when you try to use the raw_input() method in Python 3. To fix this error, replace all instances of raw_input() with the input() function in your program](https://careerkarma.com/blog/python-nameerror-name-raw-input-is-not-defined/#:~:text=The%20NameError%3A%20name%20'raw_input'%20is%20not%20defined%20error%20is,()%20function%20in%20your%20program). To check that the address change had gone through, we ran ```two_button.py``` (from QWIIC Button’s code [here](https://github.com/sparkfun/Qwiic_Button_Py/blob/main/examples/qwiic_button_ex7_2Buttons.py)) to see if the buttons could individually discern whether or not they’d been pressed. Using the ```LED_on(brightness)``` and ```LED_off()``` calls helped illustrate this by turning the button lights off once they were pressed and on once the other button was pressed. This behavior is shown in [this video](https://drive.google.com/file/d/1O7Zbqd3yvF044HON2z-ZHFOKxhq_oLFD/view?usp=sharing).
> 
> ```mancala.py``` holds the code necessary to read the capacitive touch sensor and button presses. [Here](https://drive.google.com/file/d/1jZsKlBnsLTOb7WKCdeSGEOcTe1NbJ7fM/view?usp=sharing) is a video of the full system working and [here](https://drive.google.com/file/d/1Yo_BcSGE7JB05aXYmfTxIVN620f1huhL/view?usp=sharing) are the accompanying terminal outputs.
 
> ### "Acts Like"
> Now that our device "looks" like a mancala board, and "works" with the functionality of the mancala game, we think about the user interaction -- how to make the game "act" and feel as though the user is playing a game of mancala. Much of this task is accomplished when we look at the two main angles of the game design and function. One, making sure the way the user interacts with the imaginary mancala game is as similar as possible to if they were playing with a traditional mancala board, and two, making sure the imaginary mancala game responds in a way that the user would expect. 
>
> From our experience with playing mancala, and our experimentations with the paper prototype, we established the tapping mechanism as a way to "pick up" and "drop" the pieces into the wells. This is a simple way to mimic how a user would interact with a traditional mancala board with wells. Also, since users most typically associate mancala with wells to hold the marble game pieces, we opted to use a frame that would remind users of that trait. This recognizability is an important reason we chose a plastic prototype with wells rather than a flat piece of plastic or cardboard. 
>
> While the capacitive touch tapping is a clear way to implement the game functions, we found that the device was lacking in responsiveness. One of the most unique things about traditional mancala is the feel and sound of clattering marbles against the wooden game board. With "invisible" pieces and a plastic frame, our device doesn't inherently capture this iconic trait. After discussions with Wendy, we decided to add sounds as part of the partner graphic user interface in order to make the device "act" more like the traditional game. 
>
> Our final demo video can be seen [here](https://youtu.be/N72hd6ygvpo)! We had a lot of fun recreating a game we played as kids, and hope we captured the spirit of the mancala in this project. :)

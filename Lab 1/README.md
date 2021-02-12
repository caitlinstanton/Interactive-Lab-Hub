

# Staging Interaction

## Prep

### For lab, you will need:

### Deliverables for this lab are: 

## Overview
For this assignment, you are going to 

A) [Plan](#part-a-plan) 

B) [Act out the interaction](#part-b-act-out-the-interaction) 

C) [Prototype the device](#part-c-prototype-the-device)

D) [Wizard the device](#part-d-wizard-the-device) 

E) [Costume the device](#part-e-costume-the-device)

F) [Record the interaction](#part-f-record)

## The Report
This readme.md page in your own repository should be edited to include the work you have done. You can delete everything but the headers and the sections between the **stars**. Write the answers to the questions under the starred sentences. Include any material that explains what you did in this lab hub folder, and link it in the readme.

Labs are due on Mondays. Make sure this page is linked to on your main class hub page.

## Part A. Plan 

**Describe your setting, players, activity and goals here.**

My interactive device is a natural light desk lamp, crafted to provide a light source appropriately colored by the time of day. It will only turn on when needed by the person whose desk it sits on. This will be confirmed by connecting the lamp to an accompanying desk chair, both of which will have sensors embedded within them. A real-time clock will be tasked with determining what color light to use: earlier times will have cool-toned light, while later in the day will have warm-tone light.

This interaction is happening in a space with a desk and accompanying chair, such as an office (either at home or in a workplace), a coworking space, or a general living area. Since the interaction is utilizing a desk lamp, this device can be used during the workday at an office or workplace or at the end of the workday if it's in a home or living space.

The room may contain many people, but the main actor in question is the person whose desk the lamp is sitting on. Coworkers and clients (especially in a work environment) or family and friends (especially in a living space) may be occupying the room as well, depending on its size and furniture layout. 

The person who's directly interacting with the lamp is going to do some work at their desk. They will sit down at their desk chair, pull themselves closer to the desk, and begin working; this will turn on the lamp to assist with lighting any work they're doing. Other people in the room may be milling about, talking with the main actor, or doing their own work, but they will not be directly interacting with both the chair and the lamp unless they intend to do work at this desk.

The goal of the person directly interacting with the lamp is to complete work at their desk without eye strain. The presence of the light and its shift from cool-toned light to warmer-toned light will especially help during less naturally lit times of day.

Sketch a storyboard of the interactions you are planning. It does not need to be perfect, but must get across the behavior of the interactive device and the other characters in the scene. 
**Include a picture of your storyboard here**

Present your idea to the other people in your breakout room. You can just get feedback from one another or you can work together on the other parts of the lab.
**Summarize feedback you got here.**

The original premise involved the lamp turning off and on like a normal desk lamp, except with the added feature that the user wouldn't have to turn it on manually. The people in my breakout room (Priya Kattappurath, Jacob Rauch, Luca Spinazzola) encouraged added more interesting elements to it, particularly with color and sound. That's how I brainstormed the feature of differently toned light based on the time of day, since people are more apt to want warmer-toned light closer to nighttime so as to prevent eye strain directly before winding down for bed. At first I thought about using a light sensor to help determine what level of light the lamp should be on, but I realized that wouldn't be useful in situations when it's darker during the middle of the day (i.e. a storm) or in rooms that aren't naturally lit (since artifical light tends to be at the same strength no matter the time of day, especially in an office). A real-time clock could be loaded onto the microcontroller for this interactive device and an API tracking the sunset/sunrise of the location of the lamp could be used instead.

## Part B. Act out the Interaction

**Are there things that seemed better on paper than acted out?**

At first, the idea was that the lamp would turn on when the desk chair was compressed with weight, indicating a person was sitting down in it and ready to work. When I stood to get up, I remembered that I often use my chair to hold boxes, bags, and other items temporarily, that my chair is used for a combination of storage and sitting. Having a weight sensor alone wouldn't account for that because the weight of a box could trigger it just the same as a person, and it felt sort of invasive to have to input your weight for a desk lamp device to turn on. At least another sensor needed to be added in order to work around this use case for the desk chair.

**Are there new ideas that occur to you or your collaborators that come up from the acting?**

The original assumption was that this lamp will be used on a one-person desk, so the desk chair will be directly correlated with the desk lamp. However, in a co-working space or open office, there is the possibility that the desk lamp can be moved to another area or even simply pointed in a direction not facing the desk chair. In this case, someone sitting in the desk chair will trigger the lamp to turn on in another area or configuration. This can be solved with sensors in both the lamp and the desk chair to have more redundancy in checking if a person has sat down (a weight sensor in the desk chair) and if they're in front of the corresponding lamp (a proximity sensor on the lamp). 

## Part C. Prototype the device

**Give us feedback on Tinkerbelle.**

Unfortunately, I wasn't able to use the Tinkerbelle tool. I installed the requirements.txt items using pip3 and checked that I had a version of Python 3 installed before running python3 tinker.py. The IP address and debugging statements would print to the console, but going to http://localhost:5000 or http://192.168.1.13:5000 didn't load the page at all on my desktop or my phone. 

![Terminal printout](terminal.png)

I changed the port number to 8888 in the case that another program was using 5000, but that didn't solve the problem. Other students recommended restarting the computer or downgrading to another version of Python 3 (or even Python 2) but now of these fixes worked. 

Thankfully, Priya Kattappurath is also taking the class. She's one of my friends and is currently in Ithaca so I was able to use her functional Tinkerbelle app for additional prototyping and the final video of my interactive device. This screenshot of the launched web server was successfully grabbed from her desktop running Tinkerbelle.

![Launched Tinkerbelle](server.png)

## Part D. Wizard the device
Take a little time to set up the wizarding set-up that allows for someone to remotely control the device while someone acts with it. Hint: You can use Zoom to record videos, and you can pin someone’s video feed if that is the scene which you want to record. 

**Include your first attempts at recording the set-up video here.**

Now, change the goal within the same setting, and update the interaction with the paper prototype. 

**Show the follow-up work here.**

## Part E. Costume the device

Only now should you start worrying about what the device should look like. Develop a costume so that you can use your phone as this device.

Think about the setting of the device: is the environment a place where the device could overheat? Is water a danger? Does it need to have bright colors in an emergency setting?

**Include sketches of what your device might look like here.**

**What concerns or opportunitities are influencing the way you've designed the device to look?**


## Part F. Record

**Take a video of your prototyped interaction.**

[Final Interaction](https://youtu.be/dxMwPZV3G44)

**Please indicate anyone you collaborated with on this Lab.**

Priya, Luca, and Jacob gave good feedback during our breakout room session, and Priya was very useful in filming the finished prototype.

# Staging Interaction, Part 2 

This describes the second week's work for this lab activity.


## Prep (to be done before Lab on Wednesday)

You will be assigned three partners from another group. Go to their github pages, view their videos, and provide them with reactions, suggestions & feedback: explain to them what you saw happening in their video. Guess the scene and the goals of the character. Ask them about anything that wasn’t clear. 

**Summarize feedback from your partners here.**

## Make it your own

Do last week’s assignment again, but this time: 
1) It doesn’t have to (just) use light, 
2) You can use any modality (e.g., vibration, sound) to prototype the behaviors, 
3) We will be grading with an emphasis on creativity. 

**Document everything here.**

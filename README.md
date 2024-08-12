<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#about-the-project">Usage</a>
      <ul>
        <li><a href="#installation">Prerequisites</a></li>
        <li><a href="#prerequisites">Getting Started</a></li>
      </ul>
    </li>
    <li>
      <a href="#about-the-project">Some Complexities</a>
    </li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

I was playing some Roblox in the summer, namely this game called doodle world. The game itself is pretty grindy, and they had a summer event that was essentially to do tasks to get some in-game currency. 
These tasks were extremely repetitive and I got a little bored doing them so I made a bot instead. 
This was a fun experience because I had played this game when I was younger and had always had this idea of making a bot but never really felt motivated enough to do it.

The bot makes roughly 500 of said currency per hour which is decent (I think) to the average human rate, and does one of the two implementable tasks a lot better than I could.

When setup correctly, the bot will:
- Navigate to the event board,
- Refresh tasks until an implemented one appears
- Do said task
- Reset the character's camera angle and position

### Built With

Just Python3

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- USAGE -->
## Usage

On the off-chance someone wants to try this, here's how:

### Prerequisites

Software: The user would need python3, pytesseract, and pyautogui installed. 
In-Game: Confirm that doodle followers are off and graphics are turned to minimum. Ensure that you have a mount that is accessible by pressing q.

### Modifications

If you have a 2021 Macbook 14-inch you're in luck and can ignore this modifications section. Not a big screen-size pixel person but the stats are 3024 x 1964 px at 254 ppi, and when I drag my mouse to screenshot the accessible pixels on my screen are from 1512 to 981.

To make this bot work, you may need to do some editting of the following hard-coded pixel values I included to "avoid other player blocking NPC" issue:

event.py
- (721,474) is roughly the center of my screen
- (440,350) clicks the first task
- (1175,320) is where the yes button appears when you click the quest board
- (1175,390) is where the no button appears when you click the quest board
- the screenshot regions in get_tasks() correspond to the quest titles when the quest board is open
- the screenshot region (200,100,1000,130) is xleft, ytop, width, height and should be the entire black text box when you click accept quest except the little right pointing arrow in the bottom right
- wantsDict has a mapping of each topping to its placement on my screen when doing the making_pizza task
- (750, 800) is the "finish pizza" button in the making_pizza task
- there are two while loops with (420 +/i x*i, 480 +/i x*i). This is the location of the chef in the pizza_delivery task when you accept it and navigate in front of him.

Almost there!

Util/moveInstructions.py
- (766,777) is the reset_char button when you hit escape
- (658,428) is the followup confirmation button
- There is one while loop in reset_camera() that has 760 and 480. Replace these with the coordinates to the middle of your character's head after you press q once after loading in.

### Execution

You can get this bot running after modifications by doing the following steps:
1) Load into the event server and press q once. Do not move your character or pan your camera. If you have, reload into the event server and press q to engage your mount.
2) Run event.py and return to roblox within 3 seconds of running it
3) Hope it doesn't break

<p align="right">(<a href="#readme-top">back to top</a>)</p>


## Some Complexities

A few things I ran into while implementing the bot.

### Inconsistency in timing (both in Python's time module and Roblox)
- Turning is an important part of movement, and I would think that holding the left key for one second and the right key for one second would reset my character's camera angle to exactly what it was before. Unfortunately, either the camera pans at different speeds left and right or python's timing module has some expected variance that makes it difficult to guarantee correctness to a useable degree. As a result, we use an NPC to reset our character's camera angle after every task.
- This also means that if I move forward 2 seconds I may not end up in the exact position I want to be in when I try to click something on the screen. This has been accounted for by allowing the bot to retry clicks until it detects a popup that signals that it has done its task. If it has retried too many times it will reset.
- Furhtermore, Roblox also has some lag which makes it so that I can't just wait 1 second after clicking this npc because sometimes it takes 2 or even 3 seconds for his text to generate. Waiting 3 seconds every time would be slow, so we have on-screen detection for that.

### On-screen noise
- Expectedly, a bot that doesn't violate Roblox's terms and conditions would need to rely on screen events instead of backend data to record different game states. Unfortuantely, when it comes to locating onScreeen events there is always the chance that some other player is in the way blocking whatever is being looked for. That said, there exist some hard-coded values mentioned previously that may need to be editted for other people's uses.

- Fortunately, popups cannot be blocked by other people and are thus not hard-coded.

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

The user would need python3, pytesseract, and pyautogui installed.

### Getting Started

To get a local copy up and running follow these simple steps:



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



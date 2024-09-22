# Software Meeting Recap - September 14, 2024

## Attendance
Our meetings are 1-3pm every week. The second half is software-focused, but we expect you to attend the hardware portion as well.

**Why attend hardware meetings?** It's hard to simulate or write code for the robot if we don't know what the robot's physical capabilities and limitations are. You don't have to make significant contributions to the hardware; attending meetings and asking questions (where applicable) is good enough.

If you have to miss a portion of a future meeting for any reason, please make sure to contact any of us from `@Pacbot Lead` in our Discord (this includes Jack, Andy, Divija, Rayyan, and me) BEFORE the meeting. Pacbot is a competitive team, and we take attendance very seriously for deciding who represents us in the competition at the end of the year. We do not expect or require prior Robotics experience, but to make any progress and not fall behind, you need to be there.

Please see the slides if you couldn't make today. I will do this recap every week, but we also cover topics in meetings that are not in the slides.

## Downloading software dependencies

To run our software, you will need to install:
* The Go Programming Language (https://go.dev/doc/install)
* The Node.js web backend (https://nodejs.org/en/download/package-manager)
* Python (https://www.python.org/downloads/) - if you have a Python version less than 3.10, you may have to install Python 3.10+

## Pacbot-25

The repository we are using for this year's software (which includes firmware) is https://github.com/princeton-robotics-club/PacBot-25. If you don't have access and are part of our team, please contact ih2422@princeton.edu or jt1065@princeton.edu.

### Cloning the repo

`git clone https://github.com/princeton-robotics-club/Pacbot-25`

* If you don't have Git, you can follow a tutorial online to download it on your operating system.
* To clone the repo, you may have to set up Personal Access Tokens / SSH Keys for GitHub if you haven't already (you can find tutorials online for setting these up).

### Server

Open one terminal on your screen, and change directory to the `Pacbot-25/` folder.

If you're using MacOS / Linux, run the following commands:
```
cd server
go build
./pacbot_server
```

If you're using Windows, run the following commands:
```
cd server
go build
pacbot_server.exe
```

#### Tip: If you ever forget these instructions, you can also open the `README.md` file in the `server/` folder.

### Web Client

Open **another** terminal on your screen, and change directory to the `Pacbot-25/` folder.

Run the following commands (should be OS-independent):
```
cd web_client
npm install
npm run dev
```

#### Tip: If you ever forget these instructions, you can also open the `README.md` file in the `web_client/` folder.

Then, you can open the link in your browser. If it worked, you should see "trusted client connected" appear in the server terminal.

### Gameplay

Once you have the server and web client set up and running (in **different** terminals), you can play the game! Use SPACE to unpause/pause, and WASD or arrow keys to control the Pacman character.

### Bot Client

Open **another** terminal on your screen, and change directory to the `Pacbot-25/` folder.

Run the following commands (should be OS-independent):
```
cd bot_client
python -m pip install -r requirements.txt
python pacbotClient.py
```

#### Tip: If you ever forget these instructions, you can also open the `README.md` file in the `bot_client/` folder.

Notice that the algorithm doesn't do much! Your job for Software Challenge #1 is to edit `decisionModule.py` to match your algorithm of choice.

## Pacbot-SW-2024

You can clone our repo from last year, `https://github.com/princeton-robotics-club/Pacbot-SW-2024.git`, for inspiration from our A* algorithm used on the last Pacbot.

After the clone, run:
```
git fetch origin astar-template
git checkout origin astar-template
```

Then, follow the steps from the previous section. If everything was set up right, you should be able to start the game and have the Pacbot automatically play the game.

## Next Week

Make sure all this software is set up on your computer, and reach out to us if not.

Next week, we will cover the A-star algorithm and the Pacbot game rules in more detail. Here are some links you can check out to get ahead:
* Pacman Dossier: https://www.gamedeveloper.com/design/the-pac-man-dossier
* A-Star: https://theory.stanford.edu/~amitp/GameProgramming/AStarComparison.html
* Start working on software challenge #1! The details are in the slides PDF. Please reach out to us if you have any questions. The demo for SW challenge #1 is October 5.
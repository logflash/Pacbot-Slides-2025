# Software Meeting Recap - September 21, 2024

## Last Week

Please read and catch up with [last week's tasks](../2024-09-21/README.md).

## Today's Meeting

As of now, there are no slides in this folder (I may add some later when I have more time). We reviewed the basics of how a reinforcement learning algorithm would be implemented. Please direct any questions about the A* algorithm or Q-learning algorithm to Ian.

## Next Week

Next week, we will have a demo opportunity for you to showcase your accomplishments with automating and playing Pacbot. Once again, the rules are as follows:
* You must eventually make your code available as a branch of the [Pacbot-25](https://github.com/princeton-robotics-club/Pacbot-25) repository, so you and other students can use it as a reference for later algorithms. Assuming you wrote code on a cloned version of the repo (i.e., you used `git clone`, which you should), here are some simple steps to push your code to a branch:

  ```
  git checkout -b YOUR_NET_ID
  git add --all
  git commit -m "Software Challenge #1"
  git push origin YOUR_NET_ID
  ```

  * If you're confused about any of the Git details, please do not hesitate to reach out to Andy or Ian. It's better for us to work out issues with version control now, rather than during the hectic month leading up to the competition.

* You are allowed to play with the web client (with **any modifications you add**, provided they do not violate any other rules listed in this document), in addition to running **no more than one** Pacbot autonomous agent you write at the same time.

  * How might you write an autonomous agent? Here are some tips:

    * If you want to use the Python API for Pacbot, take a look at `decisionModule.py` in `bot_client/` within the [Pacbot-25](https://github.com/princeton-robotics-club/Pacbot-25) repo. You'll see a line with the following text:

      ```
      self.state.queueAction(4, Directions.RIGHT)
      ```

      If you look in `gameState.py` in `bot_client/`, you'll see this helpful function definition:

      ```py
	  def queueAction(self, numTicks: int, pacmanDir: Directions) -> None:
		'''
		Helper function to queue a message to be sent to the server, with a
		given Pacbot direction and number of ticks until the message is sent.
		'''

		self.writeServerBuf.append(
			ServerMessage(D_MESSAGES[pacmanDir], numTicks)
		)
      ```

      You'll want your algorithm to use the game state API functions in `gameState.py` to implement a better algorithm in `decisionModule.py`. If you have any questions about how to add an algorithm you write, please reach out to Andy or Ian.

    * You can reference the `decisionModule.py` and `aStarPolicy.py` files in [Pacbot-SW-2024](https://github.com/princeton-robotics-club/Pacbot-SW-2024.git) in the `bot_client/policies/astar/` folder to get inspiration. Once again, make sure to follow the steps in [the first week's tasks](../2024-09-14/README.md#pacbot-sw-2024) to check out the `astar-template` branch, so we use simulation code and not the more complex communication protocol we send to the robot.

    * If you want to implement an ML-style approach, I'd highly recommend using PyTorch. There are plenty of great tutorials online for how to implement Reinforcement Learning using PyTorch.

* Cite code taken from online, especially if it came from a research paper or article, both for integrity (once we publish our final algorithm) and as a reference for your peers.

* While you are allowed to make modifications to `bot_client/` and `web_client/`, do not make changes to `server/`. To make the challenge fair for everyone, we require that the server deciding the movement of the ghosts and updates to the game state does not change.

* When we demo, do not interfere with another person's trial over the network (this should be obvious, but just in case), as the server can easily get overloaded with requests from the web client and bot client.

* Make your controls reasonable. While some short-distance teleportation along a straight path is technically allowable, a good rule of thumb is to only implement a feature in simulation if we have confidence that the robot can accomplish it.

  * For example, teleporting to the other side of the screen is possible using commands to the server (see `server/game/commands.go` if you're curious), but that doesn't mean it's achievable for the robot.

  * Also, only send commands which influence the **position of Pacman** in the game state (if you use `self.state.queueAction`, you should be fine). It's technically possible to reset the game and do other manipulation of the server (like pausing and playing the game using code), but make sure that any special commands you use are not game-breaking (for example, pressing `Esc` in the web client will reset the game in the middle of your demo - please don't do that!).
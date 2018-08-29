# Reversi-reinforcement-learning
RL approach to learning the strategy of the classic game Reversi from scratch

Reversi is a board game where players take turns putting stones on the board.
By putting the stone on the board player can (and must, according to the rules)
surround opponent stones in horizontal, vertical or diagonal direction thus
flipping them. The goal of the game is to flip as many stones as possible to your
own color and at the end of the game have more stones of your color than your opponent.
To quickly familiarize with the rules one can play a game online
at, for example, http://www.webgamesonline.com/reversi/

the bot can be played against at depth-10 search by launching player.py with PyPy3 (this is needed for reasonable 3-10 second move time).

Reinforcement learning pipeline

The system has 4 modules: the value function approximator, the game-playing agent, the game database and the 
feature training module. 

Value function approximation

A given board configuration has, in theory, a value between -64 (all pieces are white) and 64 (all pieces are black) 
that is the final score of the game if both parties (white and black) played the game perfectly to the end.
However, if there are more than 10-20 turns remaining, it is computationally impossible to calculate this score. Therefore, an approximation is used: the "value function". The value function that we use is a linear function of scores of separate board patterns (lines, corners, some other combinations) and approximates the perfect final score if both parties played out a perfect game. For example, the edge of the board
of a specific board configuration would be "--OOXX--" (O is white, X is black and - is empty). We would have to look up
in a dictionary what score this particular pattern has, say c1. Then, we have to check all other edges, obtain their scores
c2, c3, c4. Then, we have to check all other patterns and obtain other scores. Finally, the value function of this particular
board is given by c1+c2+c3+c4+... . The better the value function approximates the perfect score, the stronger the agent that
uses this value function is going to be.

The game-playing agent

For a given board cofiguration, black, has, say, 10 moves available. Each one of these moves will transport the current board
state to a new board state. Using value function approximator, black should choose such a move that transports black to the
best possible board state for black - corresponding to highest value function score. Then, white should do the same, but optimize
for lowest value function score (as it is best for white). This agent would be called ply-1 agent, because it looks one move ahead.
In Reversi, just like in chess, it pays to see several moves ahead - the more the better. Therefore, our agent looks 5 moves ahead in mid-game and calculates the perfect score only when there is 10 empty squares left (these "5" and "10" are hyperparameters, they need to be tuned for best performance). Since the agent is deterministic, every game played would be the same, so they have to be forced to play different games. A policy something like "play first 5-10 moves randomly" could be used, but a better one is picked. The whole training procedure is turned into one giant Monte Carlo Tree Search (like the one used in Go papers, but the most basic version). When we encounter a MCTS leaf, we do a rollout policy, that game becomes our N-th training game. This biases the exploration so that the games played are more balanced. This choice is, in my opinion, in-between the "first 5-10 random moves" algorithm that would provide games that are too-random and unrealistic and "standard book-building" algorithm that would be basically incorrect (because dictionary changes over time) and would provide games that do not necessarily explore enough. Therefore, this choice strikes a good balance between exploration and exploitation. 

Game database

This module is simple and keeps the games and their final scores (Monte-Carlo measure) and agent's own evaluation at every step of each game (a kind of bootstrapping measure). Over time, some data cleansing is applied, such as deleting old and incorrect games, recalculating bootstrapping scores, deleting games that area too one-sided.

Feature training

This module is also simple and does the following linear regression. Each board in the game database corresponds to some features and to some final scores (Monte Carlo). So, we just train these features. Most stable learning is when we use final scores (as is expected, Monte Carlo scores + randomized initial states provide most stable learning), however, faster learning results from usage of bootstrapping scores. To illustrate this point we use an example from chess. Say, you observe a grandmaster game and you see that white is two pawns up and the black bishop is kind of trapped. It is not difficult for you to conclude that white has a high chance of winning. But, if you were suddenly pitched against a grandmaster to play with white, would it be easy for you to convert? Probably not. Also, if two amateurs started playing this position, we would observe that the position is more even than you would think, because
amateurs make more errors and that advantage can quickly evaporate. So, the heuristic explanation is that even a weak engine can determine the final score of a game played between two strong engines. The accuracy of this determination is postulated to be much higher than the accuracy obtained by playing a board out by the weak engine itself. We test this idea numerically near the endgame and we find that indeed, using the bootstrapping score the training is way faster than pure Monte-Carlo. However, when we start training from scratch, our agent is not only weak, it is super weak and has no idea what is going on. Therefore, using pure bootstrapping at this stage is problematic. Therefore, we assign the following training score to each board: ("final score obtained by engines" + "engine evaluation of the board") / 2. This seems to strike a good balance between training speed and stability. This is used in stage 1 of the training. In stage 2 (after two days of training), the engine is considered to be sufficiently strong and trustworthy and only the bootstrapping (engine's own evaluation) measures are used. For the fears of fluctuation induced instability the fitting does not use SGD, only the simple (and slow) gradient descent. This slow fitting even appears to be a good thing, because it somewhat suppresses the overfitting problem (but, of course, when the training is very stable, we should eventually try out SGD, maybe it is just as good and 10x faster). 

How these 4 modules talk to each other is shown in the project structure.png . The information is flowing around the circle clockwise in the following way: the more training games we have, the more reliable and less overfitted the feature evaluations are, hence, the stronger games are played, hence the more reliable final scores are produced leading to more and better quality training data. 

At this point the program has been training for 3 days (using PyPy3) and has played around 200.000 games.
Half of these games are stored in a file of 100MB, however github does not allow big files
to be stored. The strength of the evaluation function appears to be as good as WZebra's (a statement produced by playing several no-book
depth 10-12 games against WZebra).

The latest feature values (dictionaries) are in the main directory and the bot can be played against at depth-10
search by launching player.py with PyPy3 (this is needed for reasonable 3-10 second move time).

The quality of code... I know... not the highest. It will be fixed.

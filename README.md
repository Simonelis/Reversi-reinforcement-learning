# Reversi-reinforcement-learning
RL approach to learning the strategy of the classic game Reversi from scratch

Reversi is a board game where players take turns putting stones on the board.
By putting the stone on the board player can (and must, according to the rules)
surround opponent stones in horizontal, vertical or diagonal direction thus
flipping them. The goal of the game is to flip as many stones as possible to your
own color and at the end of the game have more stones of your color than your opponent.
To quickly familiarize with the rules one can play a game online
at, for example, http://www.webgamesonline.com/reversi/


At this point the program has been training for 3 days (using PyPy3) and has played around 200.000 games.
Half of these games are stored in a file of 100MB, however github does not allow big files
to be stored. 

The latest dictionary is in the main directory and the bot can be played against at depth-10 alpha-beta 
search by launching player.py with PyPy3 (this is needed for reasonable 3-10 second move time).

Stage 1
is the initial training-from-scratch phase where the game is played out as well as the bot can (not very well)
and the final score is recorded. In between games, the past games are taken as a training set to train the
feature dictionary and make it a little bit stronger for the next game.

Two optimizations are made, first, as the older games are of obviously lower quality, are slowly removed from the
training set. For every 2 new games played, the oldest game is removed from the training set.
Second, not only the final result is recorded (this we call Monte Carlo evaluation), 
but the bots own calculation how well it is doing.
We have performed experiments and shown that this bootstrapping procedure yields faster learning. However,
we cannot rely on this bootstrapping entirely from the beginning, so, first, we use the following value for the
training: (end_result + eval_result) / 2. This way, the learning is more stable and does not suffer from vanishing
training signal (to be explained) and instabilities.

Stage 2
New games are not generated at all, the existing game frames are taken and we continually recalculate game frame 
score evaluations and use these game frames with the new evaluations. So, this is 100% bootstrapping procedure and
thankfully it seems to converge. Convergence is improved by the following pre processing: we generate 200k more games and
throw out the frames that are worse than -32 and better than +32 to avoid super one sided games and to avoid evaluations
that are above 64 (linear eval function is capable of that).

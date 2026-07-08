# Search: Tic Tac Toe

In this toy repo, we design and implement a functional CLI-based tic tac toe game with an AI that uses the minimax algorithm to play against the player. 

Minimax algorithm is simple: it works under the assumption that the opponent will always play optimally to minimize the AI's score and also that both players have have full-state visibility. Every time the AI makes a move, it is given an array of scores associated with each move. When it is picking a move, it picks the move that will maximize its score. When it is simulating the opponents move, it picks the move that will minimize its (AI's not the opponent) score.

### Implementation Detail

We have the game set up to where a positive score means player 'O' wins and negative score means 'X' wins. The AI is always player 'O'. 

The AI tries to maximize its score. It will also choose moves that will result win states in the fewest amount of moves, and moves that will result in loss states in the maximum amount of moves. This is done by keeping track of depth of the recursion tree, where higher depth is better for stalling the game, and lower depth is ideal for winning the game.

---

## Alpha-Beta Pruning

One limitation to minimax is that it requires the AI to simulate every possible move until the game reaches a terminated state. With a small state space like tic tac toe, the computation associated with determining the optimal move is not an issue. With more complicated scenarios where the state space can be indefinitely vast, it becomes infeasible to try to model every state. 

Alpha-beta pruning is an optimization that reduces the number of states visited. Essentially, it ignores exploring branches of the game tree if the minimizing/maximizing player has a branch that can not yield a better outcome than one already found. We will use the following tree as an example:

![Alpha-beta pruning example][ab-pruning]

Here, maximizing nodes are upright and minimizing nodes are flipped vertically. In this example, the node $x$ will never be explored because the minimizing node with val=3 will have a value $\leq 3$. Moreover, this node knows that the root node a layer above it will always select the value of 10 since it knows that the right branch will have an upper bound of 3.

For a sanity test, if $x < 3$, then the minimizing node would subsequently choose that smaller value, but the maximizing root node would still pick the value = 10.

If $x > 3$, then the minizing node would pick 3 since it's the smaller value. The maximizing root node still ends up choosing the left branch with value = 10.

So regardless of $x$'s value, the value that the nodes at and above the layer of node with val=3 are unaffected by it.

### Optimization
We can implement this by keeping track of alpha and beta score for each recursion call, where alpha is the best possible score found, and beta is the minimum score found. If alpha is greater than or equal than beta, then we can prune any branches below it since we have already found a branch that we will always choose over any of the current branch's children. 

[ab-pruning]: /ab-pruning.png

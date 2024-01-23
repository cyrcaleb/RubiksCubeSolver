# RubiksCubeSolver
A Rubik's Cube has 43 Quintillion different scrambles. However, each and every one can be solved in 20 moves or less. This repository is about creating programs capable of determining the exact "algorithm" or sequence of moves to solve any scrambled cube.

## Fundamentals

- A Rubik's Cube has 6 sides
- Each side has three possible moves
  -   1 turn or 90 degrees
  -   2 turns or 180 degrees
  -   3 turns clockwise / 1 turn counter clockwise or 270 degrees)
- Moves: (Each face) (Prime denoted by --> ' <-- represents a counter clockwise rotation)
-   R, R', R2
-   L, L', L2
-   U, U', U2
-   D, D', D2
-   F, F', F2
-   B, B', B2

## Why is this difficult
- The task at hand is not to simply solve a Rubik's cube but to do so in the minimum number of moves possible which we know is less than or equal to 20 moves.
- We already defined a move as one of three rotations on any of the 6 sides of a cube. This means we have 18 possible moves to choose from.
- Lets say we are given a scrambled Rubik's cube. If we want to solve the cube through brute force we would simply try every combination.
- Well for each move, we have 18 choices, so at the very worst (meaning this scramble takes 20 moves to solve) we would have to go through 18^20 different solving algorithms which is wayyyyy too big.

## Simplifiying 18^20
- 18^20 is too large so how can we simiplify this
- There is no point in making 2 turns on the same side back to back because
  - a 90 degree turn on 1 side followed by a 270 degree trun on the same side would result in the cube being in the same posiition as it started
  - also a 90 degree turn followed by another 90 degree turn could just be simplified by doing a single 180 degree turn
  - no matter what combination of turns, under no circumstance should we make 2 turns on the same side back to back
  - this means our first turn will always have 18 options but every turn after that will have 15 possible options since we removed the 3 from the side we just chose
- Now we have 18 * 15^19 (Still way too large)

- ### Solving Backwards
- Currently we are just starting from a scrambled cube and trying all possibilities until we get the solve
- But we can actually simultaneous do the same thing but in reverse
- What I mean is that we can start from a solved cube and scramble it move by move until
- If we do this at the same time we find all possible move states from the scrambled start, we will eventually find a state in the middle tha-t is common on both sides (Here is a Visual).
![image](https://github.com/cyrcaleb/RubiksCubeSolver/assets/90429575/905c8bb7-1c0b-483d-a7ec-40cd8c3263c3)
- Now the two parts have been separated so each side is now 18 * 10^9 in the worst case so we have simplified our final number of calculations to 2 * 18 * 10^9

## Further Memory Simplifications
1. We only need to keep track of the current layer we are on so we can technically delete all previous layers/states to save space
2. The right side could technically be preloaded as a JSON file since the calculations will always be the same since we are always solving from a solved state.
3. We can make our map memory efficient
   - Rather than storing the cube map as:
   -   Cube Map: Center piecies will always be in the same orientation
   ```
                 W W W
                 W w W
                 W W W
   
       G G G     R R R     B B B     O O O
       G g G     R r R     B b B     O o O
       G G G     R R R     B B B     O O O
   
                 Y Y Y
                 Y y Y
                 Y Y Y
   ```

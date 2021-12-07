# K&R: Checkers Coursework

## Requirements
Please make sure you have these installed:
- python version `3.6.6` or above
    - Check python version: `python -V` in the Terminal / CMD
- pip version `21.1.1` or above
    - Check pip version: `python -m pip -V` in the Terminal / CMD

 You can install the latest version from [here](https://www.python.org/downloads/).

## How To Run
- Navigate to the base directory using a Terminal / CMD
    - `cd Downloads/KR-Checkers`
- Install the package with pip
    - `python -m pip install .`
    - If the above command gives an error about the Script directory not being on path, copy the returned path to your clipboard
- Run the program
    - If the path error is returned, paste the path and append `PlayCheckers` and enter, if no error was given, simply just run `PlayCheckers`

Have fun!

## Todo
Moving a piece while selection and move are in two separate steps.

- [ ] King piece after claiming piece
- [ ] Multi-leg moves
    - Check surrounding tiles if opposition piece is there with empty tile after then jump
    - annoying so will do at end if have time
- [ ] Make the help display a toggle
    - Side menu thingy
- [ ] Make the ai
    - [ ] Good state representation
    - [ ] Heuristic thingy for good moves
    - [ ] etc etc 
- [ ] Rules button with menu
- [ ] GUI pauses on multi-leg moves

## Guidelines Overview
- Gameplay (20 marks) 
    - [ ] Interactive checkers gameplay (Human vs. Computer) of some sort 
    - [ ] Different levels of verifiably effective AI cleverness, adjustable by the user  
 
- Search algorithm (20 marks) 
    - [ ] Appropriate and efficient state representation 
    - [ ] Reasonable successor function to generate AI moves 
    - [ ] Minimax evaluation 
    - [ ] Alpha-Beta pruning 
    - [ ] Appropriate use of heuristics  

- Validation of moves (16 marks) 
    - [ ] No invalid moves carried out by the AI 
    - [ ] Automatic check for valid user moves 
    - [ ] Rejection of invalid user moves, with a specific explanation given 
    - [ ] Forced capture - if a player can capture an enemy piece they have to do so. If there is more than one capturing opportunity in the same turn, the user may choose which one to take.  

- Other features (20 marks) 
    - [ ] Multi-leg capturing moves for the user 
    - [ ] Multi-leg capturing moves for the AI 
    - [ ] King conversion at baseline (The king's row) as per the normal rules 
    - [ ] Regicide - if a normal piece manages to capture a king, it is instantly crowned king and then the current turn ends. 
    - [ ] Some kind of help feature that can be enabled at the user's request to get hints about available moves, given the current game state. Sophisticated implementations should employ the AI functionality to make suggestions on optimal moves. 
 
- Human-Computer Interface (up to 4 marks each)  
    - [x] Some kind of board representation displayed on screen 
    - [ ] The interface properly updates the display after completed moves (User and AI moves) 
    - [x] Fully interactive GUI that uses graphics (You are permitted to use tools that make it easier to construct a GUI by generating the necessary code, such as layout managers provided with Java IDEs like Eclipse or NetBeans)  
    - [x] Mouse interaction focus, e.g., click to select & click to place, or drag & drop (better) 
    - [ ] GUI pauses appropriately to show the intermediate steps of any multi-leg moves 
    - [ ] Dedicated display of the rules (e.g., a corresponding button opening a pop-up window) 


# K&R: Checkers Coursework

## Requirements
Please make sure you have these installed:
- python version `3.9.6` or above
    - Check python version: `python3 -V` in the Terminal / CMD
- pip version `21.2.3` or above
    - Check pip version: `pip3 -V` in the Terminal / CMD

 You can install the latest version from [here](https://www.python.org/downloads/).

## How To Run
- Navigate to the base directory using a Terminal / CMD
    - `cd Downloads/KR-Checkers`
- Install the package with pip
    - `pip3 install .`
- Run the program
    - `PlayCheckers`

Have fun!

## Todo
- [ ] Movement
    - [ ] King
    - [ ] Auto capture
- [ ] Help menu
- [ ] Win situations

## Guidelines Overview
1. Gameplay (20 marks) 
    a. [ ] Interactive checkers gameplay (Human vs. Computer) of some sort 
    b. [ ] Different levels of verifiably effective AI cleverness, adjustable by the user  
 
2. Search algorithm (20 marks) 
    a. [ ] Appropriate and efficient state representation 
    b. [ ] Reasonable successor function to generate AI moves 
    c. [ ] Minimax evaluation 
    d. [ ] Alpha-Beta pruning 
    e. [ ] Appropriate use of heuristics  

3. Validation of moves (16 marks) 
    a. [ ] No invalid moves carried out by the AI 
    b. [ ] Automatic check for valid user moves 
    c. [ ] Rejection of invalid user moves, with a specific explanation given 
    d. [ ] Forced capture - if a player can capture an enemy piece they have to do so. If there is more than one capturing opportunity in the same turn, the user may choose which one to take.  

4. Other features (20 marks) 
    a. [ ] Multi-leg capturing moves for the user 
    b. [ ] Multi-leg capturing moves for the AI 
    c. [ ] King conversion at baseline (The king's row) as per the normal rules 
    d. [ ] Regicide - if a normal piece manages to capture a king, it is instantly crowned king and then the current turn ends. 
    e. [ ] Some kind of help feature that can be enabled at the user's request to get hints about available moves, given the current game state. Sophisticated implementations should employ the AI functionality to make suggestions on optimal moves. 
 
5. Human-Computer Interface (up to 4 marks each)  
    a. [ ] Some kind of board representation displayed on screen 
    b. [ ] The interface properly updates the display after completed moves (User and AI moves) 
    c. [ ] Fully interactive GUI that uses graphics (You are permitted to use tools that make it easier to construct a GUI by generating the necessary code, such as layout managers provided with Java IDEs like Eclipse or NetBeans)  
    d. [ ] Mouse interaction focus, e.g., click to select & click to place, or drag & drop (better) 
    e. [ ] GUI pauses appropriately to show the intermediate steps of any multi-leg moves 
    f. [ ] Dedicated display of the rules (e.g., a corresponding button opening a pop-up window) 


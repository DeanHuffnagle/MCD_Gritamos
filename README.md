# MCD_Gritamos

### A bot to complete McDonald's VOICE surveys

## Getting Started:
1. Navigate to the ".env.example" file which should be in the base level of the project. 
2. Copy everything in that file
3. Create a file named ".env"
4. Paste the contents into ".env"
5. fill out the information
   * Both the "API key" and "proxy url" should be able to be found on webshare's website
   
## Adding New Codes:
1. navigate to "TextFiles/newCodes.txt"
2. add your codes in, one per line
3. navigate to "src/code_manipulation.py"
4. run that file
   * This will expand your codes into 10x as many codes then add them to the list of codes to use
   * You can run the file by
     1. selecting the file in the explorer
     2. scrolling down to the play button towards the bottom of the file

#### (IMPORTANT): You can't do this while the bot is in use because it constantly overwrites the file while in use.

## Stopping The Bot:
* The MCD_Gritamos bot will run until it runs out of codes, or runs into an error.
* however if you need to stop it for anyother reason you may press the red square at the top of pycharm.
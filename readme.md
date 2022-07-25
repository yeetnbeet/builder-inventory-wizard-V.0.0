# Builder Inventory Wizard V.0.0
This First iteration of the builder inventory wizard keeps inventory between frames and respective bike builders in balance. It requires two csv files from the following locations:
- [Frames](https://contender-bikes.myshopify.com/admin/products/inventory?location_id=55763894440&tag=internal%3Aprobuild-frame)  
- [Builders](https://contender-bikes.myshopify.com/admin/products/inventory?location_id=55763894440&tag=internal%3Acustom-builder)  

> Please Export as plain csv all variants for best results
> You must be logged into shopify for links to work

Click Export in the top right -> Select 50+ Variants Matching Search. The files will be emailed to you. Download the two csv files - They Should be called BUILDER.csv and FRAMES.csv respectively
> you have to re-name the files, shopify will not name them properly

## Required Software

- [Python](https://www.python.org/downloads/)
- [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- [Basic Knowlege of bash (ie Mac terminal)](https://www.educative.io/blog/bash-shell-command-cheat-sheet)
> git is optional but highly recommended

### Set Up
First Check to make sure you have the proper dependancies installed:
`python3 --version`
`git --version`
Navigate to the desired directory in terminal and glone the git repository: 

`git clone https://github.com/yeetnbeet/builder-inventory-wizard-V.0.0`

Navigate into the program directory find the name using:

`ls` then use `cd foldername`

> by default it has the proper test files so you can run the program
>and make sure everything is working properly

TO RUN: `Python3 app.py` *output to the console should be test logs*

#### Importing the proper CSV files and Using the Program
This part is simple just drag the BUILDER.csv and FRAMES.csv files into the program folder replacing the placeholders **Do Not Remove OUTPUT.csv**. Check the files to make sure they are what they say they are. 
> advanced users: the config object can be intialized to accept any file name or path.
>`class config (self, builderFile = "./BUILDER.csv",framesFile = "./FRAMES.csv",outputFile = "./OUTPUT.csv")`

Once the CSV files are in the correct location you are ready to run the program:
`Python3 app.py` 
> output will be test logs if everything worked correctly
>the output file is now ready but don't close the terminal
>you will need the test logs in the next step

### Uploading The File
STEP 1
Go to shopify->products->inventory: *Cross reference test logs by inputing SKU into search*
STEP 2
If you passed the check at step one hit upload in the top right corner: *Drag OUTPUT.csv*
Step 3
You are done



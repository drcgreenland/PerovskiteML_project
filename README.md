# PerovskiteML_project
This is a repository for Claire Greenland's research project on machine learning for perovskite materials discovery.

Important steps to get started:

1) Install miniconda 3. This is your Python distribution.

2) Add conda paths to system variables.
3) If you have not already done so, create a folder somewhere on your PC that you want to use as your working directory for the project.
4) Go to the GitHub repo (I will invite you as a collaborator so can see the repo) and copy the URL by clicking on "Code".
5) Open VS code. Under the "Start" menu, click "Clone Git Repository", paste URL into the bar in the top middle and click "Clone from URL". This will prompt you to choose a folder as the Repository Destination. Select the folder you created in step 3.
6) Get Python extensions in VS code - the ones you need will most likely be recommended to you by VS code. Make sure Jupyter is included as we will be working on Jupyter notebooks.
7) Open CMD prompt terminal in VS code.
8) Run conda env create test-env to create a virtual environment for running your code.
9) Run conda activate test-env to activate this environment. This now means that any packages you install will only be installed in this environment, which is important for avoiding conflicts between different package dependencies in different coding projects.
10) Run pip install -r requirements.txt to install essential packages into your virtual environment. You can always add more packages later as and when they are needed.
11) Save the data (Perovskite_database_full.csv) into the directory you are working from, in a folder called 'Data'.
12) You will see that in this repository there is a file called .gitignore. This file specifies that anything in the'Data' file you have created will not be synced to the online GitHub repo. We need to do this because it is important not to store any raw data in the GitHub repo.

Now you should be ready to start coding. If you get stuck with any of the first 12 steps, ask Claire.

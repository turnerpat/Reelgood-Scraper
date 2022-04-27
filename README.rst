Reelgood Scraper and Visualizations
====================================
************
Introduction
************
    This is a scrapy spider for the website Reelgood.com. The spider can be run on a variable number of TV and Movie item pages in increments of 50. This documentation will detail how to run the spider and the visualizations that can be generated from it using python packages.

************
Requirements
************
    **Requirements**
        * Anaconda or other Python Interpreter and Prompt

        * Scrapy Python package
            - Install Scrapy onto your machine with conda using:
                    ``$ conda install -c conda-forge scrapy``
            - Alternatively you can install using pip:
                    ``$ pip install Scrapy``
        * Latest version of git (Optional)
            - Check to see if you have the latest version of git with:
                    ``$ git --version``
            - Install git onto your Linux machine with:
                    ``$ sudo apt-get install git``
            - Be sure to configure your user email with:
                    ``$ git config --global user.email <email>``

************
Installation
************
        * Reelgood Spider and Visualizer
            - You may download the files from GitHub_ or clone with:
                    .. _GitHub: https://github.com/turnerpat/Reelgood-Scraper

                    ``$ git clone https://github.com/turnerpat/Reelgood-Scraper.git``

*********
Execution
*********
    After you have the MazeGame files on your machine, follow these steps for executing the program.
        * Change into the directory with:

            ``$ cd MazeGame/``
        * Compile the code with:
            
            ``$ javac MazeGame.java``
        * Execute the code with:

            ``$ java MazeGame.java``

    The code is now being executed and should prompt you to input the name of the text file you wish to use.

        .. image:: images/execute.png

    If you look in the directory you will see two text files are provided for you to serve as the maze maps. The file "easy.txt" is used in the example above.

        .. image:: images/maze.png

    After entering any character to continue the console will display the maze and the game will begin.

        .. image:: images/move.png

    Once the game begins you can move your player token (@) around the maze by entering up, down, left, or right (or u, d, l, r to be simpler) into the console. You may also quit by entering quit or q.

    Your token will leave behind bread crumbs (.) to show where you have been in the maze, making it easier to traverse.

    As you can see, the borders of the maze are made up by + and - characters while the walls within the maze itself are X characters that you cannot move through. 

        .. image:: images/complete.png

    The goal of the game is to move your player token from the starting point (S) to the goal point (G) in as few moves as possible.

****
FAQs
****
        * "How do I change the spider settings?"

            - Spider settings can be found in the reelgoodSpider/reelgoodSpider/settings.py file. 
            - Uncomment or change listed settings in the file to change the spider settings when it runs. 
            - For details on each setting option see the file comments or the Scrapy_ documentation. 
            .. _Scrapy: https://docs.scrapy.org/en/latest/topics/settings.html

        * "Can this code run on Windows and Mac machines?"

            - Yes! As long as you have the means to compile and run the program with Java you can  play the game on any platform. Simply download from GitHub and compile/execute where possible.

            - This could be through an IDE, console, or command line, as long as you know where the files are downloaded and can compile them.

        * "What are the output files for?"

            - The output files provided serve to show what the program will convert the easy and hard text files into. The program will still work without them.

    If you have any questions or remaining issues feel free to contact me at turnerpatrick21@gmail.com.

*********
Licensing
*********
    This project is distributed under an `MIT license <https://opensource.org/licenses/MIT>`_.

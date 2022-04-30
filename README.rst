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
        * Python 3.9 or higher
    
        * Anaconda_ or other Python Interpreter/Prompt
            .. _Anaconda: https://www.anaconda.com/products/distribution
        
        * Scrapy Python package
            - Install Scrapy onto your machine with conda using:
                    ``$ conda install -c conda-forge scrapy``
            - Alternatively you can install using pip:
                    ``$ pip install Scrapy``
        
        * Pandas Python package
            - Install Pandas onto your machine with conda using:
                    ``$ conda install pandas``
            - Alternatively you can install using pip:
                    ``$ pip install pandas``
        
        * Matplotlib Python package
            - Install Scrapy onto your machine with conda using:
                    ``$ conda install matplotlib``
            - Alternatively you can install using pip:
                    ``$ pip install matplotlib``
                    
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
    After you have downloaded files on your machine, follow these steps for executing the program:
        * Open your Anaconda Prompt and change into the directory with:

            ``$ cd reelgoodSpider/reelgoodSpider/spiders/``
        * Run the spider file with:
            
            ``$ scrapy runspider reelgood.py``
        * You may export the data scraped using these arguments:

            ``$ scrapy runspider reelgood.py -o [filename].[filetype] -t [filetype]``
        
        * As an example you can output to csv, json, jsonlines, xml, etc.
        
            ``$ scrapy runspider reelgood.py -o articles.csv -t csv``
            
            ``$ scrapy runspider reelgood.py -o articles.json -t json``
            
            ``$ scrapy runspider reelgood.py -o articles.xml -t xml``
            
    The code is now being executed and will output details of the data scraping to your prompt. If you output to a file it will be written to in the same directory as the reelgood.py file.
    
    .. code-block:: python
    
        class ReelgoodSpider(CrawlSpider):
            name = 'reelgood'
            allowed_domains = ['reelgood.com']
            # Restrict the offset of the movie and tv lists being crawled (by increments of 50 starting at 0)
            # For example: offset = 0 = 50 links per each list, offset = 1 = 100 links per each list, etc.
            offset = 200
            start_urls = []
            i = 0
            for i in range(offset + 1):
                start_urls.append(f'https://reelgood.com/movies?offset={i * 50}')
                start_urls.append(f'https://reelgood.com/tv?offset={i * 50}')
    
    
    The code above is from the top of reelgood.py. As the comments say you can change the offset to determine how many item pages are scraped in increments of 50. For example, the data set generated was used with an offset of 200, meaning 10,000 item pages were scraped each for the main tv and movie page. 
    
    WARNING: Depending on the offset number set in reelgood.py the number of item pages the spider will crawl, and therefore the amount of time taken will vary. Subsequent scrapes can be sped up if HTTP caching is turned on in settings.py (it is on by default). Scrapes are in increments of 50 due to each page of the tv and movie page tables hold 50 items each.
    
    
    TV and Movie pages have different parse methods provided that each scrape over 15 attributes from the page. Attributes scraped include the title, imdb score, reelgood score, list of genre(s), maturity rating, release year(s), runtime for movies, number of seasons for tv, the ongoing/finished status of tv shows, list of streaming services, list of associated tags, country of production, director of movie, top three* billed actors (can be increased, see comments below), link to poster, url, and description of plot/critical reception.
    
    .. code-block:: python
    
        # Change the numbers in the array at the end to determine how many actors are shown:
        # (start from 1 to remove director)
        'actors': response.xpath('//div[@class="css-gq6ll egg5eqo4"]/a/@title').extract()[1:4],
        
    
    Both TV and Movie parsers by default will scrape the top three billed actors from a given production. This can be changed to be less or more by changing the second value in the brackets after .extract(). For example, [1:6] would return the top 4 actors.
    
    visualization details here

****
FAQs
****
        * "How do I change the spider settings?"

            - Spider settings can be found in the reelgoodSpider/reelgoodSpider/settings.py file. 
            - Uncomment or change listed settings in the file to change the spider settings when it runs. 
            - For details on each setting option see the file comments or the Scrapy_ documentation. 
            .. _Scrapy: https://docs.scrapy.org/en/latest/topics/settings.html

        * "How do I turn off caching?"

            - HTTP caching is turned on by default for the reelgood spider, however any cached data has been removed for the release. 
            - If you do not want to cache scraped item pages go to the settings.py file and set HTTPCACHE_ENABLED equal to False.

        * "How do I change attributes, number of pages, etc.?"

            - Actual output and results of running the spider can be manipulated in the reelgoodSpider/reelgoodSpider/spiders/reelgood.py file. Read file comments for more details.
            
        * "What is the 'reelgood.csv' file?"
        
            - This file is an example data set collected by running the spider. It is a collection of over 8000 movie and tv show pages from reelgood.com.               - This is the data set that was used to generate the sample visualizations shown, but are not required to run the spider itself.

    If you have any questions or remaining issues please contact turnerpatrick21@gmail.com.

*********
Licensing
*********
    This project is distributed under an `MIT license <https://opensource.org/licenses/MIT>`_.

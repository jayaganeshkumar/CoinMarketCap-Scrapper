# CoinMarketCap-Scrapper

  This is a web scrapping code which retrieves the data of a particular cypto currency.
  
## Technologies needed:
   Python 3.7<br>
   Chrome Driver
   
 ## Required Libraries
   Selenium <br>
   CSV <br>
   Scrapy <br>
   Datetime <br>
   Time <br>
   BeautifulSoup4 <br>
   Requests <br>
   
   To install these libraries, download the repo, extract it and open the command prompt or terminal in the folder. <br>
   Now run the command: `pip install -r requirements.txt` to install the required libraries. <br>
   
   Now download the chrome driver for Selenium from [https://chromedriver.chromium.org/downloads](Link).<br>
   Check the version of chrome installed and then download the respective driver.
   <br>
   Now open `main.py` in text editor and replace the path for chrome driver in line 8 with your chrome driver path.<br>
   
   Run the code.<br>
 
 ## Execution
   You can find one file named `coins.csv` in the folder with names of 50 crypto currencies from website, [https://coinmarketcap.com/coins/](Link).
   <br>
   Now enter the symbol of any crypto currency, after 5 seconds you can find a file with name `coin_data_<datetime>.csv` created.
   <br>
   The details are in the order:
   <br>
   1. Symbol	
   2. Name	
   3. WatchlistCount	
   4. Website URL
   5. Circulating Supply %
   6. Price
   7. Volume / Market Cap
   8. Market Dominance
   9. Rank
   10. Market Cap 
   11. All Time High - DATE
   12. All Time High - PRICE
   13. All Time Low  - DATE
   14. All Time Low  - PRICE
   15. What is <Coin Name>?
   16. Who are the founders?
   17. What makes it unique?

## Thank you

Introduction
My Capstone project consists of working with time series datasets to conduct market analysis and price forecasting.  My modeling consisted of working with 
technical indicators, LSTM models, and ARIMA models to perform the tasks.  Stock traders and analysts have a lot of tools available to them like technical 
indicators and financial algorithms to perform market analysis and price forecasting.  The goal of my project was to see whether these financial tools 
could be made so anyone could perform market analysis and price forecasting from their laptops, tablets and/or smart phones.  These tools and models would 
need to be created so they are user-friendly for individuals with a non-technical background, easy to understand and produce good results.  The 
algorithms would need to be user-friendly so that all the user needs to do is input the stock symbol and the application would produce the results.  Also, 
there could be some parameter tuning but at a minial level.


I would like to build a platform where subscribers can use deep learning and ARIMA algorithms for price forecasting by simply inputting the stock symbol.  
This platform may already exist and if it does this is an opportunity for me to test the results of such algorithms.  What I set out to determine in my 
Capstone was whether financial tools and algorithms could produce good results with mainly default parameters or minimal tuning of the parameters.  
If I could only get good results with higher levels of parameter tuning then it would be questionable whether subscribers with non-technical and 
non-financial backgrounds could really use these tools.  

The Data
I worked with data from stocks of 6 companies producing COVID-19 vaccines.  I got the data using the library Yahoo Finance.  The library provides sufficient 
stock data consisting of opening, closing price and volume, etc.  It was easy to put the data into Pandas and then I added calculations from the technical 
indicators to the data frames. 

Methodology
The methodology I used was to check the performance of financial tools and algorithms in market analysis and forecasting.  I used only basic 
calculations in Python for the financial indicators and for the financial algorithms using only the default parameters and/or basic tuning of parameters.  
For moving averages I used only 10 and 50 day calculations for the algorithms which are pretty basic.  

I created ARIMA models for the price forecasting.  I used the Auto_Arima models to get the pdqs and lowest AIC for the ARIMA model.  
Regarding LSTM models, I only used 3 layers with no dropout layers and 25 epochs.  For the price forecasting I used One-Step Ahead Forecasting and Dynamic 
Forecasting. 

Modeling:
I used technical indciators to determine the price history, volatility of the stocks and price points when stocks should have been bough and sold.I used 
LSTM and ARIMA models for price forecasting.  My modeling was structured around the following questions:

Question 1: Can technical indicators provide an investor or trader with information to make a decision of whether to buy and sell stocks?
Answer: Yes
Technical indicators are tools used by investors and traders to gain insights regarding the stock's history, volatility, trends and the direction the price 
may be headed. I used moving averages with averages of 10 and 50, MACD crossover strategies and the RSI ( Relative Strength Index)to answer this question.  
The MACD was effective in showing at what points the stock could have been bought or sold.   


Question 2: How well does the LSTM model perform in forecasting stock prices with 'Adj Close' and Technical Indicator columns with default parameters and 
minimal tuning of model parameters?


            Volatility	Min	Max	Mean	RMSE
NVAX	 High	3.6900	319.9290	88.549	27.96
PFE	 Low	25.6990	41.6910	32.999	0.71
MRNA	High	13.9300	186.0200	75.152	24.04
JNJ	Low	108.2136	169.4235	145.426	13.34
BNTX	High	12.7500	208.8990	70.957	22.84
AZN	Low	36.7790	59.4660	49.690	7.17

This first part of this section deals with LSTM models and the 6 pharmaceutical stocks. The data consists of the Adj Close price for each stock. The 
second part I used the PFE stock with the columns 'MA_50' and 'Actual_Changes'. Overall the models performed pretty well. The stocks perfoemd well. As 
expected the stocks that were highly volatile didn't perform as well as those with low volatility stocks but that is expected given their price histories.


Question 3:
Does the SARIMA algorithm perform better in predicting future stocks price with the Adj Close column or Technical Indicators?

                     RMSE/One	     RMSE/Dyn
PFE/Adj Close	       0.53	         3.02
PFE/MA_50	           0.02	         1.57
PFE/Actual_Changes	 0.53	         0.53
BNTX/Adj Close	     6.60	         41.42
BNTX/MA_50	         74.67	       17.24
BNTX/actual_changes	 6.46	         6.67
NVAX /Adj Close	     4.30	         35.11

For each model I ran One-Step Ahead Forecasting and Dynamic Forecasting to see if that made a difference in the models forecasting. Regarding Pfizer, I ran 
the models with the columns Adj_Close, MA_50, Actual_Changes. Pfizer is not a volatile stock. With One-Step Ahead the models did really well and the 
predicitons were off by around 0.53 or less. In Dynamic Forecasting, the models still performed well but with Adj_Close column model was off 3.02.

BNTX is a volatile stock. The average price of the stock was 70.95. However, the price fluctuated from a low of 12.7500 to a high of 208.899. With 
column actual_changes the model performed exceeding well with both one-Step and Dynamic and was off 6.46 and 6.67 for both. The above chart shows that 
with column MA_50 and One-Step the model was off 74.67 which is a lot consdiering the average for price for the MA_50 column was 69.456025.

NVAX is also a volatile stock. One-Step performed really well and predictions were only off $4.30. Overall, I think the models performed pretty well 
consdiering that I used the Auto_Arima model to get the pdqs with lowest AIC and no other tuning.

In response to the question, the models probably perform about the same because the price volatility of the stock have a lot to do with the performance of 
the models.



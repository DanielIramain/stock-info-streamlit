<p align='center'>
  <img src="resources/logo-stock-info.png">
</p>

## Project Description
Stock Info is a web application with the objetive of simplify the process to obtain financial information of companies listed in the [US Stock Market](https://www.nasdaq.com/market-activity/stocks/screener). In its current version allows you to get fundamental data and time series data displayed as DataFrames and can be storaged in CSV format.

For the **fundamental information**, it gets you:
- $${\color{red}Overview:}$$ General information about the company.
- $${\color{red}Income \space Statement:}$$ Income statements for the last 5 periods.
- $${\color{red}Balance \space Sheet:}$$ Balance sheets for the last 5 periods.
- $${\color{red}Cash \space Flow:}$$ Financial statement showing cash flows.
- $${\color{red}Earnings:}$$ Data on the earnings report date, earnings per share, expected EPS, and the absolute and relative "surprise" level.
- $${\color{red}Dividends:}$$ Information on the company's dividend payments by date.
- $${\color{red}Splits:}$$ History of the company's dividend splits.

And by using **time series**:
- $${\color{red}Intraday}$$
- $${\color{red}Daily}$$
- $${\color{red}Weekly}$$
- $${\color{red}Weekly \space Adjusted}$$
- $${\color{red}Monthly}$$
- $${\color{red}Monhtly \space Adjusted}$$
- $${\color{red}Global \space quote \space (last \space price \space and \space volume)}$$

## Tecnologies used
The core of the project is writen in Python using libraries for data analytics such as Numpy and Pandas. There is also some HTML and CSS just for style purposes. Requirements.txt is included in the project.

Framework used: ![Streamlit](https://img.shields.io/badge/Streamlit-%23FE4B4B.svg?style=for-the-badge&logo=streamlit&logoColor=white)

Services used: API REST architecture provided by [Alpha Vantage](https://www.alphavantage.co/)

## How to install and run the project
Once in the IDE of your preference, according to [Streamlit Documentation](https://docs.streamlit.io/get-started/fundamentals/main-concepts), you need to execute the main file command of Streamlit to run the project in your browser, in this case `streamlit_app.py`. Using the terminal:
```
cd stock-info

streamlit run streamlit_app.py
```
Or the equivalent for your OS.


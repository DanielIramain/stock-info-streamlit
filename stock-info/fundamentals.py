import utils
from custom_classes import Fundamentals

import streamlit as st

services = ['income_statement', 
            'balance_sheet', 
            'cash_flow', 
            'earnings', 
            'dividends', 
            'splits']

tab_names = ['Income statement', 'Balance Sheet', 'Cash Flow', 'Earnings', 'Dividends', 'Splits']

st.subheader('Fundamentals: financial statements and reports', divider=True)

st.markdown('##### Currently provides accounting and financial information about the company.')

st.markdown(':red[**Overview:**] General information about the company.')
st.markdown(':red[**Income Statement:**] Income statements for the last 5 periods.')
st.markdown(':red[**Balance Sheet:**] Balance sheets for the last 5 periods.')
st.markdown(':red[**Cash Flow:**] Financial statement showing cash flows.')
st.markdown(':red[**Earnings:**] Data on the earnings report date, earnings per share, expected EPS, and the absolute and relative "surprise" level.')
st.markdown(":red[**Dividends:**] Information on the company's dividend payments by date.")
st.markdown(":red[**Splits:**] History of the company's dividend splits.")

with st.form('Data input'):
    ticker = st.text_input('Company ticker', key='ticker')
    'The ticker of the company you need information about (US MARKET data only).'

    optional = st.selectbox('Select the time lapse: ', ['annual', 'quarterly'], key='optional')
    'This option will modify the display information of time period in: income statement, balance sheet, cash flow and earnings report.'

    api_key = st.text_input('API key', key='key', type="password")
    'The API key from the Alpha Vantage service'

    submit = st.form_submit_button('Obtain data')

if submit:
    fundamentals = Fundamentals(ticker, api_key)
    data_overview = fundamentals.get_overview()

    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            st.dataframe(data_overview[0])
        with col2:
            st.dataframe(data_overview[1])
    
    tabs = st.tabs(tab_names)

    for i, (tab, service) in enumerate(zip(tabs, services)):
        with tab:
            data = fundamentals.get_data(service)
            st.dataframe(data)

    #if services[option] == 'income_statement':
#
    #    data = utils.pipeline(data, ['fiscalDateEnding', 'reportedCurrency'])
    #    
    #    graphs = Grapher(data)
#
    #    graphs.plot_line_chart('Revenue and cost revenue evolution', 'fiscalDateEnding', 
    #                           ['totalRevenue', 'costOfRevenue', 'costofGoodsAndServicesSold'], 
    #                           'Fiscal date ending', 'Revenue and cost expresed in dollars')
    #    
    #    graphs.plot_line_chart('Net income evolution over time', 'fiscalDateEnding', 'netIncome', 
    #                           'Fiscal date ending', 'Net income in dollars')
    #    
    #    graphs.plot_line_chart('EBITDA evolution', 'fiscalDateEnding', 'ebitda', 'Fiscal date ending', 'EBITDA in dollars')
#
    #    col1, col2 = st.columns(2)
    #    with col1:
    #        graphs.plot_line_chart('Gross profit evolution', 'fiscalDateEnding', 'grossProfit', 
    #                               'Fiscal date ending', 'Gross profit expressed in dollars')
    #        
    #        graphs.plot_pie_chart(size=(9, 9),title='Total revenue and cost', 
    #                              data=data, columns=['totalRevenue', 'costOfRevenue'], items_legend=['Total revenue', 'Cost of revenue'])
    #        
    #    with col2:
    #        data['grossProfitMargin'] = ((data['totalRevenue'] - data['costofGoodsAndServicesSold']) / data['totalRevenue']) * 100
#
    #        graphs.plot_line_chart('Gross profit margin evolution', 'fiscalDateEnding', 'grossProfitMargin', 
    #                               'Fiscal date ending', 'Gross profit margin')
    #        
    #        graphs.plot_pie_chart(size=(9,9), title='Costs of the company', data=data, 
    #                              columns=['costofGoodsAndServicesSold', 
    #                                       'sellingGeneralAndAdministrative', 'researchAndDevelopment', 'operatingExpenses'], 
    #                              items_legend=['Cost of goods and services sold', 
    #                                            'General and administrative costs', 'R&D Cost', 'Operating expenses'])
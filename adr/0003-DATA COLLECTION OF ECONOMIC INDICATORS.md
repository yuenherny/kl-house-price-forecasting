# Investigating Current Literature on the Importance of Economic Indicators
Date created: 3 Sep 2023
Date revised: TBD

Author(s): Yu Yuen Hern

## What does the current literature say about the impact of economic indicators on house price?
Several existing literature discovered that economical climate has impact on house price. The following list of factors were compiled by ChatGPT 3.5 with information extracted from the literature review table, cross-checked with each reference:
- **Interest Rate**: Higher interest rates increases the cost of mortgage (Abidoye et al., 2019; Lee et al., 2021).
- **Unemployment Rate**: Higher employment rate increases the number of participants of housing market (Abidoye et al., 2019).
- **Household or Personal Income**: Income affect individual ability to afford housing mortgage (Iliychovski et al., 2022; Abidoye et al., 2019).
- **Credit Availability**: The ease of accessing credit and mortgages from banks (Iliychovski et al., 2022; Al-Marwani, 2015).
- **Money Supply**: Total amount of money circulating in the economy (Zhan et al., 2023; Li et al., 2020).
- **Regulation**: Government policies including fiscal/monetary, land and tax policies (Yu, 2022) and foreign reserves (Lee et al., 2021).
- **Household Size**: Miniaturisation of household (smaller household size) increases demand for residential units (Mohamed et al., 2023; Yu, 2022; Abidoye et al., 2019).
- **Population Growth**: Higher population increases demand for housing (Abidoye et al., 2019).
- **Consumer Psychological Demand**: Higher cultural level of consumers contribute to higher quality of life and therefore real estate demand (Yu, 2022).
- **Environmental Factors**: Natural environmental conditions like landscapes, municipal infrastructure (transportation facilities, post and telecommunications facilities, and water supply and drainage facilities) and water supply and drainage facilities, public building supporting facilities conditions (Yu, 2022; Lee et al, 2021).
- **Social Factors**: Politics, social security, urbanization development level (Yu, 2022) and crime rate (Lee et al., 2021; Yu, 2022).

Comparing this with response from ChatGPT 3.5 without any context on the given literature:
- **Interest Rates**: The prevailing interest rates set by central banks can significantly impact mortgage rates. Lower interest rates often lead to lower borrowing costs, which can stimulate demand for housing and drive up prices.
- **Income Levels**: Household incomes play a crucial role in determining the affordability of homes. Rising incomes can enable more people to enter the housing market and bid up prices.
- **Employment and Unemployment Rates**: Low unemployment rates and a strong job market generally support housing demand and can lead to higher prices.
- **Consumer Confidence**: Consumer sentiment about the economy can affect people's willingness to make large investments like buying a home. High consumer confidence can drive housing demand.
- **Supply and Demand**: The basic principles of supply and demand apply to the housing market. When there's a shortage of housing relative to demand, prices tend to rise, and vice versa.
- **Housing Inventory**: The number of homes available for sale in a particular market can influence prices. A tight housing inventory can lead to bidding wars and higher prices.
- **Inflation**: Moderate inflation can contribute to rising home prices as it erodes the purchasing power of money over time. Real estate is often seen as a hedge against inflation.
- **Government Policies**: Government policies, such as tax incentives, subsidies, and regulations, can impact housing affordability and demand. For example, tax credits for first-time homebuyers can boost demand.
- **Credit Conditions**: Access to credit and the ease of obtaining mortgages can affect housing demand. Tighter lending standards can restrict access to credit and slow down price growth.
- **Population Growth**: Areas experiencing significant population growth may see increased demand for housing, leading to higher prices.
- **Infrastructure and Amenities**: Investments in infrastructure, transportation, and the development of amenities like schools and parks can make an area more attractive, potentially driving up property values.
- **Speculation**: Investor sentiment and speculative activity can also influence house prices. When investors believe prices will rise, they may buy properties with the expectation of selling them at a profit later.
- **Global Economic Factors**: International economic conditions, such as exchange rates and global economic crises, can indirectly impact housing markets, especially in areas with a high proportion of foreign buyers.
- **Local Factors**: Local conditions, including neighborhood characteristics, crime rates, and school quality, can have a significant impact on house prices within a specific area.

The economic indicators extracted from literature aligns with most of ChatGPT's suggestions, except for:
- speculation
- global economic factors
- consumer confidence
- supply and demand
- housing inventory
- inflation
- local factors

As much as we want to include as much indicators as possible, the data of these indicators are not publicly available and difficult to measure, therefore will be omitted in this project, except for inflation which is publicly available.

## Collecting data on the economic indicator
With the list of economic indicators, the data collection stage ensues. The following are the possible data source of economic indicators for Malaysia:
- **Interest Rate**: [BNM OPR Decisions 2004-2023](https://www.bnm.gov.my/monetary-stability/opr-decisions)
- **Unemployment Rate**: [DOSM Annual Unemployment Rate 1982-2021](https://open.dosm.gov.my/data-catalogue/dosm-public-economy_labour-principalstats-annual_5)
- **Household or Personal Income**: [DOSM Annual Mean Household Income by State (KL) 1970-2022](https://open.dosm.gov.my/data-catalogue/dosm-public-economy_hiesba_timeseries_state_3) or [DOSM Annual Median Household Income by State (KL) 1995-2022](https://open.dosm.gov.my/data-catalogue/dosm-public-economy_hiesba_timeseries_state_2) 
- **Credit Availability**: Difficult to quantify, thus omitted.
- **Money Supply**: [DOSM Total Money Supply 2013-2021](https://www.data.gov.my/data/ms_MY/dataset/total-money-supply)
- **Regulation**: Difficult to quantify, thus omitted.
- **Household Size**: No direct data found. [DOSM Number of Households by State (KL) 1995-2022](https://open.dosm.gov.my/data-catalogue/dosm-public-economy_hiesba_timeseries_state_1) are used instead with the assumption that the number of households increase as the household size decreases.
- **Population Growth**: [DOSM Population by State 2016-2020](https://statsdw.dosm.gov.my/population/)
- **Consumer Psychological Demand**: Difficult to quantify, thus omitted.
- **Environmental Factors**: Difficult to quantify, this omitted.
- **Social Factors**: [DOSM Violent Crime by State (KL) 2015-2021](https://open.dosm.gov.my/violent-property-crime/kul) and [DOSM Malaysian Economic and Social Wellbeing Index 2000-2021](https://www.data.gov.my/data/ms_MY/dataset/malaysian-well-being-index)
- **Inflation**: [DOSM Consumer Price Index 2010-2023](https://open.dosm.gov.my/data-catalogue/dosm-public-economy_cpi_headline_1)

Most of the data can be downloaded into XLSX/CSV format, except the historical interest rates by BNM. Thus, the data is scraped using `selenium` as the BNM website has anti-bot mechanism.

## References
Abidoye, R. B., Chan, A. P. C., Abidoye, F. A., & Oshodi, O. S. (2019). Predicting property price index using artificial intelligence techniques: Evidence from Hong Kong. International Journal of Housing Markets and Analysis, 12(6), 1072–1092. https://doi.org/10.1108/IJHMA-11-2018-0095

Al-Marwani, H. A. (2015). Modelling and Forecasting Property Types’ Price Changes and Correlations within the City of Manchester, UK. Studies in Business and Economics, 18(2), 5–16. https://doi.org/10.29117/sbe.2015.0087

Iliychovski, S., Filipova, T., & Petrova, M. (2022). Applied aspects of time series models for predicting residential property prices in Bulgaria. Problems and Perspectives in Management, 20(3), 588–603. https://doi.org/10.21511/ppm.20(3).2022.46

Lee, S.-H., Kim, J.-H., & Huh, J.-H. (2021). Land Price Forecasting Research by Macro and Micro Factors and Real Estate Market Utilization Plan Research by Landscape Factors: Big Data Analysis Approach. Symmetry, 13(4), 616. https://doi.org/10.3390/sym13040616

Li, Y., Xiang, Z., & Xiong, T. (2020). The Behavioral Mechanism and Forecasting of Beijing Housing Prices from a Multiscale Perspective. Discrete Dynamics in Nature and Society, 2020, 1–13. https://doi.org/10.1155/2020/5375206

Mohamed, H. H., Ibrahim, A. H., & A. Hagras, O. (2023). Forecasting the Real Estate Housing Prices Using a Novel Deep Learning Machine Model. Civil Engineering Journal, 9, 46–64. https://doi.org/10.28991/CEJ-SP2023-09-04

Yu, F. (2022). Real estate price forecasting based on fundamental analysis. BCP Business & Management, 34, 309–316. https://doi.org/10.54691/bcpbm.v34i.3030

Zhan, C., Liu, Y., Wu, Z., Zhao, M., & Chow, T. W. S. (2023). A hybrid machine learning framework for forecasting house price. Expert Systems with Applications, 233, 120981. https://doi.org/10.1016/j.eswa.2023.120981
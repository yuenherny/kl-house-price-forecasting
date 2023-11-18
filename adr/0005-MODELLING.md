# Modelling: Time Series Forecasting of Real Estate Prices

Date created: 16 Nov 2023
Date revised: TBD

Author(s): Yu Yuen Hern

## Data Type
Data associated with forecasting can be categorised into several types:
1. Time series data: One observation per timestamp, collected at regular intervals over time (Hyndman & Athanasopoulos, 2018)
2. Cross-sectional data: One observation per entity, collected at the same point in time (Hyndman & Athanasopoulos, 2018)
3. Panel / pooled data: One observation per entity, collected at multiple points in time (Dielman, 1983)

The collected data from Brickz.my is a collection of purchase transactions of real estate, with transaction date as time element. As there are no limitations of the number of transactions per day, each timestamp can have more than one data point.

Each transaction is a cross-sectional data containing other external features which could impact price per square feet. Moreover, the data is collected at different points in time. Thus, it is a panel / pooled data.




# References
1. Dielman, 1983: https://www.jstor.org/stable/2685870
2. Hyndman & Athanasopoulos, 2018: https://otexts.com/fpp2/data-methods.html#data-methods
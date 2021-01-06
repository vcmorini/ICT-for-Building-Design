# building-design
Smart Building project

In this project, the following tasks were accomplished:
1) Modeling of a house with Design Builder Software. Output: IDF file;
2) IDF file parameters optimization to reduce the building power consumption. The optimized parameters are: insulation, glazing, WWR, orientation;
3) 3 years simulation of power consumption, electricity, inside and ouside temperatures;
4) Upload of the simulated data into local InfluxDB;
5) Connection of local Grafana and local InfluxDB, and creation of a dashboard to show the data;
6) InfluxDB data retrieval in SQL-like language, and energy signature characterization;
7) Forecasting of total power consumption (cooling power+heating power) with Arima model.

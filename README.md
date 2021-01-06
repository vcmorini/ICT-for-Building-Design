# Smart Building project

In this project, the following tasks were accomplished:
1) Modeling of a dummy house. Output: IDF file. SW: Design Builder;
2) IDF file parameters optimization to reduce the building power consumption. Optimized parameters: insulation, glazing, WWR, and orientation. SW: Besos and EnergyPlus (Python);
3) 3-years simulation of power consumption (for cooling and heating), electricity, inside and ouside temperatures. SW: EnergyPlus (Python);
4) Upload of the simulated data into a local database (InfluxDB);
5) Connection of a local platform (Grafana) with the local database (InfluxDB), and creation of a dashboard in Grafana to visualize the data;
6) InfluxDB data retrieval in SQL-like language, and energy signature characterization. Language: Python;
7) Forecasting of total power consumption (cooling power+heating power) with Arima model. Language: Python.

Tools:
Design Building Software (Student Edition)
Python
InfluxDB
Grafana

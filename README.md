# Smart Building project

### In this project, the following tasks were accomplished:
1) Modeling of a dummy house. Output: IDF file. SW: Design Builder;
2) IDF file parameters optimization to reduce the building power consumption. Optimized parameters: insulation, glazing, WWR, and orientation. SW: Besos/EnergyPlus (Python);
3) 3-years simulation of power consumption (for cooling and heating), electricity, inside and ouside temperatures. SW: Besos/EnergyPlus (Python);
4) Upload of the simulated data into a local database (InfluxDB);
5) Connection of a local platform (Grafana) with the local database (InfluxDB), and creation of a dashboard in Grafana to visualize the data;
6) InfluxDB data retrieval in SQL-like language, and energy signature characterization. Language: Python;
7) Forecasting of total power consumption (cooling power+heating power) with Arima model. Language: Python.

### Tools:
Design Building Software (Student Edition);
Python;
InfluxDB;
Grafana

# Authors
* [Anastasya Isgandarova](https://github.com/ianastasiya)
* [Cansu Ilter](https://github.com/cansuilter)
* Samane
* [Victor de Castro Morini](https://github.com/vcmorini)

# Dummy Building
## Design Builder
![alt text](https://github.com/vcmorini/building-design/blob/main/design_builder_dummy.PNG?raw=true)
## Besos IDF Visualization
![alt text](https://github.com/vcmorini/building-design/blob/main/design_builder_besos_dummy.PNG?raw=true)

# Graphana Dashboard
![alt text](https://github.com/vcmorini/building-design/blob/main/graphana_dashboard.JPG?raw=true)

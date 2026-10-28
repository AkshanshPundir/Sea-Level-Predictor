# Sea Level Predictor

A Python data analysis project developed as part of the freeCodeCamp *Data Analysis with Python* certification. This program uses **Pandas**, **Matplotlib**, and **SciPy** to model global average sea level changes and forecast predictions through the year 2050.

---

## Key Features & Operations

* **Scatter Plot Generation:** Plots historical sea level data from 1880 to 2014.
* **Global Line of Best Fit:** Computes the slope and intercept using all available data via `linregress` and extends the prediction line to 2050.
* **Recent Trend Line of Best Fit:** Calculates a secondary regression line utilizing only data from the year 2000 onward to highlight accelerated rise rates through 2050.
* **Custom Styling:** Formats axes labels (`Year`, `Sea Level (inches)`) and chart title (`Rise in Sea Level`).

---

## Tech Stack

* **Language:** Python
* **Data Science & Stats:** Pandas, SciPy (`linregress`)
* **Visualization:** Matplotlib
* **Testing:** Unittest framework

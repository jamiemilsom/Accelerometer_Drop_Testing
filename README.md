# Accelerometer Drop Test Analysis

This repository contains a Python script for analyzing accelerometer data obtained from drop tests. The script processes the data, performs interpolation and convolution, and visualizes the acceleration over time for each drop test.

## Requirements

To run the script, you need to have the following dependencies installed:

- `pandas`: A library for data manipulation and analysis.
- `numpy`: A library for numerical computing in Python.
- `scipy`: A library for scientific computing in Python, used for interpolation and signal processing.
- `matplotlib`: A plotting library for creating visualizations.
- `seaborn`: A data visualization library based on matplotlib.

You can install the required dependencies using pip:

```
pip install pandas numpy scipy matplotlib seaborn
```

## Usage

1. Clone the repository to your local machine or download the code files.

2. Ensure that you have the accelerometer data files in CSV format stored in the specified folder (`/home/jamie/Documents/Accelerometer_Drop_Testing/2023-05-26 Drop Test C25`).

3. Open the Python script in a Jupyter Notebook or any Python IDE.

4. Set the `sample_rate_hz` variable to the desired sample rate of the accelerometer data.

5. Run the script.

The script will iterate through each CSV file in the specified folder, process the data, and generate plots showing the acceleration over time for each drop test. The processed data includes interpolation and convolution to enhance the accuracy of the results.

## Results

The script generates two sets of plots:

1. **Raw Acceleration Data**: This set of plots shows the raw acceleration data for each drop test. Each plot represents a different drop test, with the time (ms) on the x-axis and acceleration (m/s^2) on the y-axis.

2. **Convolved Acceleration Data**: This set of plots shows the convolved acceleration data for each drop test. Convolution is applied to smooth the acceleration signal and reduce noise. Similar to the raw data plots, each plot represents a different drop test, with time (ms) on the x-axis and convolved acceleration (m/s^2) on the y-axis.

The plots provide insights into the acceleration profiles during the drop tests, allowing for further analysis and interpretation of the results.

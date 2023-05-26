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

## AccelerometerDropTest Class

The `AccelerometerDropTest` class is defined in the code to encapsulate the functionality related to processing accelerometer data for drop tests. Here is a breakdown of the class and its methods:

### `__init__(self, path, sample_rate_hz)`

The constructor method initializes an instance of the `AccelerometerDropTest` class. It takes in the path to the accelerometer data file (`path`) and the sample rate in hertz (`sample_rate_hz`). Within this method:

1. The file name is extracted from the given path.
2. The first line of the CSV file is modified to ensure it ends with a comma.
3. The data is read from the CSV file into a `pandas` DataFrame.
4. Column names are renamed to more descriptive labels.
5. Additional columns for time in milliseconds (`Time (ms)`) and acceleration in meters per second squared (`Acceleration m/s^2`) are added to the DataFrame based on the index and the accelerometer data in the original columns.

### `interpolate_acceleration(self)`

This method performs interpolation on the acceleration data to create a uniformly spaced time series of acceleration values. The interpolated data is stored in a new DataFrame called `TC_data`. The steps involved are:

1. The minimum and maximum time values from the original data are determined.
2. The number of points required for interpolation is calculated based on a time resolution of 0.25 milliseconds.
3. The `TC_data` DataFrame is created with a new column for time.
4. The `interp1d` function from `scipy.interpolate` is used to perform cubic interpolation on the original acceleration data, generating a smooth curve for the new time series.

### `calculate_velocity(self)`

This method calculates the velocity based on the interpolated acceleration data in the `TC_data` DataFrame. The velocity is computed using the `cumtrapz` function from `scipy.integrate` with the time and acceleration data as inputs. The resulting velocity values are stored in a new column called `Velocity m/s`.

### `convolve_velocity(self, length_of_kernel)`

This method applies convolution to the velocity data in the `TC_data` DataFrame to smooth the signal and reduce noise. The convolution is performed using a kernel created from a vector of ones divided by the specified `length_of_kernel`. The resulting convolved velocity values are stored in a new column called `Convolved Velocity m/s`.

### `convolve_acceleration(self, length_of_kernel)`

Similar to the previous method, this method applies convolution to the acceleration data in the `TC_data` DataFrame to smooth the signal and reduce noise. The resulting convolved acceleration values are stored in a new column called `Convolved Acceleration m/s^2`.

### `__repr__(self)`

The `__repr__` method overrides the default representation of the class and returns a string that provides information about the accelerometer drop test, including the name of the file.

This class provides a convenient way to process accelerometer data for drop tests and perform operations such as interpolation, velocity calculation, and convolution on the data.


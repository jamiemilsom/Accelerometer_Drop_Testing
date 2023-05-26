import os
import numpy as np
import pandas as pd
from scipy.interpolate import interp1d
from scipy.signal import convolve
from scipy.integrate import cumtrapz

class AccelerometerDropTest:
     def __init__(self,path,sample_rate_hz):
          self.path = path
          
          self.filename = os.path.basename(path)[:-4]

          with open(path,'r') as file:
               first_line = file.readline().rstrip()

          if not first_line.endswith(','):
               first_line += ','
          
          with open(path, 'r+') as file:
               content = file.readlines()
               content[0] = first_line + '\n'
               file.seek(0)
               file.writelines(content)

          self.data = pd.read_csv(path)
          self.data.rename(columns={self.data.columns[0]: 'Time h/m/s/ms', self.data.columns[1]: 'Device Name'}, inplace=True)
          
          self.data['Time (ms)'] = (self.data.index / sample_rate_hz) * 1000
          self.data['Acceleration m/s^2'] = self.data['Acceleration Y(g)'] * 9.81
          
            
     def interpolate_acceleration(self):
          
          min_time = self.data['Time (ms)'].min()
          max_time = self.data['Time (ms)'].max()
          num_points = int((max_time - min_time) / 0.25) + 1
          self.TC_data = pd.DataFrame()
          self.TC_data['Time (ms)'] = np.linspace(min_time, max_time, num_points)
                
          acceleration_interp_func = interp1d(self.data['Time (ms)'], self.data['Acceleration m/s^2'],kind='cubic')
          self.TC_data['Acceleration m/s^2'] = acceleration_interp_func(self.TC_data['Time (ms)'])
          
     def calculate_velocity(self):
          self.TC_data['Velocity m/s'] = cumtrapz(self.TC_data['Acceleration m/s^2'],x=self.TC_data['Time (ms)'],initial=0) / 1000
          
     def convolve_velocity(self, length_of_kernel):
          convolve_vector = np.ones(length_of_kernel) / length_of_kernel
          self.TC_data['Convolved Velocity m/s'] = convolve(self.TC_data['Velocity m/s'].values,convolve_vector,mode='same')
          
     def convolve_acceleration(self, length_of_kernel):
          convolve_vector = np.ones(length_of_kernel) / length_of_kernel
          self.TC_data['Convolved Acceleration m/s^2'] = convolve(self.TC_data['Acceleration m/s^2'].values,convolve_vector,mode='same')

     def __repr__(self):
               return "This is an accelerometer drop test with the name '{filename}'".format(filename = self.filename)
               


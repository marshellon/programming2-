# Week 2.7

This script predicts anomelies in sensor data using a previously trained model.
This data is available for download from kaggle: https://www.kaggle.com/datasets/nphantawee/pump-sensor-data

All results will be saved in a log folder by the script. This is not given and should be.
To collect all of the plots, the image folder is required. 
The data folder is required to retrieve fresh incoming data.

# usage
Create the folders shown below:
- data: the fetcher.py scripts will retrieve data from the data folder.
- img: in order to save the plots
- log: to record the entire process

Simply run the fetcher.py script to start the program.
The fetcher script will no longer run and process the data stored in the data folder.
Make sure that the data is in csv format and that only sensor data lookalikes are processed.


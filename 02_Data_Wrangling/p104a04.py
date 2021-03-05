# Standard imports.
import saspy
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from IPython.display import HTML
from datetime import datetime

# Get a SAS session object
sas = saspy.SASsession(cfgname="oda")

# Assign the PG1 library
sas.saslib('pg1', engine='base', path='~/PG1/Data/data/data')

# Creat a new DataFrame object by pulling PG1.STORM_SUMMARY data from SAS.
storm_df = sas.sasdata('STORM_SUMMARY', 'PG1').to_df()

# Drop the columns we don't want and create a new DataFrame
storm_length_df = storm_df.drop(columns=['Hem_EW', 'Hem_NS', 'Lat', 'Lon'])

# Create a new column as the delta of EndDate and StartDate
storm_length_df['StormLength'] = storm_length_df['EndDate'] - storm_length_df['StartDate']

# Print first 5 rows
storm_length_df.head()

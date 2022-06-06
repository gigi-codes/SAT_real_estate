# this script remotely imports REALTOR.COM dataset to my machine, 
# outputs a smaller subset as realtor.csv
# kept crashing browser! Couldn't download. 

import pandas as pd


data_url ='https://econdata.s3-us-west-2.amazonaws.com/Reports/Core/RDC_Inventory_Core_Metrics_Zip_History.csv'

realtor = pd.read_csv(data_url) # importing external data directly from realtor.com url

# extracting select series: only need time, zip, and price information
prop_val = realtor[['month_date_yyyymm', 'postal_code', 'median_listing_price', 'median_listing_price_mm', 'median_listing_price_yy',
                'average_listing_price', 'average_listing_price_yy']] 

# exporting slice to csv in same directory, may modify if I move code location 
prop_val.to_csv('realtor.csv')

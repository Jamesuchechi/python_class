import pandas as pd
from strata_client import StrataClient

# Initialize the client inside a context manager
with StrataClient() as client:
    # Fetch the dataset artifact from the Strata cloud platform
    table = client.fetch("strata://datasets/customer_churn_events.parquet")
    
    # Convert it directly to a Pandas DataFrame
    df = table.to_pandas()

# Now you can use your dataset normally
print(df.head())

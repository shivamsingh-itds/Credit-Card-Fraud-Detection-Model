import pandas as pd

# Load full dataset
df = pd.read_csv("data/raw/fraudTest.csv")

# Take random sample 
sample_df = df.sample(n=5000, random_state=42)

# Save sample
sample_df.to_csv("data/raw/fraud_sample.csv", index=False)

print("Sample file created successfully!")

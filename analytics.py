import pandas as pd
import os
import streamlit as st  

# Initialize or load analytics data
analytics_file = "analytics.csv"
if os.path.exists(analytics_file):
    df = pd.read_csv(analytics_file)
else:
    df = pd.DataFrame(columns=["intent", "count"])
    df.to_csv(analytics_file, index=False)

def update_analytics(intent):
    global df
    if intent in df.intent.values:
        df.loc[df.intent == intent, "count"] += 1
    else:
        df = pd.concat([df, pd.DataFrame({"intent": [intent], "count": [1]})], ignore_index=True)
    df.to_csv(analytics_file, index=False)

def show_analytics():
    st_df = pd.read_csv(analytics_file)
    st.dataframe(st_df.sort_values(by="count", ascending=False), use_container_width=True)

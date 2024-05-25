import streamlit as st
import pandas as pd

# Load the CSV data
csv_file = 'tour_de_france.csv'
df = pd.read_csv(csv_file)

# App title with an image
st.title('🏆 Tour de France Stage Winning Details')
st.image('Le_Tour_de_France_2015_Stage_21_(19992460678).jpg', use_column_width=True)

# Introduction
st.markdown("""
## Welcome to the Tour de France Stage Winning Details App!

This app provides detailed information about the stages of the Tour de France, including stage types, distances, origins, destinations, and winners up until 2017.
""")

# Display the data
st.header('📊 Tour de France Stages Data')
st.dataframe(df)

# Summary statistics
st.header('📈 Summary Statistics')
st.write(df.describe())

# Filter by stage type
st.header('🔎 Filter by Stage Type')
stage_type = st.selectbox('Select Stage Type:', df['Type'].unique())
filtered_data = df[df['Type'] == stage_type]
st.write(filtered_data)

# Display winners by country
st.header('🌍 Winners by Country')
country_count = df['Winner_Country'].value_counts().reset_index()
country_count.columns = ['Country', 'Number of Wins']
st.bar_chart(country_count.set_index('Country'))

# Display stages by date
st.header('📅 Stages by Date and Distance')
st.line_chart(df.set_index('Date')['Distance'])

# Filter by winner's country
st.header('🏅 Filter by Winner\'s Country')
winner_country = st.multiselect('Select Winner\'s Country:', df['Winner_Country'].unique())
if winner_country:
    filtered_data = df[df['Winner_Country'].isin(winner_country)]
    st.write(filtered_data)
else:
    st.write(df)

# Additional analysis or visualizations can be added here

# Footer
st.markdown("""
---
Created with ❤️ using [Streamlit](https://streamlit.io/)

App developed with the assistance of [ChatGPT](https://openai.com/chatgpt).

Source code available on [GitHub](https://github.com/ishara/tour-de-france).

Data source: [Kaggle](https://www.kaggle.com/datasets/ralle360/historic-tour-de-france-dataset).
""")

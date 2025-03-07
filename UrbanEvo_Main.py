# Urban Evo - Demo

import streamlit as st


st.set_page_config(
    page_title="Urban Evo Main",
   # page_icon="👋",
    layout="wide"
)

#st.set_page_config(layout="wide")
st.markdown("# Urban Evo")
st.sidebar.markdown("# Urban Evo")



st.header("Urbanization Probability Prediction", divider=True)
#st.subheader("Predict the probability of urbanization across locations .")


st.markdown(
    """
    Forecasting of urbanization can be a challenging task and can be crucial for urban development, healthcare, education etc. 
    Global trends may show varying population growth in different regions and there might be multiple factors affecting this. 
    Hence, predicting the growth of urban areas can be a bit tricky using the traditional statistical methods. 

    **Urban-Evo model predicts the probability of urbanization across locations over the next five year period.**
    It uses geospatial climatic, vegatation & population growth data from earth engine to predict urbanization.""")
st.image("static/final_2.gif", caption="Comparison of 5 year Ground Truths and predictions for cities in Maharashtra")


st.markdown("""
    ### Want to learn more?
    - 👈 Check out the data/training pipelines used for the model & the results!
    - st.page_link("pages/4_Results.py", label="Check out the prediction results!", icon="🌎") """)
st.markdown("""
    ### Want to see the predictions in action?""")
st.page_link("https://ee-mayuresh.projects.earthengine.app/view/urban-evo-demo", label="Check Out the Visualization in the interactive Earth Engine app!", icon="🌎")
st.page_link("pages/4_Results.py", label=":blue[:link:  View the prediction results here!]", icon="🌎")
st.markdown("""
    ### Want to learn more?
    - [🌎 View prediction results here!](pages/4_Results.py)""")
st.markdown("""
[:link: Check Out the Visualization in the interactive Earth Engine app!](https://ee-mayuresh.projects.earthengine.app/view/urban-evo-demo)
""")
st.markdown("""[:link: View the prediction results here!](pages/4_Results.py")
""")



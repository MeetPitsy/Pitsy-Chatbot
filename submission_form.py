import streamlit as st

# Function to draw the form
def draw_form():
    with st.form(key='manufacturing_form'):
        st.write("Product Details")
        product_details = st.text_area(label="Could you provide us with detailed specifications for the deodorant you want us to manufacture? What materials are used? Who do you source each material from? Weight of each unit?")

        st.write("Packaging Design")
        packaging_design = st.text_area(label="What are your packaging requirements? Measurements for the container?")

        st.write("Timeline")
        timeline = st.text_input(label="What is your desired timeline for the initial production run and subsequent runs?")

        st.write("Pricing")
        pricing = st.text_input(label="What is your budget for the manufacturing process? Are there specific cost targets per unit we should aim to meet?")

        st.write("Distribution")
        distribution = st.text_area(label="What do you use to ship your finished product?")

        st.write("Sustainability")
        sustainability = st.text_area(label="Do you have any specific environmental or ethical standards that our manufacturing process needs to uphold?")

        submit_button = st.form_submit_button(label='Submit')

# Title of the app
st.title("Deodorant Manufacturing Submission Form")

# Drawing the form
draw_form()

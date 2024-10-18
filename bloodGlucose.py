import streamlit as st

def glucose_assessment(fasting_glucose=None, random_glucose=None):
    """
    Assess the blood glucose level based on fasting or random glucose tests.
    
    Args:
    fasting_glucose (float): Fasting glucose level in mg/dL
    random_glucose (float): Random glucose level in mg/dL
    
    Returns:
    str: Blood glucose level assessment.
    """
    if fasting_glucose is not None:
        if fasting_glucose < 100:
            return "Normal fasting glucose."
        elif 100 <= fasting_glucose <= 125:
            return "Pre-diabetes (Impaired Fasting Glucose)."
        else:
            return "Diabetes (High fasting glucose)."
    
    if random_glucose is not None:
        if random_glucose < 140:
            return "Normal random glucose."
        elif 140 <= random_glucose < 200:
            return "Pre-diabetes (Impaired Glucose Tolerance)."
        else:
            return "Diabetes (High random glucose)."
    
    return "Invalid input. Provide fasting or random glucose."

def estimate_hba1c(avg_glucose):
    """
    Estimate HbA1c based on average blood glucose levels.
    
    Args:
    avg_glucose (float): Average glucose level in mg/dL
    
    Returns:
    float: Estimated HbA1c level.
    """
    hba1c = (avg_glucose + 46.7) / 28.7
    return round(hba1c, 2)

# Streamlit app UI
st.title("Blood Glucose Level Assessment and HbA1c Estimation")

# User input for fasting glucose
fasting_glucose = st.text_input("Enter your fasting glucose level (mg/dL)", "")

# User input for random glucose
random_glucose = st.text_input("Enter your random glucose level (mg/dL)", "")

# User input for average glucose (for HbA1c)
avg_glucose = st.text_input("Enter your average glucose level (mg/dL) for HbA1c estimation", "")

# Assess glucose and estimate HbA1c when the button is pressed
if st.button("Assess and Estimate"):
    # Convert inputs to float if provided
    fasting_value = float(fasting_glucose) if fasting_glucose else None
    random_value = float(random_glucose) if random_glucose else None
    avg_value = float(avg_glucose) if avg_glucose else None
    
    if avg_value:
        glucose_result = glucose_assessment(fasting_value, random_value)
        hba1c_result = estimate_hba1c(avg_value)
        
        # Display the results
        st.subheader("Results:")
        st.write(f"Glucose Assessment: {glucose_result}")
        st.write(f"Estimated HbA1c: {hba1c_result}")
    else:
        st.error("Please enter your average glucose level for HbA1c estimation.")

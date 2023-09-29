import streamlit as st
# import pyautogui

# def pdf_parsing():
with st.form("login", clear_on_submit=True):
    pdf_url = st.text_input('PDF File URL', 'Paste the URL here.')

    option = st.selectbox(
        'Which python library would you like to choose for pdf parsing?',
        ('PyPDF', 'Nougat'))

    is_submit = st.form_submit_button("Submit", type="primary")
    if is_submit:
        st.write(f'You selected {pdf_url} file and {option} library for pdf parsing')

        if option == 'Nougat':
            st.write('Nougat')

        # mmd_file_path = "C:/Users/naman/Downloads/NamanGupta_Resume.mmd"

            # with open(mmd_file_path, "r", encoding="utf-8") as mmd_file:
            #     mmd_content = mmd_file.read()
            #     st.title("Hello from Streamlit!")
            #     st.markdown(mmd_content)
        elif option == 'PyPDF':
            st.write('PyPDF')
            
# if st.button("Submit", type="primary"):
#     st.write(f'You selected {pdf_url} file and {option} library for pdf parsing')

# if st.button("Reset", type="secondary"):
#     pyautogui.hotkey("ctrl","F5")


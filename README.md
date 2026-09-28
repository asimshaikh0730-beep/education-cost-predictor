# International Education Cost Predictor

This project is a machine learning web app that estimates the total cost of studying abroad. The user selects a country, city, university, program and level, then enters the duration, living cost index, visa fee and insurance cost. The app instantly shows the estimated total cost.

Live Demo: https://education-cost-predictor-eym8mvyna6ti3tdt4sfdci.streamlit.app

How it works

First, the dataset is cleaned and the text columns (country, city, university, program and level) are converted into numbers. Then a Random Forest Regressor model is trained on this data to predict the total cost. The trained model is saved as a pickle file and used inside a Streamlit web app, so anyone can try it in the browser.

Tools used

Python, Pandas, NumPy, scikit-learn, Matplotlib, Seaborn and Streamlit.

Files in this project

app.py - the Streamlit web app
model.pkl - the trained model
International_Education_Costs.csv - the dataset
requirements.txt - the list of libraries needed

How to run it on your computer

-Install the libraries with: pip install -r requirements.txt
-Then start the app with: streamlit run app.py

Author

Mohammad Asim
GitHub: https://github.com/asimshaikh0730-beep
LinkedIn: https://linkedin.com/in/asim-mohammad-0a033a345

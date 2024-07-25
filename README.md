# chatbot
A Streamlit app for interacting with a chatbot powered by OpenAI's language model and SentenceTransformers. Features include caching for frequent questions and dynamic responses from the language model. Easy to deploy and use locally or on Streamlit Cloud.
Streamlit Chatbot App
This repository contains a Streamlit application that enables users to interact with a chatbot. The chatbot is powered by OpenAI’s language model and SentenceTransformers for handling user inputs and responses. It also uses a simple caching mechanism for frequently asked questions.

**Features**
Chat Interface: Users can send messages and receive responses from the chatbot.
Caching: Frequently asked questions are pre-cached for quick responses.
Language Model Integration: Uses OpenAI’s language model via LangChain for generating responses to less common queries.
Installation
To run this application locally, follow these steps:

**Clone the Repository:**
git clone https://github.com/yourusername/streamlit-chatbot-app.git
cd streamlit-chatbot-app
Create a Virtual Environment (optional but recommended):
python -m venv venv source venv/bin/activate # On Windows use venv\Scripts\activate

Install Dependencies:
pip install -r requirements.txt

Run the Application:
streamlit run app.py

Access the Application:
Open your web browser and navigate to http://localhost:8501 to interact with the chatbot.

**Deployment**
To deploy this application on Streamlit Community Cloud:

Push Your Code to GitHub: Ensure your code is pushed to a GitHub repository.

Create a New App on Streamlit Community Cloud:

Go to Streamlit Community Cloud. Connect your GitHub account. Select the repository and the file path (app.py).

Deploy the App:
Click Deploy and wait for the deployment process to complete. Usage Once the application is running, you can:

Enter a message in the text input field and click Send to receive a response from the chatbot. Click Clear to reset the chat history.

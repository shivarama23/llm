from fastapi import FastAPI
from fastapi.responses import RedirectResponse

app = FastAPI()

streamlit_app_url = "https://your-streamlit-app-url.com"  # Replace with your Streamlit app URL

@app.get("/redirect_to_streamlit")
def redirect_to_streamlit():
    return RedirectResponse(url=streamlit_app_url)

import uvicorn
"""Starts the backend"""
if __name__ == "__main__":
    uvicorn.run("backend.backend:app", host="127.0.0.1", port=8000, reload=True)
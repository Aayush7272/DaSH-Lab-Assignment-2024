import json # To convert Python Objects into JSON format
import requests # To send HTTP requests in Python
import time # To handle time related task


# API endpoint and API key from environment variable
api_endpoint = "https://api.openai.com/v1/chat/completions"
api_key = ("YOUR_API_KEY_HERE")

# prompts and parameters
prompts = [
    "What is operating System?",
    "What is the OSI model",
    "Who was Alan Turing",
    "How do computer networks work?",
    "What is linux kernel",
    "what is a file system?",
    "What is docker?",
    "What is GPU and how is it diffrent from a CPU?",
    "What are the layers of the OSI model?",
    "What is BeeGFS?",
    "What are the various components that comprise a computer?",
    "What is federated learning?"
 
]

# parameters for the API call
parameters = {
    "model": "gpt-3.5-turbo",
    "max_tokens": 2048, # Maximun number of tokens
    "temperature": 0.5, # Controls the randomness of the response
    "top_p": 1, # Parameter limits the sampling of top p probablity mass (1 means no restrictions)
    "frequncy_penalty": 2 # Discorages model from repeating tokens
    
}

output = []
for prompt in prompts: #loops the iterates over each prompt
   
    headers = {
        "Authorization": f"Bearer {api_key}", #Contains API key 
        "Content-Type": "application/json" # Request body in JSON format
    }
    data = { # Dictonary
        "model": parameters["model"],
        "messages": [{"role": "user", "content": prompt}], 
        "max_tokens": parameters["max_tokens"],
        "temperature": parameters["temperature"],
        "top_p": parameters["top_p"],
        "frequncy_penalty": parameters["frequncy_penalty"]
    }
    
    time_sent = int(time.time()) # Captures the current time before sending requests
    
    try:
        # Send request to API
        response = requests.post(api_endpoint, headers=headers, json=data)
        response.raise_for_status()  # Raise an error for HTTP error responses
        response_data = response.json()
        response_text = response_data["choices"][0]["message"]["content"] # Extract the text of the response from the API
    except requests.exceptions.RequestException as e:
        response_text = f"Error: {e}"

    time_recvd = int(time.time()) # Captures the current time immediately after sending the requests

    # Create output object
    output_object = {
        "Prompt": prompt,
        "Message": response_text,
        "TimeSent": time_sent,
        "TimeRecvd": time_recvd,
        "Source": "ChatGPT"
    }
    output.append(output_object) #Adds the output_object to the output list
    
    # Add delay between requests to avoid rate limits 
    time.sleep(10)

# Write output to file
with open('output.json', 'w') as f:
    json.dump(output, f, indent=4)

print("Output written to output.json")
# This code was made with "help" of Genrative AI
# The error 429 (ChatGPT) and Max retries exceeded (Gemma) of this code was unable to be fixed after adding delay.
# :)
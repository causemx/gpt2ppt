filename = "/content/drive/MyDrive/Colab Notebooks/minutes/data/Round_22_Online_Kickoff_Meeting.txt"

prompt_response = []
tokenizer = AutoTokenizer.from_pretrained("gpt2")
chunks = break_up_file_to_chunks(filename)

for i, chunk in enumerate(chunks):

    prompt_request = "Summarize this meeting transcript: " + tokenizer.decode(chunks[i])
    messages = [{"role": "system", "content": "This is text summarization."}]    
    messages.append({"role": "user", "content": prompt_request})

    response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
            temperature=.5,
            max_tokens=500,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
    )
    
    prompt_response.append(response["choices"][0]["message"]['content'].strip())
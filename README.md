# gpt2ppt
Auto generating pptx from gpt3+

## Requirement
1. Python version > 3.6
2. [OpenAI key](https://platform.openai.com/account/api-keys)
3. discord.py
4. python-dotenv
5. pyautogui

## Install
1. Install Selenium: `pip3 install -r requirements.txt`
2. Modify extension.py and enter correct api_key

## Generator
### Usage
```
positional arguments:
    options: [input_file]   path/to/input_file, format:[question, topic]
    
optional arguments:
    -o, --output_file       destination for output pptx

```


### Example
```
python example.py input.json
python example.py input.json -o output.pptx
```

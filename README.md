# gpt2ppt
Auto generating pptx from gpt3+

## Requirement
1. Python version > 3.6
2. [OpenAI key](https://platform.openai.com/account/api-keys)

## Install
1. Make sure you have Chrome browser installed.
1. Install Selenium: `pip3 install -r requirements.txt`

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
python example.py input.txt
python example.py input.txt -o output.pptx
```

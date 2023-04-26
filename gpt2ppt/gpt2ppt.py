import os
import openai
import requests 
import json
import gpt2ppt.extension as extension
from pptx import Presentation as pt

openai.api_key = extension.OPENAI_API_KEY

MODEL_ENGINE = "gpt-3.5-turbo"


class GenerationError(Exception):
    def __init__(self, f, *args):
        super().__init__(args)
        self.f = f

    def __str__(self):
        return 'There are something wrong when generating'

class Slide:
    _instance = None
    SLD_LAYOUT_TITLE_AND_CONTENT = 1

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self, input=None, output=None) -> None:
        self.prs = pt()
        self.slide = []
        self.entry = []
    
    def add(self, title, prompt):
        slide = self.prs.slides.add_slide(
            self.prs.slide_layouts[self.SLD_LAYOUT_TITLE_AND_CONTENT])
        shapes = slide.shapes

        title_shape = shapes.title
        body_shape = shapes.placeholders[1]
        title_shape.text = title
        tf = body_shape.text_frame
        
        if isinstance(prompt, list):
            for p in prompt:
                self.add_para(tf, p)
        else:
            self.add_para(tf, p)
    
    def add_para(self, tf, content, level=1):
        p = tf.add_paragraph()
        p.text = content
        p.level = level

    def save(self):
        self.prs.save('output.pptx')

        

def add_slide(prs, layout, title, content):
    """Return slide newly added to `prs` using `layout` and having `title`."""
    slide = prs.slides.add_slide(layout)
    slide.shapes.title.text = title
    body_shape = slide.shapes.placeholders[1]
    tf = body_shape.text_frame
    tf.text = content
    return slide

def generate(args):
    prs = pt()
    input_file = args.input_file
    output_file = args.output_file
    output = "./output.pptx" if not output_file else output_file

    try:
        with open(input_file) as topo_file:
            for line in topo_file:
                print(line)
    except FileNotFoundError as fe:
        print("error:", str(fe))
        return 1
    return 0

def foo(input):
    response = openai.ChatCompletion.create(
        model=MODEL_ENGINE, 
        messages=[{"role": "user", "content": input }])   
    return response['choices'][0]['message']['content']
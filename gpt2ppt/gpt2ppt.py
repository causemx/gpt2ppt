import openai
import json
from gpt2ppt import extension
from gpt2ppt.utils import IterWrapper
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
    
    def add(self, title, prompts):
        slide = self.prs.slides.add_slide(
            self.prs.slide_layouts[self.SLD_LAYOUT_TITLE_AND_CONTENT])
        shapes = slide.shapes

        title_shape = shapes.title
        body_shape = shapes.placeholders[1]
        title_shape.text = title
        text_frame = body_shape.text_frame
        text_frame.clear()
        
        if isinstance(prompts, dict):
            for topic, prompt in prompts.items():
                p = text_frame.add_paragraph()
                res = gen(prompt)
                p.text = f"{topic}, {res}"
        else:
            print('Prompt must contain at least one topic')
            pass
    
    def add_para(self, tf, content, level=1):
        p = tf.add_paragraph()
        p.text = content
        p.level = level

    def save(self):
        self.prs.save('output.pptx')

def generate(args):
    try:
        with open(args.input_file) as topo_file:
            slide = Slide() 
            doc = json.load(topo_file)
            iter_doc = IterWrapper(doc)
            while iter_doc.hasnext():
                key = next(iter_doc)
                if key.startswith("page"):  # ignore _comment token
                    slide.add(doc[key]["title"], doc[key]["prompts"])
            slide.save()
 
    except FileNotFoundError as fe:
        print("error:", str(fe))
        return 1
    return 0

def gen(prompts):
    for prompt in prompts:
        response = openai.ChatCompletion.create(
            model=MODEL_ENGINE, 
            messages=[{"role": "user", "content": prompt}])   
    return response['choices'][0]['message']['content']
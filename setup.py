from setuptools import find_packages, setup

setup(
    name='gpt2ppt',
    version='0.1.0',
    author='causemx',
    author_email='allen.cause@gmail.com',
    description='Auto generate PPTX from query to GPT3.5/ChatGPT',
    packages=['gpt2ppt'],
    package_dir={'gpt2ppt': 'src/gpt2ppt'},
    install_requires=[
        'openai',
        'python-pptx',
    ]
)

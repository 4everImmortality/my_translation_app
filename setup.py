from setuptools import setup, find_packages

setup(
    name='my_translation_app',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'tkinter',
        'pyperclip',
        'pdfplumber',
        'python-docx',
        'reportlab',
        'transformers',
        'torch',
        'langdetect',
        'pystray',
        'Pillow',
        'openai'
    ],
    entry_points={
        'console_scripts': [
            'my_translation_app = my_translation_app.trans:main',
        ],
    },
    author='Your Name',
    author_email='your.email@example.com',
    description='A local AI translation software',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/my_translation_app',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
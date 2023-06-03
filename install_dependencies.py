import subprocess

# List of required packages
packages = [
    'huggingface-hub',
    'scikit-learn',
    'scipy',
    'transformers>=4.6.0,<5.0.0',
    'sentence-transformers'
]

# Install packages
for package in packages:
    subprocess.check_call(['pip', 'install', package])

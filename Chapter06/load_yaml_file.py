#!/usr/bin/python
__author__ = "Bassim Aly"
__EMAIL__ = "basim.alyy@gmail.com"

import yaml
from pprint import pprint

with open(
        r'/media/bassim/DATA/GoogleDrive/Packt/EnterpriseAutomationProject/Chapter6_Configuration_generator_with_python_and_jinja2/yaml_example.yml',
        'r') as yaml_file:
    yaml_data = yaml.load(yaml_file)  # This is to read the file content

pprint(yaml_data)

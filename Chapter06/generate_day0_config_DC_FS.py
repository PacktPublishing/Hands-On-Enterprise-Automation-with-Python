#!/usr/bin/python
__author__ = "Bassim Aly"
__EMAIL__ = "basim.alyy@gmail.com"

import yaml
from jinja2 import FileSystemLoader, Environment

with open(
        '/media/bassim/DATA/GoogleDrive/Packt/EnterpriseAutomationProject/Chapter6_Configuration_generator_with_python_and_jinja2/network_dc.yml',
        'r') as yaml_file:
    yaml_data = yaml.load(yaml_file)

template_dir = "/media/bassim/DATA/GoogleDrive/Packt/EnterpriseAutomationProject/Chapter6_Configuration_generator_with_python_and_jinja2"

template_env = Environment(loader=FileSystemLoader(template_dir),
                           trim_blocks=True,
                           lstrip_blocks=True
                           )

for device, config in yaml_data['dc1'].iteritems():
    if config['device_template'] == "vIOSL2_Template":
        device_template = template_env.get_template("switch_day1_template.j2")
    elif config['device_template'] == "vIOSL3_Template":
        device_template = template_env.get_template("router_day1_template.j2")

    print("rendering now device {0}".format(device))
    Day0_device_config = device_template.render(config)

    print Day0_device_config
    print "=" * 30

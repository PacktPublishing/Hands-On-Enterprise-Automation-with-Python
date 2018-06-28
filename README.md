# Hands-On Enterprise Automation with Python

<a href="https://www.packtpub.com/networking-and-servers/hands-enterprise-automation-python?utm_source=github&utm_medium=repository&utm_campaign=9781788998512"><img src="https://dz13w8afd47il.cloudfront.net/sites/default/files/imagecache/ppv4_main_book_cover/B10179_MockupCover_New.png" alt="Hands-On Enterprise Automation with Python" height="256px" align="right"></a>

This is the code repository for [Hands-On Enterprise Automation with Python](https://www.packtpub.com/networking-and-servers/hands-enterprise-automation-python?utm_source=github&utm_medium=repository&utm_campaign=9781788998512), published by Packt.

**Automate common administrative and security tasks with Python**

## What is this book about?
Hands-On Enterprise Automation with Python starts by covering the set up of a Python environment to perform automation tasks, as well as the modules, libraries, and tools you will be using. 

This book covers the following exciting features: 
* Understand common automation modules used in Python
* Develop Python scripts to manage network devices
* Automate common Linux administration tasks with Ansible and Fabric
* Managing the Linux processes
* Administrate VMWare, Openstack, and AWS instances with Python

If you feel this book is for you, get your [copy](https://www.amazon.com/dp/1788998510) today!

<a href="https://www.packtpub.com/?utm_source=github&utm_medium=banner&utm_campaign=GitHubBanner"><img src="https://raw.githubusercontent.com/PacktPublishing/GitHub/master/GitHub.png" 
alt="https://www.packtpub.com/" border="5" /></a>


## Instructions and Navigations
All of the code is organized into folders. For example, Chapter02.

The code will look like the following:
```
from netmiko import ConnectHandler
from devices import R1,SW1,SW2,SW3,SW4

nodes = [R1,SW1,SW2,SW3,SW4]

for device in nodes:
    net_connect = ConnectHandler(**device)
    output = net_connect.send_command("show run")
    print output
```

**Following is what you need for this book:**
Hands-On Enterprise Automation with Python is for system administrators and DevOps engineers who are looking for an alternative to major automation frameworks such as Puppet and Chef. Basic programming knowledge with Python and Linux shell scripting is necessary.

With the following software and hardware list you can run all code files present in the book (Chapter 1-18).

### Software and Hardware List

| Chapter  | Software required                   | OS required                        |
| -------- | ------------------------------------| -----------------------------------|
| All      | Python (2.x, 3.x), Ansible, EVE-NG  | Windows, Linux (Ubuntu)            |
| All      | Linux                               | Windows, Linux (Ubuntu)            |


We also provide a PDF file that has color images of the screenshots/diagrams used in this book. [Click here to download it](http:/​/​www.​packtpub.​com/​sites/​default/​files/
downloads/​HandsOnEnterpriseAutomationwithPython_​ColorImages.​pdf).

### Related products <Paste books from the Other books you may enjoy section>
* Mastering Python Networking [[Packt]](https://www.packtpub.com/networking-and-servers/mastering-python-networking?utm_source=github&utm_medium=repository&utm_campaign=9781784397005) [[Amazon]](https://www.amazon.com/dp/1784397008)

* Practical Network Automation [[Packt]](https://www.packtpub.com/networking-and-servers/practical-network-automation?utm_source=github&utm_medium=repository&utm_campaign=9781788299466) [[Amazon]](https://www.amazon.com/dp/1788299469)

## Get to Know the Author
**Bassem Aly**
Bassem Aly is an experienced SDN/NFV solution consultant at Juniper Networks and has been working in the Telco industry for last 9 years. He focused on designing and implementing next generation by leveraging different automation and devops frameworks. Also he has extensive experience in architecting and deploying telco applications over the openstack. Bassem also conducts corporate training on network automation & network programmability using python and ansible.

### Suggestions and Feedback
[Click here](https://docs.google.com/forms/d/e/1FAIpQLSdy7dATC6QmEL81FIUuymZ0Wy9vH1jHkvpY57OiMeKGqib_Ow/viewform) if you have any feedback or suggestions.

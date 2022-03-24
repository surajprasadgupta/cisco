# cisco
assignment for cisco

# Overview

Django REST framework is a powerful and flexible toolkit for building Web APIs.

Some reasons you might want to use REST framework:

* The [Web browsable API][sandbox] is a huge usability win for your developers.
* Authentication policies including optional packages for JWT .
* Serialization that supports both ORM and non-ORM data sources.
* Customizable all the way down - just use regular function-based views if you don't need the more powerful features.
* Extensive documentation, and great community support.

There is a live example API for testing purposes, [available here][sandbox].

**Below**: *Screenshot from the browsable API*

![Screenshot][image]

# Requirements

* Python (3.6, 3.7, 3.8, 3.9, 3.10)
* Django (2.2, 3.0, 3.1, 3.2, 4.0)

-----
# Installation
Step 1: download the project.

Step 2: create vertual environment for the project using command

*  python3 -m venv <env_name>

Step 3: activate the env using command

*  source/env_name/bin/activate

Step 4: go to the requairement.py file and Run

*  pip install -r requirements.txt (Python 2), or pip3 install -r requirements.txt (Python 3)

Step 5: Run command to start the server

*  python3 manage.py runserver 

# API Documentation

Step 1: Login API

![login](https://user-images.githubusercontent.com/40552569/160017357-57ba8dcf-7c96-4f44-94cd-0b58fc8910a8.png)

Step 2: List create routers

![create_router](https://user-images.githubusercontent.com/40552569/160017619-bd17aa91-9c9f-4a8b-b950-f00640a91584.png)

Step 3: Get List of routers

![get_routers](https://user-images.githubusercontent.com/40552569/160017762-76d0be88-15ba-41e8-8d27-0ed2e6ae2f9c.png)

Step 4: Router get by Id

![get_router_by_id](https://user-images.githubusercontent.com/40552569/160017870-78fe8209-d47c-493a-ac5c-aa8e884e4d5d.png)

Step 5: Router Update by Id

![update_by_id](https://user-images.githubusercontent.com/40552569/160017963-fbd2b140-f5b4-4183-967b-4d6eb05b074c.png)

Step 6: Router Delete by Id

![delete_by_id](https://user-images.githubusercontent.com/40552569/160018029-9f4205ee-35b0-4db9-a0a5-583549095966.png)





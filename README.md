# mobile-client-python
Client library for Glue's Mobile API

### Installation

Make sure you have a Python3 installation in your system.

After you create your virtualenv and source your environment, you can install the dependencies by running:

```
pip install -r requirements.txt
```

All required dependencies should now be ready so that you try out the sample app.

### Execute sample app

After you get your client_id from the Glue tech team, you will be able to run the below app to approve or reject the first available key approval request
```
python sample/app.py --username=<glue_user_phone> --password=<glue_user_pass> --client-id=<client_id>
```


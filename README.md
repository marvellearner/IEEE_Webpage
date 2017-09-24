# IEEE_Webpage
This is a one page website along with a registration form to save user's data

## Installation Guide
1.Get the source code on your machine via git

 ```shell
    git clone https://github.com/modestlearner/IEEE_Webpage.git
 ```
    
2.Create a python virtual environment and install python dependencies.

```shell
    cd sarthak_web
    virtualenv venv
    source venv/bin/activate  # run this command everytime before working on project
    pip install -r requirements.txt
```

3.Now go to the root directory where you'll see **manage.py** file


4.After going in the root directory type
 ```shell
    python manage.py migrate
    python manage.py runserver
 ```


5.That's it. Now you can run development server at [http://127.0.0.1:8000/] (for serving backend)

# Pitch

## Description
This is an application that enables a user to post pitches and view other users' pitches. A user can log in to the application using their credentials, post comments and leave remarks on other people's pitches.
### By Maurine Sinami

## Setup/Installation Requirements

### Prerequisites
* python3.7
* pip
* Virtual environment(virtualenv)
* Flask-Mail
* PostgreSQL

## Cloning and running
Clone the application using git clone(this copies the app onto your device). In your terminal:

  ```  $ git clone https://github.com/maurinesinami/pitch/```
  
  ```  $ cd pitch```

## Creating the virtual environment

  ```  $ python3.7 -m venv --without-pip virtual```
  
  ```  $ source virtual/bin/env```
  
  ```  $ curl https://bootstrap.pypa.io/get-pip.py | python```

## Installing Flask and other Modules

  ```  $ python3.6 -m pip install Flask```
  
  ```  $ python3.6 -m pip install Flask-Bootstrap```
  
  ```  $ python3.6 -m pip install Flask-Script```
  
  ```  $ python3.6 -m pip install Flask-Mail```


## Testing the Application
To run the tests for the class files:

  ```  $ python3.7 manage.py test```

## Technologies Used
* Python 3.7
* Flask

## Behaviour driven development/ Specifications
| Behaviour    | Input     | Output|
| :------------- | :------------- |:---------|
|   Post pitch     |     Pitch is saved in a database | Post from database|
|Comment on pitch|Leave a comment| Comment saved for display|

|Login and authenticate|Email address and password|Saved and used for authentication|


## Support and contact details
Feel free to reach out to the developer at:

* Mobile: 0714828944
* Email: maurine.sinami@gmail.com
## License
MIT License Copyright (c) {2019} Maurine Sinami
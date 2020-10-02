# PRGX Simple API

### This API was developed Using Django-Rest Framework
#### Funcitionalities:
* Compute a sum operation between to numbers, either using a body of a post request or the query string

#### Easy steps to run it:
* Get a computer with Linux Os
* Clone the repo, when in your machine, It doesn't matter the path
- git clone https://github.com/jalondono/PRGX
* Type on your console the next commands
- cd PRGX_Api
* Install the requirements on the requierements file,  either in your venv or not using this command
- pip install -r requirements.txt
* Once done this, just run it using the next command  "./manage.py runserver"      

#### Workin on it
* You can use your navigator or a software that allow you perform HTTP requests (I used Insomnia)
and enjoy it.

#### Available Urls
 * http://127.0.0.1:8000/api/v1/url/?num1=x&num2=x
 * http://127.0.0.1:8000/api/v1/body


#### Examples
* Post Request With body
<img align="center" src="https://i.ibb.co/NsMcD2x/body-post.png" height="50%" width="100%"/>

* Get Request
<img align="center" src="https://i.ibb.co/p03FfwV/get.png" height="50%" width="100%"/>

* POST REQUEST with Query string
<img align="center" src="https://i.ibb.co/99gs10T/URL-POST.png" height="50%" width="100%"/>

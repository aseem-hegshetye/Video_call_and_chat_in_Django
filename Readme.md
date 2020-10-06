

<h1>Video call and chat in Django</h1>
<div>
Using Django, Django-channels, js, js - websockets, Daphne ASGI server ( built specially for django channels),
redis server (installed locally using docker or on GCP using redis memory cache service)
</div>

<h4> Deploying this app on google app engine flex </h4>

* We dont use/need any sql db. This app has default sqlite db in settings.py.

* Clone this repository to your local machine. cd into this repo- `cd django_video/`

* create a python virtual env `python3.8 -m venv venv`

  * Install all dependencies required: `pip install -r requirements.txt`

* Create a GCP (google cloud platform lol) project.

* Deploy a test app on gcp app engine flex to get an idea - 
<a href='https://cloud.google.com/python/django/flexible-environment'> Link</a>

  *  You can ignore the cloud sql creation step as we dont need sql in our app.
  
  *  In settings.py update STATIC_URL with your gcp public bucket name that you created 
  when deploying test app to GAE flex

* Create a redis instance on default VPC network in same gcp project - 
<a href='https://cloud.google.com/memorystore/docs/redis/creating-managing-instances#creating_a_redis_instance_on_a_vpc_network'>Link </a>
  *  This Redis instance should be in same region as app engine flex.
   
  *  Perhaps every gcp project comes with a default VPC network, hence we choose default and dont have to create 
  another VPC.
  
  *  In app.yaml file update env variables - REDISHOST,REDISPORT from your redis instance.


<h4>You can run this project locally through your venv that you created above. I run it on Ubuntu. 
if you are using windows, god save you. </h4>

*  we will need a redis server locally: Hoping you have docker installed on your machine. 
if not then install it on your own.
  *  `docker run -p 6379:6379 -d redis:5`
  *  `daphne django_video.asgi:application`
  *  Once you are done using this app, you can stop the redis container:
  
     * `sudo systemctl restart docker.socket docker.service`
     
     * `docker ps` -- shows which containers are running
     
     * `docker rm <container id>` -- stop the container

<h4>Deploy your project to google app engine flex:</h4>

*  `gcloud app deploy` -- call this from root dir that contains app.yaml file.

* If this is your first time deploying app to GAE, you will be asked to select a region and app engine type.
  *  Pick the same region as your redis instance.
  *  Pick flexible app engine option
  
GAE Flex deployment takes lot of time compared to GAE standard deployment, but GAE standard doesnt support websockets
(which are required for peer to peer connections for video and chat functionality.)

Video calling doesnt work on localhost if your VPN is on.
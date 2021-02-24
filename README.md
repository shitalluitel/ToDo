### Table of Content

* [ToDo](#todo)
    * [REST API](#rest-api)
    * [TDD](#tdd)
    * [CI/CD](#cicd)
    * [Deployment](#deployment)    

## ToDo

This is an application build using django, django rest framework, and postgres as a database intended to replicate
trello as an implementation. This application helps us to keep track of all the task that we intended to do in future.

This application for me as a developer is intended to learn about software development process, REST API, TDD approach
as well as deployment process. I am willing to write everything that I learn on the process of developing to deployment.

### REST API

For this application I have used django rest framework. To learn more about RESTAPI, you may
visit [django rest framework](https://www.django-rest-framework.org/)

### TDD

Test first approach for writing codes is main objective of Test Driven Development. In this approach we write test cases
covering different scenarios and after writing those test cases we write codes to pass those test cases.

### CI/CD

This section will be carried latter

### Deployment

This section of documentation is based on a
[blog](https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-16-04)
posted by digitalocean.

I will be skipping basic of creating and setting up project.

#### Create a gunicorn systemd service file

Create and open a systemd service file for Gunicorn with sudo privileges in your text editor:

```shell
sudo nano /etc/systemd/system/gunicorn.service
```

Add following codes within the file.

```text
[Unit]
Description=gunicorn daemon
After=network.target

[Service]
User=sammy
Group=www-data
WorkingDirectory=/home/sammy/myproject
ExecStart=/home/sammy/myproject/myprojectenv/bin/gunicorn --access-logfile - --workers 3 --bind unix:/home/sammy/myproject/myproject.sock myproject.wsgi:application

[Install]
WantedBy=multi-user.target
```

With that, our systemd service file is complete. Save and close it now.

We can now start the Gunicorn service we created and enable it so that it starts at a boot:

```shell
sudo systemctl start gunicorn
sudo systemctl enable gunicorn
```

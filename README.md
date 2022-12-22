# UcoverAPI
This api will handle 3 types of users:
Client: person that want to buy.
Coverer: person that want to make a experience.
Admin: Person that have all the permissions of the app.

Configuration:
1. Clone repository
2. Create a virtual environment
3. Activate the virtual environment 
4. $ pip install -r requirements.txt
5. modify settings.py DATABASES={} to a correct database that you have
6. Make migrations
7. Create super user in django
8. Run server

Folder distribution: 
ucover_backend_api
(main)
--ucover_backend_api
(apps)
--payments
--services
--users

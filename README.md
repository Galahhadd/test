Howdy

I did not manage to finish all assignments

How to launch:
1. Download this repo or use git clone 

2. Start docker on your local machine and use "docker-compose up -d" Then type "docker-compose exec web python manage.py migrate" (all within folder where project is located)

3. Start making API calls
   Available endpoints:
   1) http://127.0.0.1:8000/api/v1/cat/create/ - allows to create cats
   2) http://127.0.0.1:8000/api/v1/cats/ - retrieve all cats
   3) http://127.0.0.1:8000/api/v1/cat/<pk> - retrieve a single cat, update it, delete it (<pk> refers to cat id inside db)
   4) http://127.0.0.1:8000/api/v1/mission/create/ - create a single missions and 1-3 targets to it
   5) http://127.0.0.1:8000/api/v1/missions/ - retrieve all missions and related targets
   6) http://127.0.0.1:8000/api/v1/mission/<pk> - retrieve a single mission and related targets, also can assign a cat to mission (<pk> refers to mission id inside db)
   7) http://127.0.0.1:8000/api/v1/target/<pk> - retrieve a single target to update it (<pk> refers to target id inside db)

   

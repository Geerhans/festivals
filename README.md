# ShareFestival

ShareFestival features an festival guide for everything you need to know about an exiciting festival in different countries. It is a 
platform to expose our users to different festivals around the world and to share their thoughts and experiences. A way to celebrate our 
experiences together.
Beginning with a list of countries to choose from, the website navigates you to the interesting history of the fetsival, 
then an opportunity to share your experience.

How to run the project:

1. Clone the file 
        
        git clone https://github.com/Geerhans/festivals.git

2. Change directory 
        
        cd festivals

3. Create Virtual Environment 
        
        conda create -n festival python=3.7.5

4. Activate the environment
        
        conda activate festival

5. Install dependencies 
        
        pip install -r requirements.txt

6. Configure and pre-populate the application 
 
        python manage.py makemigrations festival
        
        python manage.py migrate
        
        python population_script.py

7. Start the application 
        
        python manage.py runserver

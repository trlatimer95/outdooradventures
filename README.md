# Readme File for Catalog App - Outdoor Adventures

## PURPOSE:
The purpose of this project was to tie together everything learned in the Back-End portion of the Udacity Full-Stack Web Developer Nanodegree. The intent was to create an application that replicated an online catalog. The application had to display catalog, category, and item pages. The catalog page was expected to show a list of categories as well as a list or recent items. The category page was expected to show a list of items within a specific category. The item page was expected to show information on a specific item. The application also required the ability for users to sign in/out and for users to be able to create, edit, and delete items given that they had the proper permissions, e.i. they created the item in the first place. Udacity provided none of the code for this project and it was expected that I complete all of it alone using resources provided to me throughout the class.

## REQUIRED PROGRAMS/LIBRARIES:
 1. Python
 2. Vagrant
 3. VirtualMachine
 4. Flask
 5. SQLAlchemy
 6. database_setup
 7. oauth2client.client
 8. httplib2
 9. json
 10. requests
 
## DIRECTORIES AND FILES INCLUDED/NEEDED:
 - Catalog
    - static
        - formStyles.css
        - styles.css
    - templates
        - addItem.html
        - catalog.html
        - category.html
        - deleteItem.html
        - editItem.html
        - item.html
        - login.html
        - publicCatalog.html
        - publicCategory.html
        - publicItem.html
    - application.py
    - client_secrets.py
    - clientInfo.py
    - database_setup.py
    - fb_client_secrets.py
    - lotsofitems.py
    - README
    - Vagrantfile

## TO START PROGRAM:
 1. Download project files and unzip them into a directory
 2. From a Linux-like terminal (ex. Git Bash, Mac Terminal, etc), cd to the directory where you store the repository
 3. Ensure that the directory contains all of the proper files and directories (View Directories/Files Included section)
 4. Start vagrant by typing vagrant up and hitting enter
 - It may be necessary to type vagrant init first to create an init file
 - Wait for vagrant up to complete 
 5. Type vagrant ssh
 - No login information should be required and VM should load
 - Wait for vagrant ssh to complete (Should see some text saying "cd /vagrant to view shared directories")
 6. cd into /vagrant and then to the directory you stored the files in
 7. Run python database_setup.py to create database structure
 8. Run python lotsofitems.py to populate the database
 9. Run python application.py to launch the program
 - The console will advise when teh program has launched on localhost:8000
 10. Open a browser and enter localhost:8000 or localhost:8000/catalog into the url
 11. The first page will be the catalog page and will display a list of categories as well as recent items
 12. Click login to login to the application in order to add, edit, and delete items 
 - You can only edit/delete items you created
 - NOTE: Google sign in requires Google+ to work properly
 13. When you are finished with the application, type Ctrl C in the terminal to exit
 14. Type exit to exit vagrant and exit again to exit the terminal
 
## TO VIEW JSON API:
 1. Ensure that the program is running and open in your web broswer
 - Follow the To Start Program steps above if it is not running
 2. Append either of the below routes to the end of 'http://localhost:8000' to view the JSON API
    - '/catalog/JSON' - Displays JSON information regarding the various categories within the Catalog application
    - '/catalog/items/JSON - Displays JSON information of each item within the catalog

## DATABASE STRUCTURE
The database involved in this program is a mock SQLAlchemy database of a fictional Outdoor Adventures catalog. The catalog shows categories of various outdoor activities and displays information about items that would be used in each category.

The database contains the following structures:
 - User - Information obtained through Google+ or Facebook Sign-in
    - name
    - email
    - picture
    - id
    
 - Category
    - name
    - id

 - Item
    - name
    - id
    - image
    - description
    - category_id
    - category(Relationship)
    - user_id
    - user(Relationship)

## BUG REPORTING
Please report any issues and bugs to me at trlatimer95@gmail.com. Please ensure to include a complete description of the issue you are experiencing and steps to recreate the issue. Thank you!
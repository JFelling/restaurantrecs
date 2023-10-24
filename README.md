OVERVIEW
The Restaurant Recs project was designed to fulfil the requirements of Codecademy's CS 102: Data Structures, Algorithms, Trees, & Graphs portfolio project: Creating Recommendation Software. The project asked students to "research, brainstorm, and build a basic recommendation program for a topic of your choice." Specifically, the instructions included:
  1. Store data in a data structure
  2. Use an algorithm to sort or search for data within a data structure
  3. Use Git version control
  4. Use the command line and file navigation

For this project, I decided to create a restaurant recommendation software, as suggested by Codecademy. The software allows users to input a choice of cuisine type, and provides the user with a list of restaurants that match that cuisine. The list also includes contact information, price range, and average raiting for each restaurant.

INSTRUCTIONS FOR USE
The program is written in Python, and was created using Vistual Studio (VS) Code. In it's current itteration, the program can only be run in a terminal, using either a code editor or command prompt. 

To run the program, download RestaurantRecs.py, linkedlist.py, node.py, and restaurantData.py. Open in a code editor or command prompt to use. 

EXPLANATION OF CODE
The RestaurantRecs.py file initializes by importing the linkedlist class and restaurant data. The linkedlist class in turn imports the node class. The restaurant data data set includes a list of restaurant types, and a list of restaurants, including type, name, price range, rating, and address for each restaurant. The data set was provided by Codecademy. The code then includes a welcome graphic, and definitions for functions to insert restaurant types into a linked list, and the restaurants with their information into a linked list of linked lists. After the functions are defined, the rest of the code sets up print statements and options for user input to select a cuisine and see a list of relevant restaurants, including edge cases for cuisines not included in the data set. The code ends by allowing the user to restart or end the program. 

AREAS FOR FURTHER DEVELOPMENT
As this project was a basic terminal game, there are a number of areas for further development outside the scope of the original project. These areas include:
  1. User interface and expereince, including on a web and/or app platform.
  2. Expanded restaurant lists.
  3. Functionality to allow users to add new restaurant information and reviews.
  4. Further filters for restaurants (for example, by price range).
  7. User logins and profiles, which could include the ability to maintin a history of restaurants visited, track submitted reviews, and share photos from restaurants.

ACKNOWLEDGEMENTS
Thank you to my dad for help troubleshooting!

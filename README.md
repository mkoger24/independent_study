# An Integrated Library System that Focuses on Collaboration: Bringing Books and Computers Together

## Presented in Partial Fulfillment of the Requirements for the Degree Bachelor of Arts in Computer Science in the Department of Mathematical and Computational Sciences at The College of Wooster

### Mae Koger

This software aims to create an Integrated Library System (ILS) for the use of searching, surfing, and collaborating on literature materials in an academic setting, allowing users to interact with one another. This encourages academic conversation about papers, articles, and books stored in the ILS. This software is intended for use in an academic library for collaboration among students and faculty. See ```2024_koger_mae.pdf``` for more information about this project and the research I conducted in the process.
#### Environment Setup

To get started, create a virtual environment by using the command ```python -m venv venv```. The virtual environment can be activated with the command ```source myvenv/bin/activate``` and terminated with ```deactivate```.

Once the virtual environment is activated, use the command ```pip install -r requirements.txt``` to install the correct packages for use in running this program. To run the program, use the command ```python3 app.py``` or ```flask run``` and navigate to <localhost:5000/>.

#### SQL Database

To create the database used for this application in SQL, run the script ```books.sql```. This will create the tables used in the site: **books**, **comments**, and **tags**.

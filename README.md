# CS-340-Portfolio
SNHU CS 340 Client/Server Development Portfolio

Project Overview

For this project, I developed an interactive dashboard for Grazioso Salvare, an organization that identifies dogs for search-and-rescue training. Using MongoDB, Python, and Dash, I created a dashboard that allows users to filter animal shelter records and view the results through a data table, pie chart, and geolocation map.

Writing Maintainable and Adaptable Programs

I learned that writing maintainable programs means keeping code organized, readable, and easy to update. In Project One, I created a CRUD Python module to handle database operations. I was able to reuse that same module in Project Two to connect my dashboard to MongoDB.

Keeping the database functions separate from the dashboard made the project easier to manage and troubleshoot. In the future, I could reuse this module in other applications that need to store, retrieve, or update information in MongoDB.

My Approach to Problem Solving

When working on this project, I started by reviewing the requirements and breaking them into smaller tasks. I first connected the database, then worked on the data table, filtering options, and charts.

This project was different from some of my previous assignments because I had to make several components work together. I encountered issues with the geolocation map and pie chart, but I worked through them by reviewing the code, making adjustments, and testing the results.

In future projects, I plan to continue breaking problems into smaller steps and testing each part before moving forward.

The Importance of Computer Science

Computer scientists develop solutions that help people and organizations use technology more effectively. This can include creating applications, managing databases, and finding ways to make information easier to access.

My work on the Grazioso Salvare dashboard demonstrates how technology can help an organization make better use of its data. Instead of searching through thousands of animal records manually, users can filter the information and identify dogs that meet specific rescue-training requirements.

This project helped me see how computer science can be used to solve real-world problems and support better decision-making.

Project Files

ProjectTwoDashboard.ipynb — Interactive dashboard source code

CRUD_Python_Module.py — MongoDB CRUD operations

Grazioso Salvare Logo.png — Dashboard logo

CS 340 Project Two Christina Frediani.docx — Project documentation and testing screenshots

Running the Project

The dashboard requires Python, MongoDB, and the Austin Animal Center Outcomes dataset. The required Python libraries include Dash, JupyterDash, PyMongo, Pandas, Plotly, and Dash Leaflet.

To run the dashboard, configure valid MongoDB credentials, open ProjectTwoDashboard.ipynb in Jupyter Lab, and execute the notebook. The dashboard will provide a link to open the application in a browser.

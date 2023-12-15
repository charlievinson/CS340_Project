# CS340_Project

The purpose of this project is to create an interactive and user-friendly dashboard for Grazioso Salvare’s animal database. The dashboard utilizes a reusable Python module that implements CRUD functionality to retrieve individual animals from the database based on user-selected filtering options, then displays charts to visually communicate specific information related to each animal’s breed and location.

This dashboard provides a way for those working with the animal database to easily obtain and view information and statistics associated with it, and offers employees without technical training general access to the database that they may not have otherwise. While this dashboard only implements ‘R’ functionality (to ‘Read’ from the database), the Python module that facilitates dashboard-database connectivity allows for authorized users to create, update, and delete documents, as well. Future versions of this dashboard may contain these functions without updating the Python module.

This dashboard requires users to be authenticated and includes hard-coded values for login and server information. When the server is running, users simply navigate to the specified host and select one of the simple options provided to filter database results and view charts. The dashboard is designed to initially display all animals in the database formatted as a table containing all animal information. Users can then select filtering options to update the animals that appear in the table. Alternatively, users can select individual animals to view specific information related to their breed and location, formatted as a pie chart and geolocation chart, respectively.

Pymongo documentation: https://pymongo.readthedocs.io/en/stable/.
Dash documentation: https://dash.plotly.com/.

While the dashboard currently displays accurate breed and location information for each individual animal that is selected by the user, further development must be completed before the dashboard’s filtering options will correctly update the table with filtered results.

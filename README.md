
Airbnb Clone Project
Description
This project is an attempt to create a simplified version of Airbnb, a popular online marketplace for lodging and travel experiences. The goal is to replicate some of the core features of Airbnb to provide users with a familiar and functional platform for finding and booking accommodations.

Command Interpreter
The command interpreter serves as the main interface for users to interact with the Airbnb clone. It allows users to perform various actions, such as searching for listings, making reservations, and managing their bookings.

Getting Started
To start the Airbnb clone, follow these steps :

Clone the repository to your local machine.
Navigate to the project directory.
Run the command interpreter executable.
bash
Copy code
$ git clone https://github.com/mohamed-amine-ayari/airbnb-clone.git
$ cd airbnb-clone
$ ./interpreter
Usage
Once the interpreter is running, you can enter commands to explore and interact with the Airbnb clone. Here are some example commands:

search location dates: Find available listings in a specific location for given dates.
book listing_id dates: Reserve a listing for a specified duration.
list_listings: Display all available listings.
Examples
Searching for Listings
bash
Copy code
$ search Paris 2023-12-01 to 2023-12-10
Booking a Listing
bash
Copy code
$ book 1234 2023-12-01 to 2023-12-10
Listing Available Listings
bash
Copy code
$ list_listings
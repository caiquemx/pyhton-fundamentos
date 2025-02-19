# Contact Management System

## Overview

This is a simple command-line Contact Management System written in Python. It allows users to manage their contacts by adding, editing, deleting, and marking favorites. The system operates via a text-based menu.

## Features

- **View Contacts**: List all saved contacts.
- **Favorite Contacts**: View only the contacts marked as favorites.
- **Add Contact**: Register a new contact with name, telephone, email, and favorite status.
- **Edit Contact**: Update an existing contact's details.
- **Delete Contact**: Remove a contact from the system.
- **Toggle Favorite**: Mark or unmark a contact as a favorite.

## Installation

To run the project, follow these steps:

1. Clone the repository:
   ```sh
   git clone git@github.com:caiquemx/pyhton-fundamentos.git
   ```
2. Navigate to the project directory:
   ```sh
   cd contact-management
   ```
3. Run the main script:
   ```sh
   python main.py
   ```

## Usage

Once the program starts, a menu will appear with different options. Enter the corresponding number to perform an action:

```
-------------------------------------
---------------AGENDA----------------
-------------------------------------
Select an option:
1 - View Contacts
2 - View Favorite Contacts
3 - Add Contact
4 - Edit Contact
5 - Delete Contact
6 - Toggle Favorite
7 - Exit
```

## Code Structure

The project is divided into two main files:

1. **`main.py`**: Handles user interaction, menu navigation, and calling appropriate functions.
2. **`functions.py`**: Contains functions for managing contact operations.

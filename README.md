## Task Management System

The Task Management System is a web application designed to help users efficiently manage tasks. It provides various features, including user authentication, task creation, assignment, tracking, commenting, and updating.





## Table of contents

1. Introduction
2. Features
3. Usage


## Introduction

The Task Management System is built using Python,Django a high-level Python web framework and frontend Technologies like HTML,CSS,Javascript and the database used is Mysql. It offers a user-friendly interface for managing tasks effectively, suitable for personal or team use.
## Features

### Homepage

* Summary: Displays an overview of the task management system.
* Navigation: Provides links to login, registration, and task management pages.

### Login

* Authentication: Allows registered users to log in securely.
* Access Control: Restricts access to authenticated users only.

### Registration

* Account Creation: Enables new users to register for an account.
* Form Validation: Validates user inputs to ensure data integrity.

### Task Management Page

* Task Listing: Displays a list of tasks with relevant details.
* CRUD Operations: Supports creating, reading, updating, and deleting tasks.
* Assignment: Allows assigning tasks to specific users.
* Status Tracking: Tracks the status of tasks (e.g., incomplete, complete).
* Priority Management: Provides options to set task priorities (e.g., high, medium, low).
* Due Date Tracking: Enables setting and tracking due dates for tasks.
* Search and Filter: Facilitates searching and filtering tasks based on various criteria.

### Update Page

* Task Modification: Allows users to update task details, mark tasks as complete, or delete tasks.
* Confirmation: Prompts users for confirmation before performing update or delete operations.
* Permissions : The users who assigned the task has the permission to update or modify the task.

### Comment system
* Discussion: Provides a platform for users to discuss tasks by adding comments.
* Collaboration: Enables collaboration and communication among users regarding task details.


### Data Persistance

* The Application uses a RDBMS MYsql for maintaining and storing Data.

### Email Notifications 

* The Application sends email notifications whenever user is assigned a task or creates an account.

### Usage

* Visit the homepage and navigate to the login or registration page to access the task management features.
* Log in with your credentials or register for a new account if you don't have one.
* Once logged in, you can create, view, update, and delete tasks as needed.
* Use the comment page to discuss task details and collaborate with other users.

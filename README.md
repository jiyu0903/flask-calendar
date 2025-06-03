# Calendar Event Manager with Flask and FullCalendar

## Overview

This project is a web-based calendar application built with Flask (Python) on the backend and FullCalendar (JavaScript) on the frontend. It allows users to **create**, **read**, **update**, and **delete** calendar events dynamically, with each event containing a **title**, **start date/time**, **end date/time**, and **description**.

## Features and Changes Made

### Backend (Flask)

- **Database Integration with SQLAlchemy**  
  Events are stored in a SQLite database using SQLAlchemy ORM, enabling persistent data storage.

- **Event Model**  
  Added an `Event` model with fields for `id`, `title`, `start`, `end`, and `description`.

- **RESTful API Endpoints**  
  Created full CRUD API endpoints:
  - `GET /data` - Retrieve all events for the calendar display.
  - `POST /api/events` - Add a new event.
  - `GET /api/events/<id>` - Retrieve a single event's details.
  - `PUT /api/events/<id>` - Update an event.
  - `DELETE /api/events/<id>` - Delete an event.

- **Automatic Database Table Creation**  
  Database tables are created automatically before handling the first request.

### Frontend (json.html)

- **Dynamic Calendar with FullCalendar**  
  Uses FullCalendar JS library to render a modern calendar interface.

- **Event Display with Description Tooltip**  
  Events show their description in a tooltip when hovered.

- **Add Events via Date Range Selection**  
  Users can click and drag on calendar dates to add new events with a popup prompt for the title and description.

- **Delete Events via Click**  
  Clicking an event prompts for deletion confirmation and deletes the event on acceptance.

- **AJAX Integration for CRUD**  
  FullCalendar communicates with the backend REST API using AJAX for smooth, asynchronous user experience without page reloads.

- **Real-Time Calendar Updates**  
  After any event operation (create/delete), the calendar reloads events to reflect changes instantly.

## Benefits of Using REST API and CRUD Architecture

- **Separation of Concerns**  
  The backend focuses on data management and business logic, while the frontend handles user interaction and display.

- **Scalability and Extensibility**  
  REST API endpoints can be consumed by other clients (mobile apps, other web apps) beyond this frontend.

- **Stateless Communication**  
  Each REST request contains all necessary information, allowing the server to remain stateless and scalable.

- **Improved User Experience**  
  AJAX-based CRUD operations enable instant, asynchronous updates without page reloads, resulting in a smooth and responsive UI.

- **Data Integrity and Validation**  
  CRUD endpoints allow structured data validation and consistent updates to the database.

- **Maintainability**  
  Clear API routes and standardized operations make the code easier to maintain and extend.



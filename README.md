# **Renters Hub**

Renters Hub is a web application designed to assist users in finding and listing properties for rent. The platform allows property owners to post listings with images, descriptions, and rental prices, while potential tenants can search, filter, and inquire about properties.

## **Table of Contents**
1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Installation](#installation)
4. [Technologies Used](#technologies-used)
5. [Usage](#usage)
6. [Development Roadmap](#development-roadmap)
7. [Contributing](#contributing)
8. [License](#license)

## **Project Overview**

Renters Hub aims to simplify the property rental process by providing a user-friendly platform where property owners and renters can interact. Users can list properties with detailed descriptions and images, browse listings, and engage in real-time chat for inquiries.

**Author**: Edward Kataika 
**Project Status**: Ongoing

## **Features**

- User Registration and Authentication
- Role Management (Property Owners, Renters and Property Agents)
- Property Listing and Management
- Image Upload for Listings
- Property Search and Filter by Location, Price, Bedrooms, etc.(in progress)
- Property Availability (Occupied/Vacant)
- Real-time Messaging Between Users (In Progress)
- Responsive Design (Mobile and Desktop)
- Google Maps API Integration for Property Location (In Progress)

## **Installation**

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/rentershub.git
    cd rentershub
    ```

2. **Create a virtual environment**:
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows: env\Scripts\activate
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up the database**:
    Ensure you have PostgreSQL installed and configured. Create a `.env` file and set your database credentials.
    ```bash
    python manage.py migrate
    ```

5. **Run the development server**:
    ```bash
    python manage.py runserver
    ```

6. **Access the app**:
    Open a browser and go to `http://127.0.0.1:8000`

## **Technologies Used**

- **Backend**: Django, Django REST Framework
- **Database**: PostgreSQL
- **Frontend**: HTML5, CSS3, Bootstrap 5
- **Real-Time Communication**: Django Channels (for WebSockets and asynchronous features)
- **Deployment**: Heroku (planned)
- **Other Services**: Google Maps API (for displaying property locations)

## **Usage**

1. **Register** as a new user (either a property owner or renter).
2. **Post a property** if you're an owner, including details such as location, price, and images.
3. **Search for properties** using the filter options (price, location, etc.).
4. **Contact property owners** using the built-in chat (in progress).
5. **Manage properties** with CRUD functionalities (edit, delete).

## **Development Roadmap**

- [x] User Authentication (Login/Signup)
- [x] Property Listings with Images
- [x] Responsive Design
- [ ] Real-time Messaging via WebSockets (In Progress)
- [ ] Google Maps API for Property Location (In Progress)
- [ ] Deployment to Heroku or AWS (Upcoming)
- [ ] Performance and SEO Optimization

## **Contributing**

We welcome contributions to Renters Hub! If you'd like to contribute, please:

1. Fork the repository.
2. Create a new branch for your feature or fix.
3. Commit your changes and open a pull request.

## **License**

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
# Developers Portfolio Page with Django and React

## Introduction

Welcome to the repository of my Portfolio Page! This project is a hybrid web application built using the Django backend framework and the React frontend library. It leverages the power of Django for server-side rendering and React for a dynamic and interactive user interface. TypeScript is used for type-safe JavaScript, and Docker is used for containerization.

You can view a live demo of the application at [www.initial-commit.com](http://www.initial-commit.com).

## Features

- **Technologies**: Uses React, Django, and TypeScript.
- **Fetched Data**: Dynamically fetched from Django backend.
- **Responsive**: Adapts to all device screen sizes.
- **Dark Mode**: Toggleable dark mode.
- **Docker**: Supported for easy setup and deployment.

## Prerequisites

Ensure you have the following tools installed on your machine:

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)
- [Node.js](https://nodejs.org/) (for frontend development)
- [Python](https://www.python.org/) (for backend development)

## Getting Started

**Clone the repository:**

```bash
git clone https://github.com/VandaFarsad/portfolio-backend-service
cd portfolio-backend-boilerplate
```

**Start the application using Docker:**

```bash
docker compose up
```

The application will be accessible at:

- Backend (Django Admin Page): http://localhost:8000/admin
- Frontend (React App): http://localhost:3000/

For **production**, use the following command:

```bash
docker compose -f docker-compose.prod.yml up
```

**Create an environment file for production deployment:**

In order to deploy the application in production, create a `.env` file in the root directory. You can use [.env.local](.env.local) as a reference.

## Nginx in Production

For production, the Nginx service is used to serve the application. The Nginx configuration can be found in the [nginx](./nginx) directory.

Here is the GitHub repository for the Nginx image used in production: [JonasAlfredsson/docker-nginx-certbot](https://github.com/JonasAlfredsson/docker-nginx-certbot)

## Configuration

- Backend configuration files can be found in the `main` directory.
- Frontend configuration files can be found in the `frontend` directory.
- Nginx configuration for production is available in the `nginx` directory.

## License

This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.

## Acknowledgments

- Thanks to Jonas Alfredsson for the Nginx and Certbot Docker image. See the [GitHub Repository](https://github.com/JonasAlfredsson/docker-nginx-certbot).
- Thanks to the developers of the following React libraries and resources used in this project:
  - [React Vertical Timeline](https://github.com/stephane-monnot/react-vertical-timeline)
  - [React Typical Animation](https://github.com/maxeth/react-type-animation)
  - [React Toggle Dark Mode](https://github.com/JoseRFelix/react-toggle-dark-mode)
- Thanks to [Iconify Design](https://iconify.design/icon-sets/?query=angular) for providing the icons.
- Thanks to [Tholman](https://tholman.com/github-corners/) for the GitHub Ref Corner.
- Thanks to [Dorota1997](https://github.com/Dorota1997/react-frontend-dev-portfolio/blob/main/README.md) for inspiration.
- Thanks to ChatGPT, for generating this README ;-)

# CineBook — High-Concurrency Movie Ticket Booking System

CineBook is a production-style movie ticket booking platform built to practise and demonstrate essential backend engineering concepts such as API design, database modelling, concurrency control, background processing, testing, containerisation, CI/CD, cloud deployment, and system design.

The main technical challenge of this project is handling situations where many users attempt to reserve the same limited seats at the same time. The system must ensure that a seat is never confirmed for more than one user.

---

## User Booking Flow

Users will be able to complete the following booking journey:

```text
Register or Log In
        ↓
Browse Available Movies
        ↓
Select a Cinema and Show
        ↓
View the Seat Map
        ↓
Temporarily Hold Seats
        ↓
Complete Payment
        ↓
Receive Booking Confirmation
        ↓
View or Download the Ticket
```

A temporary seat-hold mechanism will prevent selected seats from being booked by another user while payment is in progress. If payment is not completed within the allowed time, the seats will automatically become available again.

---

## User Features

Users will be able to:

* Register a new account
* Log in securely
* Browse available movies
* View cinemas and show timings
* View real-time seat availability
* Select and temporarily reserve seats
* Complete a mock payment
* Receive a confirmed booking
* View previous and upcoming bookings
* Download or view booking tickets
* Cancel eligible bookings

---

## Administrator Features

Administrators will be able to:

* Create and manage movies
* Create and manage cinemas
* Create screens or auditoriums
* Configure seat layouts
* Create and schedule shows
* Set ticket prices
* Update or cancel shows
* View customer bookings
* View seat occupancy
* Manage movie and show availability

---

## Core Engineering Problems

This project focuses on solving real backend engineering problems, including:

* Preventing double booking of seats
* Handling concurrent seat-reservation requests
* Managing temporary seat holds
* Using database transactions correctly
* Implementing idempotent payment requests
* Processing background tasks reliably
* Expiring unpaid reservations
* Retrying failed background jobs
* Maintaining consistency between payments and bookings
* Designing scalable and maintainable APIs
* Monitoring application health and failures

---

## Technology Stack

### Backend

* **Python** — Primary backend programming language
* **FastAPI** — REST API framework
* **SQLAlchemy** — ORM and database interaction
* **PostgreSQL** — Primary relational database
* **Alembic** — Database migrations
* **Redis** — Caching, distributed locking, rate limiting, and temporary data
* **Amazon SQS** — Message queue for asynchronous processing
* **Pytest** — Unit and integration testing
* **Ruff** — Linting and code formatting
* **MyPy** — Static type checking

### Frontend

* **React** — User interface library
* **TypeScript** — Type-safe frontend development
* **Vite** — Frontend build tool
* **React Router** — Client-side routing
* **TanStack Query** — API state management and caching
* **Tailwind CSS or Basic CSS** — Styling

### Infrastructure and DevOps

* **Docker** — Application containerisation
* **Docker Compose** — Local development environment
* **GitHub** — Source control and collaboration
* **GitHub Actions** — Continuous integration and deployment
* **AWS ECS** — Container-based application deployment
* **AWS RDS** — Managed PostgreSQL database
* **AWS SQS** — Managed message queue
* **AWS ElastiCache** — Managed Redis service
* **AWS S3** — Ticket files and static asset storage
* **Amazon CloudWatch** — Logging, metrics, and monitoring
* **Terraform** — Infrastructure as code

---

## High-Level Architecture

```text
                    ┌─────────────────────┐
                    │   React Frontend    │
                    └──────────┬──────────┘
                               │
                               │ HTTP / REST
                               ▼
                    ┌─────────────────────┐
                    │   FastAPI Backend   │
                    └───────┬─────┬───────┘
                            │     │
                 ┌──────────┘     └──────────┐
                 ▼                           ▼
        ┌─────────────────┐         ┌─────────────────┐
        │   PostgreSQL    │         │      Redis      │
        │ Users, Shows,   │         │ Cache, Locks,   │
        │ Seats, Bookings │         │ Temporary Data  │
        └─────────────────┘         └─────────────────┘
                 │
                 ▼
        ┌─────────────────┐
        │   Amazon SQS    │
        │ Background Jobs │
        └────────┬────────┘
                 ▼
        ┌─────────────────┐
        │ Background      │
        │ Workers         │
        └─────────────────┘
```

---

## Seat Reservation Lifecycle

A seat may move through the following states:

```text
AVAILABLE
    ↓
HELD
    ↓
BOOKED
```

If the user does not complete payment before the hold expires:

```text
HELD
    ↓
AVAILABLE
```

Possible seat states:

* `AVAILABLE` — The seat can be selected
* `HELD` — The seat is temporarily reserved for a user
* `BOOKED` — The seat has been successfully paid for and confirmed
* `BLOCKED` — The seat has been disabled by an administrator

The database will remain the final source of truth for seat ownership and booking confirmation.

---

## Concurrency Requirement

The system must guarantee that a seat cannot be booked by more than one user, even when multiple requests arrive at nearly the same time.

For example:

```text
User A requests Seat A1
User B requests Seat A1
User C requests Seat A1
```

Only one request should succeed. The remaining users should receive a response explaining that the seat is no longer available.

This behaviour will be enforced using a combination of:

* PostgreSQL transactions
* Row-level locking
* Unique database constraints
* Idempotency keys
* Carefully defined reservation states
* Concurrency and integration tests

---

## Project Goals

The goals of this project are to:

* Build a production-style FastAPI application
* Improve confidence in backend development
* Understand database transactions and locking
* Learn how to handle concurrent requests
* Practise clean architecture and SOLID principles
* Write meaningful unit and integration tests
* Use Git branches, pull requests, and code reviews
* Handle merge conflicts correctly
* Build background-processing workflows
* Add logging, monitoring, and error handling
* Containerise the application using Docker
* Create CI/CD pipelines using GitHub Actions
* Deploy the application to AWS
* Document architecture and technical decisions
* Use the project later as a backend revision reference

---

## Project Status

The project is currently under active development.

### Current Phase

```text
Phase 1 — Project Setup and Engineering Foundation
```

Initial work includes:

* Repository setup
* FastAPI application setup
* PostgreSQL integration
* Redis integration
* Docker Compose configuration
* Code-quality tooling
* Testing setup
* Git workflow
* GitHub Actions CI pipeline

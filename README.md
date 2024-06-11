# lateshow-ted-gitonga
Here's the complete `README.md` with the tests section filled out:

```markdown
# Late Show API

This project is a Flask API for tracking episodes and guest appearances on a show. The API allows for CRUD operations on episodes, guests, and appearances, with data validation and relationships between models.

## Getting Started

Follow these instructions to set up the project on your local machine for development and testing purposes.

### Prerequisites

Make sure you have the following installed:

- Python 3.8+
- `pip` (Python package installer)
- `pipenv` (Python dependency manager)

### Installation

1. **Clone the repository:**

    ```bash
    git clone git@github.com:L35han/lateshow-ted-gitonga.git
    cd lateshow-ted-gitonga
    ```

2. **Install dependencies:**

    ```bash
    pip install pipenv
    pipenv install
    ```

3. **Activate the virtual environment:**

    ```bash
    pipenv shell
    ```

4. **Set up environment variables:**

    Create a `.env` file in the root directory of the project and add the following:

    ```env
    FLASK_APP=app.py
    DATABASE_URL=sqlite:///late_show.db
    ```

5. **Initialize the database:**

    ```bash
    flask db init
    flask db migrate -m "Initial migration"
    flask db upgrade
    ```

6. **Seed the database:**

    ```bash
    python seed.py
    ```

7. **Run the application:**

    ```bash
    flask run
    ```

    The application should now be running at `http://127.0.0.1:5000/`.

## Validation

- `Appearance` must have a `rating` between 1 and 5 (inclusive).

## Running Tests

To run tests, use the following command:

1. **Create a test database:**

    Ensure your `DATABASE_URL` in the `.env` file points to a test database.

    ```env
    DATABASE_URL=sqlite:///test_late_show.db
    ```

2. **Run the tests:**

    ```bash
    pytest
    ```

    Ensure you have `pytest` installed. If not, you can install it using:

    ```bash
    pip install pytest
    ```

## Contributing

Please read [CONTRIBUTING.md](https://github.com/L35han/lateshow-ted-gitonga/blob/main/CONTRIBUTING.md) for details on the code of conduct, and the process for submitting pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/L35han/lateshow-ted-gitonga/blob/main/LICENSE) file for details.
```

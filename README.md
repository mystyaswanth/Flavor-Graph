# FlavorGraph - Recipe Suggestion App

A modern Flask web application that suggests recipes based on available ingredients, provides substitutions, and generates shopping lists.

## Features

- **Recipe Suggestions**: Get personalized recipe recommendations based on ingredients you have.
- **Greedy Algorithm**: Ranks recipes by ingredient coverage.
- **Combination Suggestions**: Finds optimal combinations of recipes with minimal missing ingredients.
- **Ingredient Substitutions**: Provides alternatives for missing ingredients (e.g., dairy-free options).
- **Shopping List Generation**: Creates lists of ingredients to buy for selected recipes.
- **REST API**: JSON endpoints for programmatic access.
- **Responsive UI**: Modern Bootstrap-based interface.

## Project Structure

```
flavorgraph/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── README.md              # This file
├── src/
│   ├── __init__.py
│   ├── models.py          # Recipe data and mappings
│   ├── routes.py          # Flask routes and views
│   └── utils.py           # Helper functions and algorithms
├── static/
│   └── css/
│       └── style.css      # Custom styles
└── templates/
    ├── index.html         # Home page with input form
    ├── suggest.html       # Suggestions display
    └── shopping.html      # Shopping list
```

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd flavorgraph
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

### Development Mode
```bash
flask --app app.py run --host=0.0.0.0 --port=5000 --debug
```

Or simply press `F5` in VSCode.

### Production Mode
```bash
python app.py
```

The app will be available at `http://localhost:5000`.

## Usage

1. **Home Page**: Enter available ingredients separated by commas.
2. **Get Suggestions**: View greedy suggestions and best combinations.
3. **Generate Shopping List**: Select recipes to create a shopping list.
4. **API Access**: Use `/api/suggest` and `/api/analyze` endpoints for JSON responses.

## API Endpoints

- `GET /`: Home page
- `POST /suggest`: Get recipe suggestions (form)
- `POST /shopping`: Generate shopping list (form)
- `POST /api/suggest`: JSON API for suggestions
- `POST /api/analyze`: JSON API for recipe analysis

## Technologies Used

- **Backend**: Python, Flask
- **Frontend**: HTML, Bootstrap 5, Jinja2
- **Algorithms**: Greedy scoring, Backtracking for combinations

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make changes
4. Submit a pull request

## License

MIT License

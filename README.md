# Product Review Scraper

A web application that scrapes product reviews from a given URL and displays them in a user-friendly interface. The backend is built with Flask, and it uses Playwright for web scraping. The review section is identified dynamically using OpenAI's GPT API.

---

## Hosted Application

You can access and use the API directly without cloning the repository.  

### API Endpoint  
Base URL: `https://llm-in-api-server.onrender.com`  

### Available Routes

1. **Homepage**  
   - **URL:** `/`  
   - **Method:** `GET`  
   - **Description:** Displays the homepage where users can input a product URL.  

2. **Fetch Reviews**  
   - **URL:** `/api/reviews`  
   - **Method:** `GET`  
   - **Query Parameter:**  
     - `page` - The URL of the product page to scrape reviews from.  
   - **Response Format:**  
     ```json
     {
       "reviews_count": <number_of_reviews>,
       "reviews": [
         {
           "title": "<review_title>",
           "body": "<review_body>",
           "rating": <review_rating>,
           "reviewer": "<reviewer_name>"
         },
         ...
       ]
     }
     ```  

   - **Example Request:**  
     ```bash
     curl "https://llm-in-api-server.onrender.com/api/reviews?page=<product_url>"
     ```

   - **Example Response:**  
     ```json
     {
       "reviews_count": 5,
       "reviews": [
         {
           "title": "Great product!",
           "body": "This product exceeded my expectations.",
           "rating": 5,
           "reviewer": "John Doe"
         },
         {
           "title": "Not worth it",
           "body": "The product quality was disappointing.",
           "rating": 2,
           "reviewer": "Jane Smith"
         }
       ]
     }
     ```

---

## Features

- Dynamically identifies the review section on product pages using OpenAI GPT API.
- Scrapes multiple pages of reviews.
- Displays scraped reviews on the homepage or via API responses.
- Fully functional hosted application available online.

---

## Running Locally

If you'd like to clone and run the project locally, follow these steps:

### Prerequisites

- Python 3.8+
- Node.js (for Playwright installation)
- An OpenAI API key
- Git installed on your system

### Installation

1. Clone the repository:  
   ```bash
   git clone <repository-url>
   cd <repository-name>
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   playwright install
3. Set up your environment:
   Create a .env file in the project root.
   Add your OpenAI API key.
   ```bash
   OPENAI_API_KEY=<your_openai_api_key>
4. Run the application:
   ```bash
   python app.py
5. Open your browser and visit:
   ```bash
   http://127.0.0.1:5000

## Technologies Used

* **Flask:** Backend framework for building the API server.
* **Playwright:** For web scraping and browser automation.
* **OpenAI API:** Identifies the review section dynamically (requires a valid API key).
* **Python Dotenv:** Loads environment variables for secure API key usage.
* **Render.com:** Hosting platform for the global deployment of the app.
* **HTML/CSS:** Frontend technologies for building the user interface.

## Contact

If you have any questions or feedback, feel free to reach out:

* Email: djyothiraditya654@gmail.com

from playwright.sync_api import sync_playwright
import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')

def get_reviews(url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        page.goto(url)

        page_content = page.content()

        review_section = identify_review_section(page_content)

        reviews = extract_reviews_from_page(page, review_section)


        all_reviews = []
        while True:
            all_reviews.extend(reviews)
            next_button = page.locator("text=Next")
            if next_button.is_visible():
                next_button.click()
                page.wait_for_timeout(1000)
                reviews = extract_reviews_from_page(page, review_section)
            else:
                break
        
        browser.close()
        return all_reviews

def identify_review_section(page_content):
    """Identify the review section in the HTML content using OpenAI API"""
    response = openai.Completion.create(
        model="gpt-3.5-turbo",
        prompt=f"Analyze the following HTML content and identify the CSS selector related to product reviews:\n{page_content}",
        max_tokens=150
    )
    return response.choices[0].text.strip()

def extract_reviews_from_page(page, review_section):
    """Extract reviews from the page using the identified CSS selector"""
    reviews = []
    review_elements = page.locator(f"{review_section} .review-class")
    for review_element in review_elements:
        title = review_element.locator(".review-title").text_content()
        body = review_element.locator(".review-body").text_content()
        rating = int(review_element.locator(".review-rating").text_content())
        reviewer = review_element.locator(".reviewer-name").text_content()
        reviews.append({
            "title": title,
            "body": body,
            "rating": rating,
            "reviewer": reviewer
        })
    return reviews

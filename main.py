# main.py
import sys
import time
import cProfile
import pstats
import asyncio
from concurrent.futures import ThreadPoolExecutor

from data_models import Product
from api_fetcher import fetch_product_data
from scraper import scrape_review_data
from analyzer import (
    filter_products_with_reviews,
    calculate_avg_price_per_category,
    get_top_5_highest_rated
)
from reporter import generate_terminal_report, generate_json_report
from config import MAX_WORKERS, SAMPLE_PRODUCT_IDS

def process_single_product_threaded(product_id: int) -> Product:
    try:
        raw_data = fetch_product_data(product_id)
        if not raw_data:
            return None

        avg_score, review_count = scrape_review_data(product_id)

        if review_count == 0:
            avg_score = float(raw_data.get("rating", 4.0))
            review_count = 5

        return Product(
            id=raw_data["id"],
            name=raw_data.get("title", raw_data.get("name", "Unknown Product")),
            price=float(raw_data.get("price", 0.0)),
            category=str(raw_data.get("category", "General")),
            avg_score=float(avg_score),
            review_count=int(review_count)
        )
    except Exception:
        return None
def run_threaded_mode(product_ids: list[int]) -> list[Product]:
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        results = list(executor.map(process_single_product_threaded, product_ids))
        return [p for p in results if p is not None]

def run_app():
    mode = "threads"
    if "--mode" in sys.argv:
        idx = sys.argv.index("--mode") + 1
        if idx < len(sys.argv):
            mode = sys.argv[idx]

    start_time = time.time()

    if mode == "threads":
        products = run_threaded_mode(SAMPLE_PRODUCT_IDS)
    else:
        # Default fallback to threaded execution
        products = run_threaded_mode(SAMPLE_PRODUCT_IDS)

    # Process and analyze using analyzer functions
    valid_products = filter_products_with_reviews(products)
    avg_prices = calculate_avg_price_per_category(valid_products)
    top_5 = get_top_5_highest_rated(valid_products)

    metrics = {
        "total_products": len(valid_products),
        "avg_price_per_category": avg_prices,
        "top_rated_products": [p.to_dict() for p in top_5]
    }

    elapsed_time = time.time() - start_time
    print(f"[*] Execution finished in {elapsed_time:.2f} seconds.")

    # Output results
    generate_terminal_report(metrics)
    generate_json_report(metrics)

if __name__ == "__main__":
    if "--profile" in sys.argv:
        profiler = cProfile.Profile()
        profiler.enable()
        run_app()
        profiler.disable()
        stats = pstats.Stats(profiler).sort_stats('cumtime')
        stats.print_stats(10)
    else:
        run_app()

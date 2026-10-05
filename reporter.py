# reporter.py
import json

def generate_terminal_report(metrics: dict) -> None:
    print("\n" + "=" * 50)
    print("         MARKET RESEARCH ANALYSIS REPORT         ")
    print("=" * 50)
    print(f"Total Products Analyzed: {metrics.get('total_products', 0)}")
    print("-" * 50)
    print("AVERAGE PRICE PER CATEGORY:")
    for cat, avg_p in metrics.get("avg_price_per_category", {}).items():
        print(f"  - {cat}: ${avg_p:.2f}")
    print("-" * 50)
    print("TOP 5 HIGHEST RATED PRODUCTS:")
    for prod in metrics.get("top_rated_products", []):
        print(f"  - [{prod.get('avg_score', 0.0)}★] {prod.get('name', 'Unknown')} (${prod.get('price', 0.0)})")
    print("=" * 50 + "\n")

def generate_json_report(metrics: dict, filename: str = "report.json") -> None:
    try:
        with open(filename, "w") as f:
            json.dump(metrics, f, indent=4)
        print(f"[*] Report saved successfully to {filename}")
    except Exception as e:
        print(f"[!] Error writing JSON report: {e}")



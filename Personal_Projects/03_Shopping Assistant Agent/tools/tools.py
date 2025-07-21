from agents import function_tool
import requests
import logging

@function_tool
def fetch_api_data_according_product_name(product: str) -> dict:
    print("\nProduct Tool Called\n")
    try:
        response = requests.get(
            f"https://shopping-assistant-api-five.vercel.app/api/getproductsdata?productName={product}",
            timeout=5,
        )
        if response.status_code == 200:
            data = response.json()
            logging.info(f"Fetched product data: {data}")

            if data and "products" in data:
                formatted = "\n\n".join(
                    f"🕶️ **{p['name']}**\n"
                    f"💬 {p['description']}\n"
                    f"💵 Price: {p['price']} PKR\n"
                    f"🏷️ Category: {p['category']}"
                    for p in data["products"]
                )
                return {"products": data["products"], "formatted_output": formatted}
            else:
                return {"formatted_output": "I couldn't find any relevant information."}
        else:
            return {"formatted_output": "There was an error fetching the data. Please try again later."}
    except requests.exceptions.RequestException:
        return {"formatted_output": "There was an error fetching the data. Please try again later."}


@function_tool
def fetch_api_data_according_category(category: str) -> dict:
    print("\nCategory Tool Called\n")
    try:
        response = requests.get(
            f"https://shopping-assistant-api-five.vercel.app/api/getproductsbycategory?category={category}",
            timeout=5,
        )
        if response.status_code == 200:
            data = response.json()
            logging.info(f"Fetched category data: {data}")

            if data and "products" in data:
                formatted = "\n\n".join(
                    f"🕶️ **{p['name']}**\n"
                    f"💬 {p['description']}\n"
                    f"💵 Price: {p['price']} PKR\n"
                    f"🏷️ Category: {p['category']}"
                    for p in data["products"]
                )
                return {"products": data["products"], "formatted_output": formatted}
            else:
                return {"formatted_output": "I couldn't find any relevant information."}
        else:
            return {"formatted_output": "There was an error fetching the data. Please try again later."}
    except requests.exceptions.RequestException:
        return {"formatted_output": "There was an error fetching the data. Please try again later."}
import requests

def convert_currency(amount, from_currency, to_currency):
    # API endpoint with parameters
    url = f"https://api.frankfurter.app/latest?amount={amount}&from={from_currency}&to={to_currency}"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises HTTPError for bad status

        data = response.json()

        # Check if target currency is in the response
        if to_currency in data["rates"]:
            converted_amount = data["rates"][to_currency]
            print(f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}")
        else:
            print(f"Currency '{to_currency}' is not supported.")
    except requests.exceptions.RequestException as e:
        print("Network or API error:", e)
    except ValueError:
        print("Invalid input. Please enter numeric values.")
    except Exception as e:
        print("An unexpected error occurred:", e)

# Example usage
print("Currency Converter (No API Key Needed)")
from_currency = input("From currency (e.g., USD): ").upper()
to_currency = input("To currency (e.g., EUR): ").upper()

try:
    amount = float(input("Amount: "))
    convert_currency(amount, from_currency, to_currency)
except ValueError:
    print("Please enter a valid number for amount.")

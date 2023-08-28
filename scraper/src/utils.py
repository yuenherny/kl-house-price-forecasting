"""Utility functions for the project."""

def get_max_page_number_from_response(response) -> int:
    page_numbers = []
    for res in response:
        try:
            page_numbers.append(int(res.text))
        except:
            pass

    return max(page_numbers)
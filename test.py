form_data = {
    'entry.1588431833': ['0-12', '13-18', '19-30', '31-49', '50+'],
    'entry.1656534888': ['Yes / Иә / Да', 'No / Жоқ / Нет'],
    'entry.302442396': ['1', '2', '3', '4', '5',
                        'Strongly affects / Қатты әсер етеді / Сильно влияет'],
    'entry.1546954178': ['Always / Әрқашан / Всегда', 'Often / Жиі / Часто', 'Sometimes / Кейбір кезде / Иногда',
                        'Rarely / Жиі емес / Редко', 'Never / Ешқашан / Никогда'],
    'entry.1967286594': ['Yes / Иә / Да', 'No / Жоқ / Нет', 'Sometimes / Кейбір кезде / Иногда'],
    'entry.1132512635': ['Always / Әрқашан / Всегда', 'Often / Жиі / Часто', 'Sometimes / Кейбір кезде / Иногда',
                         'Rarely / Жиі емес / Редко', 'Never / Ешқашан / Никогда'],
    'entry.282484690': ['Yes / Иә / Да', 'No / Жоқ / Нет'],
    'entry.528134550': ['Always / Әрқашан / Всегда', 'Often / Жиі / Часто', 'Sometimes / Кейбір кезде / Иногда',
                         'Rarely / Жиі емес / Редко', 'Never / Ешқашан / Никогда'],
    'entry.932724944': ['Yes / Иә / Да', 'No / Жоқ / Нет', 'Sometimes / Кейбір кезде / Иногда'],
    'entry.932724944': ['Always / Әрқашан / Всегда', 'Often / Жиі / Часто', 'Sometimes / Кейбір кезде / Иногда',
                         'Rarely / Жиі емес / Редко', 'Never / Ешқашан / Никогда'],
    'ntry.1933996778': ['Instagram', 'YouTube', 'TikTok', 'Facebook', 'X (formerly Twitter)', 'Pinterest', 'ВКонтакте',
                         'Telegram channel/канал', 'Other:'],
    'entry.1063441752': ['1', '2', '3', '4', '5']
}
import requests
from bs4 import BeautifulSoup

def get_entry_ids(form_url):
    """Extracts entry IDs from a Google Form page using requests and BeautifulSoup.

    Args:
        form_url (str): The URL of the Google Form page.

    Returns:
        list: A list of entry IDs, or an empty list if none are found.
    """

    response = requests.get(form_url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the element containing entry IDs (may vary depending on form structure)
    entry_elements = soup.find_all('div', class_='entry-summary')  # Adjust the selector as needed

    entry_ids = []
    for entry in entry_elements:
        # Extract the entry ID from the element's attributes (may vary)
        entry_id = entry.get('data-entry-id')  # Adjust the attribute name as needed
        if entry_id:
            entry_ids.append(entry_id)

    return entry_ids

# Example usage (replace with your actual Google Form URL)
form_url = "https://docs.google.com/forms/d/e/1FAIpQLSeRk-OZGhqcIImy6aQdIvTd7_TOZB1HaUnazu1gFMUdRnD7aw"  # Replace with your form URL

entry_ids = get_entry_ids(form_url)

if entry_ids:
    print("Entry IDs:")
    for entry_id in entry_ids:
        print(entry_id)
else:
    print("No entry IDs found on the form page.")


# Google Form Submission Spammer

This script is designed to spam Google Forms with submissions. It should be noted that this script is intended for educational purposes only and should not be used for malicious intent.

## Description

This script utilizes multiple threads to submit form responses to a specified Google Form URL. It randomly selects responses for each form field from predefined options to simulate human input.

## Requirements

- Python 3.x
- Requests library (install via `pip install requests`)

## Usage

1. Ensure you have Python 3.x installed on your system.
2. Install the Requests library by running:
    ```sh
    pip install requests
    ```
3. Customize the script by providing the Google Form URL and form data.
4. Run the script:
    ```sh
    python main.py
    ```
5. Wait for the script to complete its execution. 

## Configuration

- `GoogleURL`: URL of the Google Form page.
- `form_data`: Dictionary containing form field IDs as keys and lists of possible responses as values.

## Warning

- Use this script responsibly and ethically. Do not use it to spam legitimate forms or engage in malicious activities.
- Be aware that using this script may violate terms of service of the platform hosting the form.
- Use at your own risk.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add some feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Disclaimer

This script is for educational purposes only. The author is not responsible for any misuse of this script.

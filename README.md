TWINE_USERNAME: "__token__"
* __token__: This is a special username used when authenticating with an API token instead of a traditional username/password combination. When using an API token, you set TWINE_USERNAME to __token__ to indicate that you're using token-based authentication.


TWINE_PASSWORD: ${{ secrets.PYPI_TOKEN }}
* secrets.PYPI_TOKEN: This is a reference to a GitHub secret that stores your PyPI API token. You need to create this secret in your GitHub repository settings. The API token is generated from your PyPI account and allows you to upload packages securely without exposing your actual PyPI account password.

How to Set Up the PyPI Token:
1. Generate a PyPI API Token:
   - Log in to your PyPI account.
   - Navigate to your account settings and create a new API token.
   - Make sure to set the token's scope to the project you want to publish or to the entire account if you prefer.
2. Add the Token to GitHub Secrets:
   - Go to your GitHub repository.
   - Click on "Settings" > "Secrets and variables" > "Actions".
   - Click "New repository secret".
   - Name the secret PYPI_TOKEN and paste the API token you copied from PyPI.

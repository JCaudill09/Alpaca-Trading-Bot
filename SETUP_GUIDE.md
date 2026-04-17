# SETUP_GUIDE

## Environment Setup
1. **Clone the Repository:**
   ```
   git clone https://github.com/JCaudill09/Alpaca-Trading-Bot.git
   cd Alpaca-Trading-Bot
   ```
2. **Install Dependencies:**
   Make sure you have Python installed. Then run:
   ```
   pip install -r requirements.txt
   ```

## API Credentials
1. **Get API Keys:**
   - Sign up for an account at [Alpaca](https://alpaca.markets).
   - Navigate to your API settings to find your keys.
   - Make sure to keep your API keys safe and do not expose them publicly.

2. **Set API Keys in Environment Variables:**
   - Create a `.env` file in the root directory of your project.
   - Add your keys to the `.env` file:
   ```
   ALPACA_API_KEY='your_api_key'
   ALPACA_SECRET_KEY='your_secret_key'
   ```

## Running the Bot
1. **Run the Bot:**
   ```
   python main.py
   ```
2. **Monitor Logs:**
   - Keep an eye on the console logs for updates and errors.

## Deployment Options
1. **Deploying Locally:**
   - Ensure your bot is running on a machine that has a constant internet connection.

2. **Cloud Deployment:**
   - Consider using services like AWS, Heroku, or DigitalOcean to deploy your bot for 24/7 operation. Follow their documentation for deploying Python applications.

3. **Containerization:**
   - You can also use Docker to containerize your application for easier deployment and scaling.
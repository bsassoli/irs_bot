#!/usr/bin/env python
import os
import argparse
import logging
import subprocess
import webbrowser
from threading import Timer
from src.irs_bot.server import start_server

def open_browser(url):
    """Open browser after a delay"""
    def _open_browser():
        webbrowser.open(url)
    Timer(1.5, _open_browser).start()

def start_react_dev_server():
    """Start the React development server"""
    try:
        # Change to the react-ui directory
        os.chdir('react-ui')

        # Start the React development server
        logging.info("Starting React development server...")
        process = subprocess.Popen(['npm', 'start'], stdout=subprocess.PIPE)

        # Change back to the original directory
        os.chdir('..')

        return process
    except Exception as e:
        logging.error(f"Failed to start React server: {str(e)}")
        return None

if __name__ == "__main__":
    # Configure logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.StreamHandler(),
            logging.FileHandler('irs_bot_server.log')
        ]
    )

    parser = argparse.ArgumentParser(description="Run the IRS Bot Flask server")
    parser.add_argument("--host", default="0.0.0.0", help="Host to run the server on")
    parser.add_argument("--port", type=int, default=5001, help="Port to run the server on")
    parser.add_argument("--debug", action="store_true", help="Run in debug mode")
    parser.add_argument("--no-react", action="store_true", help="Don't start the React development server")

    args = parser.parse_args()

    logging.info(f"Starting IRS Bot server on {args.host}:{args.port}...")

    # Set CORS headers
    from flask_cors import CORS
    from src.irs_bot.server import app
    CORS(app)

    # Start React development server if not disabled
    react_process = None
    if not args.no_react:
        react_process = start_react_dev_server()
        # Open browser to React UI
        open_browser("http://localhost:3000")

    try:
        # Start Flask server
        start_server(host=args.host, port=args.port, debug=args.debug)
    finally:
        # Clean up React process if it was started
        if react_process:
            logging.info("Stopping React development server...")
            react_process.terminate()
#!/usr/bin/env python
import os
import argparse
import logging
from src.irs_bot.server import start_server

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
    
    args = parser.parse_args()
    
    logging.info(f"Starting IRS Bot server on {args.host}:{args.port}...")
    
    # Set CORS headers
    from flask_cors import CORS
    from src.irs_bot.server import app
    CORS(app)
    
    start_server(host=args.host, port=args.port, debug=args.debug)
# Trading Setup (Exness & MT5)

This directory contains the configuration to start a trading environment on a VPS or local machine using Docker.

## Getting Started

1. **Start the environment**:
   ```bash
   docker-compose up -d
   ```

2. **Access the Desktop**:
   - Open your browser and go to `http://localhost:6901` (Password: `trading`).
   - Or use a VNC client on port `5901`.

3. **Install MT5**:
   Inside the VNC desktop, open a terminal and run the Exness MT5 installer:
   ```bash
   wget https://download.mql5.com/cdn/web/metaquotes.software.corp/mt5/mt5linux.sh
   chmod +x mt5linux.sh
   ./mt5linux.sh
   ```

4. **Login to Exness**:
   Once MT5 is installed, use your Exness account credentials to log in to the trading server.

## Files
- `docker-compose.yml`: Defines the VNC-enabled Ubuntu container.
- `data/`: Persistent storage for your MT5 data.

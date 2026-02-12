# Domain Controller

A domain controller service for managing Cloudflare DNS and security settings.

## Prerequisites

### Jules CLI
The Jules CLI is used for asynchronous coding tasks. To install it globally:
```bash
npm install -g @google/jules
```

### Docker
Docker is required for container management. To install on Ubuntu/Debian:
```bash
sudo apt update
sudo apt install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

Verify that Docker is running:
```bash
sudo systemctl status docker
sudo systemctl start docker
```

## Installation

You can install the package using pip:

```bash
pip install domain-controller
```

Or install from source:

### Using HTTPS
```bash
git clone https://github.com/A6-9V/domain-controller.git
cd domain-controller
pip install -e .
```

### Using SSH
```bash
git clone git@github.com:A6-9V/domain-controller.git
cd domain-controller
pip install -e .
```

### Using GitHub CLI
```bash
gh repo clone A6-9V/domain-controller
cd domain-controller
pip install -e .
```

## Usage

After installation, you can use the `domain-controller` command:

```bash
domain-controller --help
```

### Environment Variables

The tool requires the following environment variables:
- `CLOUDFLARE_API_TOKEN`: Your Cloudflare API token
- `CLOUDFLARE_ZONES`: Comma-separated list of domain:zone_id mappings (e.g., `example.com:id1,test.org:id2`)
- `CLOUDFLARE_ZONE_ID`: Generic fallback Zone ID
- `DOMAIN_NAME`: Domain name for the generic fallback
- `CLOUDFLARE_ACCOUNT_ID`: Your Cloudflare Account ID (optional)

### Commands

```bash
# List all zones in the account
domain-controller --list-zones

# Check security status for configured zones
domain-controller --status

# Set security level for configured zones
domain-controller --security-level high
# OR
domain-controller --set high

# List DNS records for configured zones
domain-controller --list-dns

# Target a specific domain
domain-controller --domain example.com --status
```

## Development

### Requirements

- Python 3.8 or higher
- `requests` library

### Running Tests

```bash
python -m pytest test_manage_cloudflare.py
```

## VS Code Setup

The project has been configured with VS Code settings to ensure a consistent development experience.

### Recommended Extensions
- **Prettier**: Code formatting
- **ESLint**: Linting
- **GitLens**: Git integration
- **MQL5 Support**: For MQL5 language support
- **Docker**: For container management

### Live Share
The project is set up for collaboration. Use the provided Live Share link to join the session.

## 📓 Knowledge Base
- **NotebookLM**: [Access here](https://notebooklm.google.com/notebook/e8f4c29d-9aec-4d5f-8f51-2ca168687616)
- **Note**: This notebook is available for reading and writing. AI agents must read it before starting work.

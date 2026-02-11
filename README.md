# Domain Controller

A domain controller service for managing Cloudflare DNS and security settings.

## Installation

You can install the package using pip:

```bash
pip install domain-controller
```

Or install from source:

```bash
git clone https://github.com/A6-9V/domain-controller.git
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
- `CLOUDFLARE_ZONE_ID`: The Zone ID for your domain
- `CLOUDFLARE_ACCOUNT_ID`: Your Cloudflare Account ID (optional)

### Commands

```bash
# Check security status
domain-controller --status

# Set security level
domain-controller --security-level high

# List DNS records
domain-controller --list-dns
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

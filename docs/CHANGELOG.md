# Changelog

## [2.0] - 2025-07-04

### Major Release: BLUX v2.0 – The Sovereign Android AI Forge ⚡️

#### Added
- **BLUX v2.0** released as a major update, introducing the Sovereign Android AI Forge platform[1].
- New bash script: `scripts/update.sh` for streamlined updates and maintenance[1].
- Enhanced plugin system: Now checks for syntax errors and missing dependencies in plugin files before updates[1].

#### Changed
- Overhauled core system to improve reliability and extensibility.

#### Fixed
- Improved error handling during plugin updates and dependency checks[1].

#### How to Test
- Instructions for testing BLUX v2.0 are included in the repository documentation[1].

---

### Detailed Features

- **Automated Update Script**
  - The new `scripts/update.sh` automates the process of updating BLUX and all plugins. It performs syntax checks and verifies dependencies before applying updates, reducing the risk of errors or incompatibility[1].

- **Advanced Plugin System**
  - Plugins are now validated for syntax and dependencies before activation, preventing runtime failures.
  - Plugin management (install, update, remove) is streamlined through the update script.

- **Professional Documentation**
  - The README and supporting docs have been rewritten for clarity, with detailed setup, usage, and troubleshooting guidance tailored for Termux and Android environments[1].

- **Modular, Extensible Architecture**
  - The core has been refactored to support easy addition and management of plugins, allowing users to expand BLUX’s capabilities without modifying the main codebase.

- **Sovereign AI Focus**
  - The platform is designed for privacy-first, user-controlled AI workflows on Android devices.

- **Enhanced Error Handling**
  - Improved detection and reporting of plugin errors and missing dependencies during updates.

- **User Experience Improvements**
  - Installation and update processes are now simpler, especially for Termux users.

---

### Plugin List (v2.0)

| Plugin Name           | Description                                              |
|-----------------------|----------------------------------------------------------|
| **jadis-hotmail**     | Integrates Hotmail/Outlook email functionality.          |
| **jadis-telegram**    | Enables Telegram messaging and automation.               |
| **jadis-whatsapp**    | Adds WhatsApp messaging capabilities.                    |
| **system-monitor**    | Monitors device resources and system health.             |
| **file-manager**      | Provides advanced file management tools.                 |
| **web-scraper**       | Allows data extraction from web pages.                   |
| **voice-assistant**   | Offers voice command and response features.              |
| **twrp-builder**      | Automates building TWRP recovery images for Android.     |

---

For detailed documentation, usage instructions, and future updates, see the main repository[1].

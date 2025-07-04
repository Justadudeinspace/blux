# 🔒 BLUX Security Guide

## Security Improvements Implemented

### Critical Vulnerabilities Fixed

#### 1. File Path Traversal Prevention
- **Location**: `blux/blux.py`
- **Fix**: Added proper path validation and directory traversal checks
- **Impact**: Prevents unauthorized file access outside the assets directory

#### 2. Command Injection Protection
- **Location**: `blux/ai_engine.py`
- **Fix**: Comprehensive input sanitization with regex validation
- **Features**:
  - Length limits (2048 characters max)
  - Character whitelist validation
  - Dangerous pattern detection
  - Absolute executable paths

#### 3. Secure Flask Configuration
- **Location**: `blux/web_ui.py`
- **Fix**: Cryptographically secure secret key generation and security headers
- **Features**:
  - Dynamic secret key generation using `secrets.token_urlsafe()`
  - Persistent key storage with restricted permissions (600)
  - Security headers (X-Content-Type-Options, X-Frame-Options, X-XSS-Protection)
  - Secure session configuration

#### 4. Input Validation Framework
- **Location**: `blux/terminal_ui.py`
- **Fix**: Centralized input validation with the `InputValidator` class
- **Features**:
  - Length limits for prompts (2048 chars) and notes (1024 chars)
  - Suspicious content detection (script tags, dangerous URLs)
  - Safe output escaping for display

#### 5. Plugin Security Enhancements
- **Location**: `blux/plugin_loader.py`
- **Fix**: Static analysis and validation before plugin loading
- **Features**:
  - File size limits (1MB max)
  - Dangerous pattern detection in source code
  - Path validation to ensure plugins are in trusted directory
  - Enhanced filename validation

#### 6. Dependency Security
- **Location**: `requirements.txt`
- **Fix**: Pinned versions and security-focused dependencies
- **Updates**:
  - All dependencies pinned to specific versions
  - Added cryptography for secure operations
  - Updated to latest secure versions

## Security Best Practices

### For Users

1. **Keep Dependencies Updated**: Regularly check for security updates
2. **Secure Configuration**: Ensure the `config/` directory has proper permissions
3. **Plugin Validation**: Only install plugins from trusted sources
4. **Input Awareness**: Be cautious with prompts and avoid pasting untrusted content

### For Developers

1. **Input Validation**: All user inputs should be validated through the `InputValidator` class
2. **Path Security**: Use absolute paths and validate against expected directories
3. **Subprocess Safety**: Always sanitize inputs before subprocess calls
4. **Error Handling**: Avoid leaking sensitive information in error messages

## Security Configuration

### Environment Variables

- `BLUX_DEBUG`: Set to `false` in production
- `BLUX_WEB_PORT`: Configure secure port (default: 8080)
- `BLUX_MAX_PROMPT_LENGTH`: Maximum prompt length (default: 2048)

### File Permissions

Ensure proper permissions on sensitive files:
```bash
chmod 600 config/secret.key  # Owner read/write only
chmod 755 blux/              # Standard directory permissions
```

## Security Testing

To verify security improvements:

```python
# Test input validation
from blux.terminal_ui import InputValidator
validator = InputValidator()

# This should work
safe_input = validator.validate_prompt("Hello world")

# This should be rejected
try:
    validator.validate_prompt("<script>alert(1)</script>")
except ValueError as e:
    print(f"Security working: {e}")
```

## Reporting Security Issues

If you discover security vulnerabilities:

1. **Do not** create public issues for security vulnerabilities
2. Email security issues to: justadudeinspace4244@hotmail.com
3. Include detailed steps to reproduce
4. Allow reasonable time for fixes before public disclosure

## Future Security Enhancements

Planned improvements:
- [ ] Rate limiting for API endpoints
- [ ] Enhanced plugin sandboxing
- [ ] Audit logging for security events
- [ ] HTTPS support for web interface
- [ ] Content Security Policy (CSP) headers
- [ ] Input sanitization testing framework

---

**Last Updated**: January 2025
**Version**: BLUX v2.0 Security Hardening
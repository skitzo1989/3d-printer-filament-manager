# Contributing to 3D Printer Filament Manager

Thank you for your interest in contributing to the 3D Printer Filament Manager! We welcome contributions of all kinds.

## 🤝 How to Contribute

### Reporting Bugs
- Use the GitHub Issues tab to report bugs
- Include your operating system, Python version, and browser
- Provide steps to reproduce the issue
- Include screenshots if applicable

### Suggesting Features
- Open an issue with the "enhancement" label
- Describe the feature and its benefits
- Consider implementation complexity
- Discuss with maintainers before starting work

### Code Contributions
1. **Fork the repository**
2. **Create a feature branch** (`git checkout -b feature/amazing-feature`)
3. **Make your changes**
4. **Test thoroughly**
5. **Commit your changes** (`git commit -m 'Add amazing feature'`)
6. **Push to your branch** (`git push origin feature/amazing-feature`)
7. **Open a Pull Request**

## 🏗️ Development Setup

### Prerequisites
- Python 3.8 or higher
- Git

### Quick Start
```bash
# Clone your fork
git clone https://github.com/yourusername/3d-printer-filament-manager.git
cd 3d-printer-filament-manager

# Run setup script
python setup.py

# Start development server
python main.py
```

### Manual Setup
```bash
# Install uv package manager
# Windows:
powershell -Command "Set-ExecutionPolicy RemoteSigned -scope CurrentUser -Force; iwr https://astral.sh/uv/install.ps1 -useb | iex"
# macOS/Linux:
curl -LsSf https://astral.sh/uv/install.sh | sh

# Create virtual environment
uv venv

# Activate virtual environment
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

# Install dependencies
uv pip install -r requirements.txt

# Setup database
python -c "from models import create_tables; create_tables()"

# Optional: Add sample data
python populate_sample_data.py
```

## 📝 Code Style

### Python
- Follow PEP 8 style guidelines
- Use type hints where possible
- Add docstrings for functions and classes
- Keep functions focused and small

### JavaScript
- Use modern ES6+ syntax
- Add comments for complex logic
- Follow consistent naming conventions
- Handle errors gracefully

### HTML/CSS
- Use semantic HTML elements
- Follow Bootstrap conventions
- Maintain responsive design
- Test across different browsers

## 🧪 Testing

### Before Submitting
- Test all functionality manually
- Verify responsive design works
- Check browser compatibility
- Test with sample data

### Areas to Test
- Add/edit/delete filaments
- Search and filtering
- Enhanced lookup feature
- Color display accuracy
- Settings management
- Cross-browser compatibility

## 🎯 Areas for Contribution

### High Priority
- **Mobile app** (React Native/Flutter)
- **Barcode scanning** integration
- **Import/export** functionality (CSV, JSON)
- **Advanced filtering** (date ranges, price ranges)
- **Inventory alerts** (low stock warnings)

### Medium Priority
- **Multi-user support** with authentication
- **Cloud backup** integration
- **Print history tracking**
- **Material cost calculator**
- **3D printer integration** (OctoPrint, Klipper)

### Low Priority
- **Dark theme** support
- **Internationalization** (multiple languages)
- **Advanced statistics** and charts
- **API documentation** with OpenAPI
- **Docker containerization**

## 📚 Documentation

### When Adding Features
- Update README.md if user-facing
- Add to CHANGELOG.md
- Create specific documentation if complex
- Update setup instructions if needed

### Documentation Style
- Use clear, concise language
- Include code examples
- Add screenshots for UI changes
- Maintain consistent formatting

## 🔍 Code Review Process

### Pull Request Requirements
- Clear description of changes
- Reference related issues
- Include testing notes
- Update documentation as needed

### Review Criteria
- Code quality and readability
- Feature completeness
- Testing coverage
- Documentation updates
- Backward compatibility

## 🏷️ Commit Message Guidelines

```
feat: add barcode scanning for filament entry
fix: resolve color mapping for metallic filaments
docs: update installation instructions
style: improve mobile responsive design
refactor: simplify lookup API endpoints
test: add unit tests for filament model
```

### Commit Types
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: UI/UX improvements
- `refactor`: Code refactoring
- `test`: Adding tests
- `chore`: Maintenance tasks

## 📞 Getting Help

### Communication
- **GitHub Issues** - Bug reports and feature requests
- **GitHub Discussions** - General questions and ideas
- **Email** - For sensitive security issues

### Resources
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)
- [Bootstrap Documentation](https://getbootstrap.com/docs/)
- [Jinja2 Documentation](https://jinja.palletsprojects.com/)

## 📜 License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

Thank you for helping make the 3D Printer Filament Manager better! 🎉
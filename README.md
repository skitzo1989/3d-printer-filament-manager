# 3D Printer Filament Manager

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-green.svg)](https://fastapi.tiangolo.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey.svg)](https://github.com/yourusername/3d-printer-filament-manager)

A comprehensive web application to manage your 3D printer filament inventory with intelligent lookup, brand-specific recommendations, and professional interface design.

![Application Screenshot](https://via.placeholder.com/800x400/007bff/ffffff?text=3D+Printer+Filament+Manager)

## ✨ Key Highlights

🔍 **Intelligent Lookup System** - Auto-fill specifications with brand-specific recommendations  
🎨 **Smart Color Recognition** - Accurate color display for compound names like "Galaxy Black"  
⚡ **Professional Interface** - Clean, responsive design with enhanced user experience  
📦 **Comprehensive Database** - 40+ brands, 11 materials, sample data included  
🔧 **Easy Setup** - Automated installation script and cross-platform compatibility

## Features

- **Filament Inventory Management**: Track all your filaments with detailed information
- **Color & Material Tracking**: Organize by brand, material type, and color
- **Storage Location Tracking**: Never lose track of where your filaments are stored
- **Temperature Settings**: Store recommended nozzle and bed temperatures for each filament
- **Enhanced Intelligent Lookup**: Auto-fill comprehensive specifications including manufacturer-specific recommended temperatures and optimal print speeds
- **Brand-Specific Profiles**: 40+ supported brands with tailored temperature and speed recommendations  
- **Search & Filter**: Quickly find filaments by brand, material, or color
- **Purchase Tracking**: Keep track of purchase dates and prices
- **Notes**: Add custom notes for each filament
- **Professional Interface**: Clean, responsive design with enhanced large 3D cube favicon
- **Intelligent Color Display**: Smart color mapping for compound names (e.g., "Transparent Red", "Galaxy Black")
- **Smart Delete Confirmations**: Optional "do not ask again" setting for streamlined workflow

## Supported Filament Types

- PLA (Polylactic Acid)
- ABS (Acrylonitrile Butadiene Styrene)
- PETG (Polyethylene Terephthalate Glycol)
- TPU (Thermoplastic Polyurethane) - Flexible
- ASA (Acrylonitrile Styrene Acrylate)
- PC (Polycarbonate)
- Nylon
- Wood Fill
- Metal Fill
- Carbon Fiber
- PVA (Support material)
- HIPS (High Impact Polystyrene)

## 🚀 Quick Start

### Automated Setup (Recommended)
```bash
# Clone the repository
git clone https://github.com/yourusername/3d-printer-filament-manager.git
cd 3d-printer-filament-manager

# Run the setup script
python setup.py
```

The setup script will:
- ✅ Check Python version (3.8+ required)
- ✅ Install uv package manager
- ✅ Create virtual environment
- ✅ Install all dependencies
- ✅ Setup database
- ✅ Generate favicon files
- ✅ Optionally add sample data

### Manual Installation

#### Prerequisites
- Python 3.8 or higher
- Git (optional, for cloning)

#### Step-by-Step
1. **Download the project**
   ```bash
   git clone https://github.com/yourusername/3d-printer-filament-manager.git
   cd 3d-printer-filament-manager
   ```

2. **Install uv package manager**
   ```bash
   # Windows
   powershell -Command "Set-ExecutionPolicy RemoteSigned -scope CurrentUser -Force; iwr https://astral.sh/uv/install.ps1 -useb | iex"
   
   # macOS/Linux
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

3. **Setup virtual environment**
   ```bash
   uv venv
   
   # Activate environment
   # Windows:
   .venv\Scripts\activate
   # macOS/Linux:
   source .venv/bin/activate
   ```

4. **Install dependencies**
   ```bash
   uv pip install -r requirements.txt
   ```

5. **Setup database**
   ```bash
   python -c "from models import create_tables; create_tables()"
   
   # Optional: Add sample data
   python populate_sample_data.py
   ```

## Running the Application

1. Start the web server:
   ```bash
   python main.py
   ```
   or
   ```bash
   uvicorn main:app --reload --host 0.0.0.0 --port 8847
   ```

2. Open your web browser and navigate to: `http://localhost:8847`

## Usage

### Adding Filaments

1. Click "Add New Filament" from the main page
2. Fill in the required fields (Brand, Material, Color, Diameter)
3. Optionally add temperature settings, storage location, and notes
4. Click "Add Filament" to save

### Managing Inventory

- **View All Filaments**: The main page displays all your filaments in card format
- **Search**: Use the search bar to find specific filaments
- **Filter**: Filter by material type or brand
- **Edit**: Click the "Edit" button on any filament card to modify its details
- **Delete**: Click the "Delete" button to remove a filament from inventory
  - First deletion shows confirmation dialog with optional "don't ask again" checkbox
  - Use Settings dropdown to manage confirmation preferences

### Enhanced Temperature & Speed Reference

The application includes comprehensive specifications with manufacturer recommendations:
- **PLA**: 190-220°C range (rec: 200-215°C), 60°C bed, 60-70 mm/s
- **ABS**: 220-250°C range (rec: 235-255°C), 90°C bed, 50-60 mm/s
- **PETG**: 220-250°C range (rec: 230-250°C), 75°C bed, 45-55 mm/s
- **TPU**: 210-230°C range (rec: 220-225°C), 50°C bed, 15-20 mm/s

**Brand-Specific Optimizations Available For:**
- Hatchbox, eSUN, PRUSAMENT, Overture, SUNLU, Polymaker, 3DHojor

## API Endpoints

The application also provides a REST API:

- `GET /api/filaments` - Get all filaments
- `GET /api/filaments/{id}` - Get specific filament
- `POST /api/filaments` - Create new filament
- `PUT /api/filaments/{id}` - Update filament
- `DELETE /api/filaments/{id}` - Delete filament

## 📊 Sample Data

The application includes comprehensive sample data to demonstrate all features:
- **32 realistic filaments** across 15 brands and 11 material types
- **Professional organization** with 20+ storage locations  
- **Price range** from budget ($16.99) to engineering grade ($59.99)
- **Special materials** including wood-fill, metal-fill, flexible, and glow-in-dark

## 💾 Data Storage

- **Local SQLite database** (`filament_inventory.db`) - No cloud required
- **Browser localStorage** for user preferences (delete confirmations, etc.)
- **No internet connection** required after initial setup
- **Easy backup** - Simply copy the database file

## Design Features

### Enhanced 3D Cube Favicon
- **4.8x larger** cube that uses 47% of the icon space (vs 10% previously)
- **High contrast** white, light blue, and blue gradient for better visibility
- **Multiple formats** supported: ICO, PNG, SVG for all browsers and devices
- **Scalable design** that looks great from 16x16 to 192x192 pixels

## 🤝 Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

### Quick Contribution Ideas
- 📱 Mobile app development
- 🔍 Barcode scanning integration  
- 📊 Advanced statistics and charts
- 🌍 Internationalization support
- 🎨 Dark theme implementation

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built with [FastAPI](https://fastapi.tiangolo.com/) for the backend
- [Bootstrap 5](https://getbootstrap.com/) for the responsive UI
- [SQLAlchemy](https://www.sqlalchemy.org/) for database management
- [uv](https://github.com/astral-sh/uv) for fast package management

## 📈 Project Stats

- **Lines of Code**: ~2,000+ (Python, JavaScript, HTML)
- **Features**: 15+ major features implemented
- **Supported Browsers**: Chrome, Firefox, Safari, Edge
- **Database Records**: 32 sample filaments included
- **Documentation**: Comprehensive guides and API docs

---

**⭐ Star this project if you find it useful!**
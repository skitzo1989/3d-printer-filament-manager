# Changelog

All notable changes to the 3D Printer Filament Manager project will be documented in this file.

## [1.0.0] - 2025-07-12

### 🎉 Initial Release

#### ✅ Core Features
- **Comprehensive Filament Management** - Add, edit, delete, and search filaments
- **Advanced Search & Filtering** - Filter by brand, material, color, and text search
- **Storage Location Tracking** - Organize filaments with custom storage locations
- **Purchase Tracking** - Track purchase dates, prices, and notes
- **Temperature Management** - Store min/max nozzle temps and bed temperatures

#### 🔍 Enhanced Lookup System
- **Intelligent Brand Autocomplete** - 40+ supported brands with real-time suggestions
- **Brand-Specific Profiles** - Custom temperature and speed recommendations for major brands:
  - Hatchbox, eSUN, PRUSAMENT, Overture, SUNLU, Polymaker, 3DHojor
- **Material Database** - Comprehensive defaults for 11 material types:
  - PLA, ABS, PETG, TPU, ASA, PC, Nylon, Wood Fill, Metal Fill, HIPS, PVA
- **Recommended Settings** - Manufacturer-specific optimal temperatures and print speeds

#### 🎨 Professional Interface
- **Enhanced Color Mapping** - Smart color recognition for compound names
  - Supports "True Black", "Transparent Red", "Galaxy Black", "Silk Gold", etc.
  - Intelligent parsing of modifiers (dark, light, transparent, metallic)
- **Clean Line Wrapping** - Temperature badges wrap as complete units
- **Large 3D Cube Favicon** - 4.8x larger, easily distinguishable icon
- **Responsive Design** - Works on desktop, tablet, and mobile

#### 🔧 Advanced Features
- **Smart Delete Confirmations** - Optional "do not ask again" setting
- **Settings Management** - Dropdown for user preferences
- **Database Migration** - Automatic schema updates for new fields
- **Sample Data Generator** - 32 realistic filaments across multiple brands
- **Windows Integration** - Batch files and PowerShell scripts for easy startup

### 📊 Sample Data Included
- **15 Brands** - From budget (AmazonBasics) to premium (PRUSAMENT)
- **11 Materials** - Including specialty materials like metal-fill and flexible TPU
- **26 Colors** - Standard colors plus special effects (silk, glow-in-dark)
- **Realistic Organization** - 20+ storage locations with logical grouping
- **Price Range** - $16.99 (budget) to $59.99 (engineering grade)

### 🛠️ Technical Specifications
- **Backend** - FastAPI with SQLAlchemy ORM
- **Database** - SQLite for local storage
- **Frontend** - Jinja2 templates with Bootstrap 5
- **Package Manager** - UV for fast dependency management
- **Python** - Compatible with Python 3.8+

### 📁 Project Structure
- Clean, production-ready codebase
- Comprehensive documentation
- Automated setup script
- Cross-platform compatibility
- MIT license for open source use

---

## Development History

### 2025-07-12 - Enhanced Autocomplete
- Fixed JavaScript structure issues
- Implemented real-time brand suggestions
- Added comprehensive error handling

### 2025-07-12 - Temperature & Speed Recommendations
- Added `nozzle_temp_recommended` and `print_speed_recommended` fields
- Implemented brand-specific lookup profiles
- Enhanced lookup API with comprehensive specifications
- Updated UI to display all temperature and speed information

### 2025-07-12 - Favicon Enhancement
- Redesigned favicon with 4.8x larger cube
- Improved visibility and recognition at small sizes
- Generated multiple formats (ICO, SVG, PNG)
- Added high-resolution versions for mobile devices

### 2025-07-12 - Color Mapping Fix
- Enhanced color recognition for compound names
- Added support for 26+ specific colors from sample data
- Implemented intelligent color parsing with modifiers
- Added gradient support for special effects

### 2025-07-12 - Line Wrapping Fix
- Fixed temperature badge wrapping issues
- Implemented `display: inline-block` and `white-space: nowrap`
- Added proper spacing and container styling
- Ensured badges wrap as complete units

### 2025-07-12 - Database Population
- Created comprehensive sample dataset
- Added 32 realistic filaments across multiple categories
- Organized storage locations and pricing
- Included specialty materials and effects

### 2025-07-12 - Project Cleanup
- Removed 22 development and test files
- Streamlined to production-ready structure
- Maintained only essential files and utilities
- Created clean project documentation

### 2025-07-12 - Delete Confirmation Enhancement
- Replaced basic confirm() with professional modal
- Added "do not ask again" option with localStorage
- Implemented settings management interface
- Added toast notifications for user feedback

### 2025-07-12 - GitHub Preparation
- Created comprehensive .gitignore
- Added requirements.txt with all dependencies
- Added MIT license
- Created automated setup script
- Prepared for public distribution
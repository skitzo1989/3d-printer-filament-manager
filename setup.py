#!/usr/bin/env python3
"""
Setup script for 3D Printer Filament Manager
"""

import os
import sys
import subprocess
import platform

def check_python_version():
    """Check if Python version is 3.8 or higher"""
    if sys.version_info < (3, 8):
        print("❌ Error: Python 3.8 or higher is required.")
        print(f"Current version: {sys.version}")
        sys.exit(1)
    print(f"✅ Python {sys.version.split()[0]} is compatible")

def install_uv():
    """Install uv package manager if not available"""
    try:
        subprocess.run([sys.executable, "-c", "import uv"], check=True, capture_output=True)
        print("✅ uv is already installed")
        return True
    except subprocess.CalledProcessError:
        print("📦 Installing uv package manager...")
        try:
            if platform.system() == "Windows":
                # Use PowerShell installation method for Windows
                ps_command = 'Set-ExecutionPolicy RemoteSigned -scope CurrentUser -Force; iwr https://astral.sh/uv/install.ps1 -useb | iex'
                subprocess.run(["powershell", "-Command", ps_command], check=True)
            else:
                # Use pip as fallback
                subprocess.run([sys.executable, "-m", "pip", "install", "uv"], check=True)
            print("✅ uv installed successfully")
            return True
        except subprocess.CalledProcessError as e:
            print(f"❌ Failed to install uv: {e}")
            return False

def setup_virtual_environment():
    """Create and setup virtual environment"""
    venv_path = ".venv"
    
    if os.path.exists(venv_path):
        print("✅ Virtual environment already exists")
    else:
        print("🔧 Creating virtual environment...")
        try:
            subprocess.run(["uv", "venv"], check=True)
            print("✅ Virtual environment created")
        except subprocess.CalledProcessError as e:
            print(f"❌ Failed to create virtual environment: {e}")
            return False
    
    return True

def install_dependencies():
    """Install project dependencies"""
    print("📦 Installing dependencies...")
    try:
        subprocess.run(["uv", "pip", "install", "-r", "requirements.txt"], check=True)
        print("✅ Dependencies installed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to install dependencies: {e}")
        return False

def setup_database():
    """Setup database and populate with sample data"""
    print("🗄️  Setting up database...")
    try:
        # Create database tables
        if platform.system() == "Windows":
            subprocess.run([".venv\\Scripts\\python.exe", "-c", "from models import create_tables; create_tables()"], check=True)
        else:
            subprocess.run([".venv/bin/python", "-c", "from models import create_tables; create_tables()"], check=True)
        print("✅ Database tables created")
        
        # Ask user if they want sample data
        response = input("📊 Would you like to populate the database with sample filaments? (y/n): ").lower().strip()
        if response in ['y', 'yes']:
            if platform.system() == "Windows":
                subprocess.run([".venv\\Scripts\\python.exe", "populate_sample_data.py"], check=True)
            else:
                subprocess.run([".venv/bin/python", "populate_sample_data.py"], check=True)
            print("✅ Sample data added successfully")
        
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Database setup failed: {e}")
        return False

def generate_favicon():
    """Generate favicon files"""
    print("🎨 Generating favicon files...")
    try:
        if platform.system() == "Windows":
            subprocess.run([".venv\\Scripts\\python.exe", "generate_favicon.py"], check=True)
        else:
            subprocess.run([".venv/bin/python", "generate_favicon.py"], check=True)
        print("✅ Favicon files generated")
        return True
    except subprocess.CalledProcessError as e:
        print(f"⚠️  Favicon generation failed (optional): {e}")
        return True  # Don't fail setup for this

def main():
    """Main setup process"""
    print("🚀 3D Printer Filament Manager Setup")
    print("=" * 50)
    
    # Check Python version
    check_python_version()
    
    # Install uv
    if not install_uv():
        print("❌ Setup failed: Could not install uv")
        sys.exit(1)
    
    # Setup virtual environment
    if not setup_virtual_environment():
        print("❌ Setup failed: Virtual environment creation failed")
        sys.exit(1)
    
    # Install dependencies
    if not install_dependencies():
        print("❌ Setup failed: Dependency installation failed")
        sys.exit(1)
    
    # Setup database
    if not setup_database():
        print("❌ Setup failed: Database setup failed")
        sys.exit(1)
    
    # Generate favicon
    generate_favicon()
    
    print("\n" + "=" * 50)
    print("✅ Setup completed successfully!")
    print("\n🎯 Next steps:")
    print("1. Run the application:")
    if platform.system() == "Windows":
        print("   python main.py")
        print("   # or use the batch file:")
        print("   start_filament_manager.bat")
    else:
        print("   .venv/bin/python main.py")
    print("\n2. Open your browser to: http://localhost:8847")
    print("3. Start managing your 3D printer filaments!")
    
    print("\n📚 Documentation:")
    print("- README.md - Complete application guide")
    print("- LOOKUP_FEATURE.md - Enhanced lookup system details")
    print("- SAMPLE_DATA_SUMMARY.md - Information about sample data")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n⏹️  Setup cancelled by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Setup failed with error: {e}")
        sys.exit(1)
#!/usr/bin/env python3
"""
Setup script for MTL Global Accounting Team - MSB Call Report XML Project

This script sets up the development environment and installs required dependencies.
"""

import subprocess
import sys
import os
from pathlib import Path

def run_command(command, description):
    """Run a command and handle errors."""
    print(f"Running: {description}")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed:")
        print(f"   Error: {e}")
        if e.stdout:
            print(f"   Stdout: {e.stdout}")
        if e.stderr:
            print(f"   Stderr: {e.stderr}")
        return False

def check_python_version():
    """Check if Python version is compatible."""
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 7):
        print(f"❌ Python 3.7+ is required. Current version: {version.major}.{version.minor}")
        return False
    print(f"✅ Python version {version.major}.{version.minor}.{version.micro} is compatible")
    return True

def install_dependencies():
    """Install required Python packages."""
    print("\n📦 Installing Python dependencies...")
    
    # Upgrade pip first
    if not run_command("pip install --upgrade pip", "Upgrading pip"):
        return False
    
    # Install requirements
    requirements_file = Path("requirements.txt")
    if requirements_file.exists():
        if not run_command("pip install -r requirements.txt", "Installing requirements"):
            return False
    else:
        print("⚠️  requirements.txt not found, installing packages individually...")
        packages = ["PyPDF2", "lxml", "xmlschema", "pandas", "numpy"]
        for package in packages:
            if not run_command(f"pip install {package}", f"Installing {package}"):
                return False
    
    return True

def create_directories():
    """Create necessary directories if they don't exist."""
    print("\n📁 Creating project directories...")
    
    directories = [
        "data/output",
        "data/shopify_transactions",
        "templates/schema",
        "docs",
        "tools"
    ]
    
    for directory in directories:
        Path(directory).mkdir(parents=True, exist_ok=True)
        print(f"✅ Created directory: {directory}")
    
    return True

def test_installation():
    """Test if the installation was successful."""
    print("\n🧪 Testing installation...")
    
    try:
        import PyPDF2
        print("✅ PyPDF2 imported successfully")
    except ImportError:
        print("❌ PyPDF2 import failed")
        return False
    
    try:
        import lxml
        print("✅ lxml imported successfully")
    except ImportError:
        print("❌ lxml import failed")
        return False
    
    try:
        import xmlschema
        print("✅ xmlschema imported successfully")
    except ImportError:
        print("❌ xmlschema import failed")
        return False
    
    return True

def main():
    """Main setup function."""
    print("🚀 Setting up MTL Global Accounting Team - MSB Call Report XML Project")
    print("=" * 70)
    
    # Check Python version
    if not check_python_version():
        sys.exit(1)
    
    # Create directories
    if not create_directories():
        print("❌ Failed to create directories")
        sys.exit(1)
    
    # Install dependencies
    if not install_dependencies():
        print("❌ Failed to install dependencies")
        sys.exit(1)
    
    # Test installation
    if not test_installation():
        print("❌ Installation test failed")
        sys.exit(1)
    
    print("\n🎉 Setup completed successfully!")
    print("\nNext steps:")
    print("1. Review the documentation in the 'docs' folder")
    print("2. Check the sample data structure in 'data/shopify_transactions'")
    print("3. Use the tools in the 'tools' folder to generate and validate XML")
    print("4. Customize the templates for your specific needs")
    print("\nFor help, refer to the README.md file")

if __name__ == "__main__":
    main()

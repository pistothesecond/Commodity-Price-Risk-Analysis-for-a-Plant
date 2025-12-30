"""Verify that all required packages are installed correctly."""

def verify_imports():
    packages = {
        'numpy': 'np',
        'pandas': 'pd',
        'matplotlib.pyplot': 'plt',
        'scipy': 'scipy',
        'seaborn': 'sns'
    }
    
    print("Verifying package installations...\n")
    
    for package, alias in packages.items():
        try:
            __import__(package)
            print(f"✓ {package}")
        except ImportError:
            print(f"✗ {package} - FAILED")
            return False
    
    print("\n✓ All packages installed successfully!")
    return True

if __name__ == "__main__":
    verify_imports()
from setuptools import setup, find_packages

setup(
    name="dsa-python",                   # Project name
    version="0.1.0",                     # Initial version
    description="A Python project for learning Data Structures and Algorithms using modern testing and type checking practices.",
    long_description=open("README.md").read(),  # Detailed description from README.md
    long_description_content_type="text/markdown",  # Format of the README.md
    author="Aakash Bamne",                  # Replace with your name
    author_email="aakash.work.001@gmail.com",  # Replace with your email
    url="https://github.com/yourusername/dsa-python",  # Replace with your GitHub repository URL
    packages=find_packages(),           # Automatically find all packages in the project
    install_requires=[
        "pytest>=7.0.0",                # Testing framework
        "assertpy>=1.1",                # Fluent assertion library
        "hypothesis>=6.0",              # Property-based testing
        "pytest-cov>=3.0",              # Code coverage
        "mypy>=0.971",                  # Static type checking
    ],
    classifiers=[
        "Programming Language :: Python :: 3",          # General Python compatibility
        "Programming Language :: Python :: 3.9",        # Specific version compatibility
        "Programming Language :: Python :: 3.12",       # Python 3.12 compatibility
        "License :: OSI Approved :: MIT License",       # Use MIT license (replace if different)
        "Operating System :: OS Independent",           # Platform independent
    ],
    python_requires=">=3.9",             # Minimum Python version required
    include_package_data=True,           # Include additional files (e.g., README.md)
    entry_points={                       # Optional: CLI tools
        "console_scripts": [
            # "example-cli=your_package.module:function",  # Example CLI command mapping
        ],
    },
)

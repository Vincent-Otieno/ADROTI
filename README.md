# Vincent Otieno's Portfolio - README

## Overview
This is a simple Python-based portfolio representation for Vincent Otieno, a Software Developer & Data Enthusiast from Nairobi, Kenya. The code demonstrates object-oriented programming to organize and display professional information.

## Features
- Personal information display
- Skills categorization
- Contact information
- Clean, object-oriented structure

## Requirements
- Python 3.x (No external dependencies required)

## Usage
1. Clone the repository or copy the code
2. Run the script:
   ```bash
   python portfolio.py
   ```

## Code Structure
```python
class Portfolio:
    def __init__(self):  # Initializes portfolio data
        self.name = "Vincent Otieno"
        self.email = "otienovincent299@gmail.com"
        # ... other attributes
        
    def display_intro(self):  # Shows introduction
        # ... implementation
        
    def show_skills(self):  # Displays technical skills
        # ... implementation
        
    def contact(self):  # Shows contact information
        # ... implementation
```

## Sample Output
When executed, the program will display:
```
Welcome to Vincent Otieno's Portfolio!
--------------------------------
Email: otienovincent299@gmail.com
Location: Nairobi, Kenya

I'm a passionate software developer & data enthusiast with experience in building
web applications and working with data.

Technical Skills:
- Programming: Python, JavaScript, Java
- Web Development: HTML/CSS, React, Flask
- Data Analysis: Pandas, NumPy, Matplotlib
- Database: SQL, MongoDB
- Other: Git, Linux

Let's connect! Reach me at otienovincent299@gmail.com
```

## Customization
To personalize this portfolio:
1. Update the `__init__` method with your information
2. Modify the skills and categories as needed
3. Add new methods for additional sections (projects, education, etc.)

## License
This is free to use and modify (MIT License).

## Contact
Vincent Otieno  
Email: otienovincent299@gmail.com  
Location: Nairobi, Kenya

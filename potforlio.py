class Portfolio:
    def __init__(self):
        self.name = "Vincent Otieno"
        self.email = "otienovincent299@gmail.com"
        self.title = "Software Developer & Data Enthusiast"
        self.location = "Nairobi, Kenya"
        self.skills = {
            'Programming': ['Python', 'JavaScript', 'Java'],
            'Web Development': ['HTML/CSS', 'React', 'Flask'],
            'Data Analysis': ['Pandas', 'NumPy', 'Matplotlib'],
            'Database': ['SQL', 'MongoDB'],
            'Other': ['Git', 'Linux']
        }
        self.interests = [
            "Open-source contributions",
            "Machine learning",
            "Cloud computing",
            "Technical writing"
        ]
    
    def display_intro(self):
        print(f"""
        Welcome to {self.name}'s Portfolio!
        -------------------------------
        Email: {self.email}
        Location: {self.location}
        
        I'm a passionate {self.title.lower()} with experience in building
        web applications and working with data.
        """)
    
    def show_skills(self):
        print("\nTechnical Skills:")
        for category, skills in self.skills.items():
            print(f"- {category}: {', '.join(skills)}")
    
    def contact(self):
        print(f"\nLet's connect! Reach me at {self.email}")

# Create and display portfolio
vincent = Portfolio()
vincent.display_intro()
vincent.show_skills()
vincent.contact()
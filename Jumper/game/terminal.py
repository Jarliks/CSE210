class Terminal:
    """Simple class for getting user inputs from the terminal"""
    
    def read_input(self, prompt):
        """accepts user inputs while using a provided prompt for the input"""
        return input(prompt)
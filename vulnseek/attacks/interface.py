from abc import ABC, abstractmethod

class AttackInterface:
    """Attack to be used on an API"""

    @abstractmethod
    def title(self):
        """
        Returns a string to display in main menu when selecting attacks
        """
        return
    
    @abstractmethod
    def run(self):
        """
        Runs the attack
        All outputs to stdout and stderr must also be outputted to the output file
        """
        return
    
    @abstractmethod
    def output_filename(self):
        """
        Returns a string indicating the output filename of this attack
        """
        return
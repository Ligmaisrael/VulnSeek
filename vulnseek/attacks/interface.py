class AttackInterface:
    """Attack to be used on an API"""

    def title(self):
        """
        Returns a string to display in main menu when selecting attacks
        """
        raise NotImplementedError

    def prompt_for_params(self):
        """
        Runs functions related to prompting the user to input parameters
        needed to run the attack
        """
        raise NotImplementedError

    def run(self):
        """
        Runs the attack
        All outputs to stdout and stderr must also be outputted to the output file
        """
        raise NotImplementedError

    def output_filename(self):
        """
        Returns a string indicating the output filename of this attack
        """
        raise NotImplementedError

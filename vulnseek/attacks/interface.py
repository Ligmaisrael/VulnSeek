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

        Must be called by run()
        """
        raise NotImplementedError

    def run(self):
        """
        Runs the attack
        All outputs to stdout and stderr must also be outputted to the output file
        """
        raise NotImplementedError

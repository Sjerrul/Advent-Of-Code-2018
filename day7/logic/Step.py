class Step:
    step_id = None
    requirements = None

    def __init__(self, step_id):
        self.step_id = step_id
        self.requirements = []

    def add_requirement(self, requirement):
        self.requirements.append(requirement)

    def __repr__(self):
        return "Step %s - Requirements: %s" % (self.step_id, self.requirements)

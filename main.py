class Brain:
    def __init__(self):
        self.regions = []

    def add_region(self, region):
        self.regions.append(region)
    
    def describe(self):
        return (f'This brain has {len(self.regions)} regions: ' + ', '.join(region.name for region in self.regions))

class Cerebrum(Brain):
    def __init__(self):
        super().__init__()
        self.name = 'Cerebrum'
        self.functions = ['thinking', 'sensation', 'movement']
    
    def describe(self):
        return (f'{self.name} is responsible for {", ".join(self.functions)}')
    
class Cerebellum(Brain):
    def __init__(self):
        super().__init__()
        self.name = 'Cerebellum'
        self.functions = ['coordination', 'balance', 'motor control']
    
    def describe(self):
        return (f'{self.name} is responsible for {", ".join(self.functions)}')
    
class Brainstem(Brain):
    def __init__(self):
        super().__init__()
        self.name = 'Brainstem'
        self.functions = ['breating', 'heart rate', 'sleep']
    
    def describe(self):
        return (f'{self.name} controls basic life functions like {", ".join(self.functions)}')

if __name__ == "__main__":
    brain = Brain()
    cerebrum = Cerebrum()
    cerebellum = Cerebellum()
    brainstem = Brainstem()

    brain.add_region(cerebrum)
    brain.add_region(cerebellum)
    brain.add_region(brainstem)

    print(brain.describe())
    print(cerebrum.describe())
    print(cerebellum.describe())
    print(brainstem.describe())
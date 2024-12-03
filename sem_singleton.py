class Config:
    def __init__(self):
        self.settings = {}

    def set_config(self, key, value):
        self.settings[key] = value

    def get_config(self, key):
        return self.settings.get(key)


# Testando
if __name__ == "__main__":
    config1 = Config()
    config1.set_config("theme", "dark")

    config2 = Config()
    print("Config 2 Theme:", config2.get_config("theme"))  
    print("Config 1 é igual ao Config 2?", config1 is config2)  

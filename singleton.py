class SingletonConfig:
    _instance = None  

    def __new__(cls, *args, **kwargs):
        if not cls._instance:  
            cls._instance = super().__new__(cls, *args, **kwargs)
            cls._instance.settings = {}  
        return cls._instance

    def set_config(self, key, value):
        self.settings[key] = value

    def get_config(self, key):
        return self.settings.get(key)


# Testando
if __name__ == "__main__":
    config1 = SingletonConfig()
    config1.set_config("theme", "dark")

    config2 = SingletonConfig()
    print("Config 2 Theme:", config2.get_config("theme"))  
    print("Config 1 é igual ao Config 2?", config1 is config2)  

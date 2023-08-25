class Group:
    def __init__(self, object_type):
        self.objects = []
        self.object_type = object_type

    def add(self, *args):
        for arg in args:
            if type(arg) is not self.object_type:
                raise TypeError(f"Incorrect object type: {type(arg)} for {self}")
        self.objects.append(*args)

    def __str__(self):
        return f"Group(Length: {len(self.objects)}, Type: {self.object_type})"

    def execute_objects_func(self, func_name, args=tuple(), kwargs=None):
        if kwargs is None:
            kwargs = dict()
        for obj in self.objects:
            obj.__getattribute__(func_name)(*args, **kwargs)

    def __getitem__(self, item: int):
        return self.objects[item]

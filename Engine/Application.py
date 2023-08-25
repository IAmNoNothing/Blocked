import pygame as pg


from Engine.GameObjects.Groups.Group import Group


class Application:
    def __init__(self):
        from Engine.GameObjects.Label import Label
        from Engine.GameObjects.Block import Block

        pg.init()

        # objects
        self.clock = pg.time.Clock()
        self.screen = pg.display.set_mode((800, 600), pg.RESIZABLE)

        self.Label = Label
        self.Block = Block

        # variables
        self.running = True
        self.dt = 0
        self.fps = 0

        # data structures
        self.pre_run_tasks = Group(callable)
        self.fonts = {}

        self.allowed_game_objects = (self.Label, self.Block)

        # game objects
        self.labels = Group(self.Label)
        self.blocks = Group(Group)

    def draw(self):
        self.screen.fill((255, 255, 255))

        self.labels.execute_objects_func('draw')
        self.blocks.execute_objects_func('execute_objects_func', args=('draw',))

    def check_events(self):
        for event in pg.event.get():
            # exit
            if event.type == pg.QUIT:
                self.running = False

    def input(self):
        pass

    def update(self):
        self.dt = self.clock.tick()
        self.fps = self.clock.get_fps()
        pg.display.update()

    def execute_pre_run_tasks(self):
        pg.display.set_caption("Blocked")

        self.add_game_object(self.Label(self, "1234567890", 30, collider=self.Label.AutoCollider, color=(0, 0, 0),
                                        font_name='RobotoCondensed-Regular'))
        self.pre_run_tasks.execute_objects_func('__call__')

    def run(self):
        self.execute_pre_run_tasks()
        while self.running:
            self.check_events()
            self.input()
            self.draw()
            self.update()

    def add_pre_run_task(self, task: callable):
        self.pre_run_tasks.add(task)

    def get_font(self, font_name: str, font_size: int) -> pg.font.Font:

        if (font_name, font_size) in [(_font.name, _font.size) for _font in self.fonts.values()]:
            return self.fonts[(font_name, font_size)]
        try:
            if font_name is not None:
                self.fonts.update({(font_name, font_size): pg.font.Font(f'Assets/Fonts/{font_name}.ttf', font_size)})
            else:
                self.fonts.update({(font_name, font_size): pg.font.Font(None, font_size)})
            return tuple(self.fonts.values())[-1]
        except FileNotFoundError:
            raise FileNotFoundError(f"No font \"{font_name}\" in ./Assets/Fonts")

    def add_game_object(self, obj):
        match type(obj):
            case self.Label:
                self.labels.add(obj)

from PIL import Image, ImageTk
import pygame

class Player:
    def __init__(self, canvas, x, y, jump_sound, coin_sound):
        self.canvas = canvas
        self.image = ImageTk.PhotoImage(Image.open("assets/images/mario.png"))
        self.id = self.canvas.create_image(x, y, anchor='nw', image=self.image)
        
        self.jump_sound = jump_sound
        self.coin_sound = coin_sound
        self.fall_sound = pygame.mixer.Sound("assets/sounds/fall.wav")

        self.vx = 0
        self.vy = 0
        self.on_ground = False
        self.last_y = y  
        self.falling_from_platform = False  
        self.width = self.image.width()
        self.height = self.image.height()

    def on_key_press(self, event):
        if event.keysym == 'Left':
            self.vx = -5
        elif event.keysym == 'Right':
            self.vx = 5
        elif event.keysym == 'Up' and self.on_ground:
            self.vy = -15
            if self.jump_sound:
                self.jump_sound.play()
            self.on_ground = False

    def on_key_release(self, event):
        if event.keysym in ['Left', 'Right']:
            self.vx = 0

    def update(self, platforms):
        self.vy += 1 
        self.canvas.move(self.id, self.vx, self.vy)
        
        coords = self.canvas.coords(self.id)
        if coords[1] + self.height >= 600:
            self.on_ground = True
            self.vy = 0
            self.canvas.coords(self.id, coords[0], 600 - self.height)
            if coords[1] > self.last_y:
                self.falling_from_platform = True
            else:
                self.falling_from_platform = False
            self.last_y = coords[1]
        else:
            self.on_ground = False
            self.falling_from_platform = False

        for platform in platforms:
            if self.collides_with(platform):
                self.on_ground = True
                self.vy = 0
                self.canvas.coords(self.id, coords[0], platform.coords[1] - self.height)
                if not platform.coin_collected:
                    platform.collect_coin()
                    if self.coin_sound:
                        self.coin_sound.play()

        if self.falling_from_platform:
            self.fall_sound.play()

    def collides_with(self, platform):
        coords = self.canvas.coords(self.id)
        return (coords[0] + self.width > platform.coords[0] and
                coords[0] < platform.coords[0] + platform.image.width() and
                coords[1] + self.height > platform.coords[1] and
                coords[1] < platform.coords[1] + platform.image.height())

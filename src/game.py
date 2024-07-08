import tkinter as tk
from PIL import Image, ImageTk
import os
import pygame
from player import Player
from platform import Platform



class Game:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Super Mario Clone")
        
        self.canvas = tk.Canvas(self.root, width=800, height=600)
        self.canvas.pack()

        pygame.mixer.init()

        self.assets_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'assets'))

        background_path = os.path.join(self.assets_dir, "images", "background.png")
        self.background_image = Image.open(background_path)
        self.bg_width, self.bg_height = self.background_image.size
        self.background_image_tk = ImageTk.PhotoImage(self.background_image)

        for i in range(0, 800, self.bg_width):
            for j in range(0, 600, self.bg_height):
                self.canvas.create_image(i, j, anchor=tk.NW, image=self.background_image_tk)

        jump_sound_path = os.path.join(self.assets_dir, "sounds", "jump.wav")
        if os.path.exists(jump_sound_path):
            self.jump_sound = pygame.mixer.Sound(jump_sound_path)
        else:
            print(f"Erreur : '{jump_sound_path}' introuvable.")
            self.jump_sound = None

        coin_sound_path = os.path.join(self.assets_dir, "sounds", "coin.wav")
        if os.path.exists(coin_sound_path):
            self.coin_sound = pygame.mixer.Sound(coin_sound_path)
        else:
            print(f"Erreur : '{coin_sound_path}' introuvable.")
            self.coin_sound = None

        self.player = Player(self.canvas, 100, 550, self.jump_sound, self.coin_sound)
        self.player.start_sound = pygame.mixer.Sound(os.path.join(self.assets_dir, "sounds", "start.wav"))

        self.platforms = [
            Platform(self.canvas, 50, 500),
            Platform(self.canvas, 150, 400),
            Platform(self.canvas, 300, 300),
            Platform(self.canvas, 450, 200),
            Platform(self.canvas, 600, 100)
        ]

        for platform in self.platforms:
            platform.create_coin()

        self.running = False
        self.coins_collected = 0
        self.total_coins = sum(1 for platform in self.platforms if platform.has_coin())

        self.end_sound_played = False

    def run(self):
        self.player.start_sound.play()
        self.root.bind("<KeyPress>", self.on_key_press)
        self.root.bind("<KeyRelease>", self.on_key_release)
        self.update()
        self.root.mainloop()

    def on_key_press(self, event):
        self.player.on_key_press(event)

    def on_key_release(self, event):
        self.player.on_key_release(event)

    def update(self):
        if not self.running:
            self.running = True
        if self.running:
            self.player.update(self.platforms)
            self.check_coins_collected()
            self.root.after(16, self.update)

    def check_coins_collected(self):
        coins = sum(1 for platform in self.platforms if not platform.has_coin())
        if coins == self.total_coins and not self.end_sound_played:
            self.running = False
            self.player.start_sound.stop()
            pygame.mixer.Sound(os.path.join(self.assets_dir, "sounds", "end.wav")).play()
            self.show_level_complete_message()
            self.end_sound_played = True

    def show_level_complete_message(self):
        message = "You Win!"
        colors = ["red", "blue", "yellow", "blue", "green", "indigo", "violet"]
        x_start = 320
        y_start = 200

        offsets = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for dx, dy in offsets:
            for index, char in enumerate(message):
                self.canvas.create_text(
                    x_start + index * 20 + dx, 
                    y_start + dy, 
                    text=char, 
                    font=("Comic Sans MS", 30, "bold"), 
                    fill="black"
                )

        for index, char in enumerate(message):
            color = colors[index % len(colors)]
            self.canvas.create_text(
                x_start + index * 20, 
                y_start, 
                text=char, 
                font=("Comic Sans MS", 30, "bold"), 
                fill=color
            )

        mariowin_image_path = os.path.join(self.assets_dir, "images", "mariowin.png")
        mariowin_image = Image.open(mariowin_image_path)

        aspect_ratio = mariowin_image.height / mariowin_image.width
        mariowin_image = mariowin_image.resize((300, int(300 * aspect_ratio)), Image.LANCZOS)
        mariowin_image_tk = ImageTk.PhotoImage(mariowin_image)

        self.canvas.create_image(400, 400, anchor=tk.CENTER, image=mariowin_image_tk)
        self.mariowin_image_tk = mariowin_image_tk 

if __name__ == "__main__":
    game = Game()
    game.run()

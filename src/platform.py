from PIL import Image, ImageTk



class Platform:
    def __init__(self, canvas, x, y):
        self.canvas = canvas
        self.image = ImageTk.PhotoImage(Image.open("assets/images/block.png"))
        self.id = self.canvas.create_image(x, y, anchor='nw', image=self.image)
        self.coin_image = ImageTk.PhotoImage(Image.open("assets/images/coin.png"))
        self.coin_id = None
        self.coin_collected = False

    def create_coin(self):
        if not self.coin_collected:
            self.coin_id = self.canvas.create_image(self.coords[0] + 25, self.coords[1] - 25, anchor="nw", image=self.coin_image)

    def collect_coin(self):
        if not self.coin_collected:
            self.coin_collected = True
            if self.coin_id:
                self.canvas.delete(self.coin_id)

    @property
    def coords(self):
        return self.canvas.coords(self.id)

    def has_coin(self):
        return not self.coin_collected

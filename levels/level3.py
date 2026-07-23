text = '''Hey Jack,

What's up?

My flight from Philadelphia 
is running a bit late, so I
thought you would be able 
to pick some things up from 
the supermarket.

We're running low on 
chocolate milk, and I'd 
like some bagels and cheese 
for breakfast.

Also, grab me detergent on 
your way.

Thanks, I'll keep in touch 
with you later.

'''

itemsLevel3 = ["Chocolate Milk", "Bagels", "Cheese", "Detergent"]
#itemsLevel3 = []

def level3(screen, font):
    text_surface = font.render(text, True, (255, 255, 255))
    text_rect = text_surface.get_rect(topleft=(20, 50))
    screen.blit(text_surface, text_rect)
text = '''Hi dear, 

I'll be home a bit late 
tonight, so I was hoping 
you could help me 
pick up a few things.

We're almost out of milk, 
and I'd like some bread 
loafs for sandwiches.

Also, please grab a dozen 
eggs and some red apples 
for your brother.

Thanks a lot! 
You're the best'''

#Code for each level is basically the same. Read level1 for exlanation.
itemsLevel2 = ["Milk", "Bread Loafs", "Eggs", "Red Apples"]
#itemsLevel2 = []

def level2(screen, font):
    text_surface = font.render(text, True, (255, 255, 255))
    text_rect = text_surface.get_rect(topleft=(20, 50))
    screen.blit(text_surface, text_rect)

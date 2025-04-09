def box(event):
    yaxis(event)
    canvas.create_rectangle(x1, y1, x2, y2)

    picture = PhotoImage(width=(x2-x1), height=(y2-y1))
    for x in range(x1, x2):
        for y in range(y1, y2):
            r, g, b = photo.get(x, y)
            picture.put("#%02x%02x%02x" % (r, g, b), (x-x1, y-y1))
    picture.write('new_image.gif', format='gif')
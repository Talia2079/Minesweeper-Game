import random  
from tkinter import * 
from cell import Cell  
import setting 
import utils
 
root = Tk()
# Override the setting of the window
root.configure(bg="black")
root.geometry(f'{setting.WIDTH}X{setting.HEIGHT}') 
root.title("Minesweeper Game") 
root.resizable(False,False) 
 
top_frame = Frame( 
      root,
      bg= 'black',
      width=setting.WIDTH,
      height=utils.height_prct(25) 
      )
top_frame.place(x=0, y=0)
      
game_title = Label( 
      top_frame, 
      bg='black',
      fg='white', 
      text="Minesweeper",
      font=("", 40) 
      ) 
game_title.place( 
       x=utils.width_pret(25), y=0
    )
 
left_frame = Frame(
      root, 
      bg ='black', 
      width=utils.width_pret(25), 
      height=utils.height_pret(75)
)
left_frame.place(x=0, y=utils.height_pret(25)) 

center_frame = Frame(
      root, 
      bg='black' , 
      width=utils.width_pret(75),
      height=utils.height_pret(75)
)  
center_frame.place(
      x=utils.width_pret(25), 
      y=utils.height_pret(25),
)
 
# btn1 = Button(              
#      center_frame,
#      bg='blue' 
#      text='First Button'
#) 
# btn1.place(x=0, y=0)
 
# c1 = Cell()
#c1.create_btn_object(center_frame) 
#c1.cell_btn_object.place( 
#     x=0, y=0
#) 

#c2 = Cell()
#c2.create_btn_object(center_frame)
#c2.cell_btn_object.place(
#     x=40, y=0
#)
  
# Create cells
for x in range(setting.GRID_SIZE): 
    for y in range(setting.GRID_SIZE): 
        c=Cell(x, y) 
        c.create_btn_object(center_frame) 
        c.cell_btn_object.grid( 
          column=x, row=y 
        )
         
# Call the label from the Cell class 
Cell.cell_count_label_object.place( x=0, y=0)
  
# Randomize mines 
Cell.randomize_mines()
# Run the window
root.mainloop()
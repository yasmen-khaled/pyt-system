import tkinter
import tkinter.messagebox
import customtkinter
import subprocess
import customtkinter as ctk


class App(customtkinter.CTk):
    # ...

    def sidebar_button_1(root):
        subprocess.run(["python3", "crud.py"], check=True)

    def sidebar_button_2(root):
        subprocess.run(["python3", "master.py"], check=True)


customtkinter.set_appearance_mode("light") 
customtkinter.set_default_color_theme("dark-blue")  
class App(customtkinter.CTk):
    def __init__(root):
        super().__init__()

        # configure window
        root.title("Contract")
        root.geometry(f"{1100}x{580}")

        # configure grid layout (4x4)
        root.grid_columnconfigure(1, weight=1)  # Sidebar column
        root.grid_columnconfigure(1, weight=3)  # Main content column
        root.grid_rowconfigure(0, weight=1)  # Row for the form

        # create sidebar frame with widgets
        root.sidebar_frame = ctk.CTkFrame(root, width=200, corner_radius=0)
        root.sidebar_frame.grid(row=0, column=0, sticky="ns")


        root.sidebar_frame.grid_rowconfigure(6, weight=1)
        root.logo_label = customtkinter.CTkLabel(root.sidebar_frame, text="Dash", font=customtkinter.CTkFont(size=20, weight="bold"))
        root.sidebar_button_1 = customtkinter.CTkButton(root.sidebar_frame, text="Employees", command=root.sidebar_button_event)
        root.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)

        root.sidebar_button_2 = customtkinter.CTkButton(root.sidebar_frame, text="Master", command=root.sidebar_button_event)
        root.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)

        root.sidebar_button_3 = customtkinter.CTkButton(root.sidebar_frame, text="Bachelor's", command=root.sidebar_button_event)
        root.sidebar_button_3.grid(row=3, column=0, padx=20, pady=10)

        root.sidebar_button_4 = customtkinter.CTkButton(root.sidebar_frame, text="Ph.D", command=root.sidebar_button_event)
        root.sidebar_button_4.grid(row=4, column=0, padx=20, pady=10)

        root.sidebar_button_5 = customtkinter.CTkButton(root.sidebar_frame, text="Contract", command=root.sidebar_button_event)
        root.sidebar_button_5.grid(row=5, column=0, padx=20, pady=10)



        root.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(root.sidebar_frame, values=["Light", "Dark", "System"],
                                                                       command=root.change_appearance_mode_event)
        
        root.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10,  10))
        root.scaling_label = customtkinter.CTkLabel(root.sidebar_frame, text="UI Scaling:", anchor="w")
        root.scaling_label.grid(row=7, column=0, padx=20, pady=(10,  0))
        root.scaling_optionemenu = customtkinter.CTkOptionMenu(root.sidebar_frame, values=["100%" , "120%"],
                                                               command=root.change_scaling_event)
        root.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10,  20))





        root.main_content_frame = ctk.CTkFrame(root)
        root.main_content_frame.grid(row=0, column=1, sticky="nsew")
                                     
        #ده امبر الفورم  الا تيقيتي

    
        # Create input text boxes
        root.input_label_1 = ctk.CTkLabel(root.main_content_frame, text="Input   1")
        root.input_label_1.grid(row=0, column=0, padx=5, pady=5, sticky="ew")
        root.input_box_1 = ctk.CTkEntry(root.main_content_frame, placeholder_text="Input   1")
        root.input_box_1.grid(row=1, column=0, padx=5, pady=5, sticky="ew")


        root.input_label_2 = ctk.CTkLabel(root.main_content_frame, text="Input   2")
        root.input_label_2.grid(row=0, column=0, padx=5, pady=5, sticky="ew")
        root.input_box_2 = ctk.CTkEntry(root.main_content_frame, placeholder_text="Input   2")
        root.input_box_2.grid(row=1, column=1, padx=5, pady=5, sticky="ew")


        root.input_label_3 = ctk.CTkLabel(root.main_content_frame, text="Input   3")
        root.input_label_3.grid(row=0, column=0, padx=5, pady=5, sticky="ew")
        root.input_box_3 = ctk.CTkEntry(root.main_content_frame, placeholder_text="Input   3")
        root.input_box_3.grid(row=1, column=2, padx=5, pady=5, sticky="ew")



        root.input_label_4 = ctk.CTkLabel(root.main_content_frame, text="Input   4")
        root.input_label_4.grid(row=0, column=0, padx=5, pady=5, sticky="ew")
        root.input_box_4 = ctk.CTkEntry(root.main_content_frame, placeholder_text="Input   4")
        root.input_box_4.grid(row=1, column=3, padx=5, pady=5, sticky="ew")



        root.input_label_5 = ctk.CTkLabel(root.main_content_frame, text="Input   5")
        root.input_label_5.grid(row=0, column=0, padx=5, pady=5, sticky="ew")
        root.input_box_5 = ctk.CTkEntry(root.main_content_frame, placeholder_text="Input   5")
        root.input_box_5.grid(row=2, column=0, padx=5, pady=5, sticky="ew")



        # ... Repeat for the rest of the input boxes ...

        # Create buttons
        root.add_button = ctk.CTkButton(root.main_content_frame, text="Add", command=root.add_event)
        root.add_button.grid(row=9, column=2, padx=5, pady=5, sticky="ew")

        root.update_button = ctk.CTkButton(root.main_content_frame, text="Update", command=root.update_event)
        root.update_button.grid(row=9, column=3, padx=5, pady=5, sticky="ew")

        root.delete_button = ctk.CTkButton(root.main_content_frame, text="Delete", command=root.delete_event)
        root.delete_button.grid(row=10, column=2, columnspan=2, padx=5, pady=5, sticky="ew")





        # Remove all other widgets
        #for widget in root.winfo_children():
            #if widget != root.sidebar_frame:
                #widget.destroy()












    def open_input_dialog_event(root):
        dialog = customtkinter.CTkInputDialog(text="Type in a number:", title="CTkInputDialog")
        print("CTkInputDialog:", dialog.get_input())

    def change_appearance_mode_event(root, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(root, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) /  100
        customtkinter.set_widget_scaling(new_scaling_float)

    def sidebar_button_event(root):
        print("sidebar_button click")


    def add_event(root):
        # Implement add functionality here
        pass

    def update_event(root):
        # Implement update functionality here
        pass

    def delete_event(root):
        # Implement delete functionality here
        pass


        

if __name__ == "__main__":  
    app = App()
    app.mainloop()

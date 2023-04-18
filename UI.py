import tkinter as tk
import json

class UserForm(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Suppression Information")
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.customer_id = tk.Label(self, text="CustomerID:")
        self.customer_id.pack()
        self.customer_id_entry = tk.Entry(self)
        self.customer_id_entry.pack()

        self.channel_label = tk.Label(self, text="Channel:")
        self.channel_label.pack()
        self.channel_entry = tk.Entry(self)
        self.channel_entry.pack()

        self.subchannel_label = tk.Label(self, text="SubChannel:")
        self.subchannel_label.pack()
        self.subchannel_entry = tk.Entry(self)
        self.subchannel_entry.pack()

        self.user_role_label = tk.Label(self, text="userRole:")
        self.user_role_label.pack()
        self.user_role_entry = tk.Entry(self)
        self.user_role_entry.pack()

        self.org_level_label = tk.Label(self, text="orgLevel:")
        self.org_level_label.pack()
        self.org_level_entry = tk.Entry(self)
        self.org_level_entry.pack()

        self.supp_day_label = tk.Label(self, text="Suppression Day:")
        self.supp_day_label.pack()
        self.supp_day_entry = tk.Entry(self)
        self.supp_day_entry.pack()

        self.submit_button = tk.Button(self, text="Save", command=self.save_user)
        self.submit_button.pack()

    def save_user(self):
        user = {
            "name": self.name_entry.get(),
            "surname": self.surname_entry.get(),
            "age": self.age_entry.get()
        }
        with open("user.json", "w") as f:
            json.dump(user, f)
        self.master.destroy()

root = tk.Tk()
app = UserForm(master=root)
app.mainloop()

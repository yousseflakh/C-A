import customtkinter as ctk
from tkinter import messagebox
from PIL import Image # ضروري تزيد هاد السطر لفوق كاع


class LoveApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # ... (نفس الإعدادات السابقة)
        self.title("Wach Katbghini?")
        self.geometry("500x650")
        ctk.set_appearance_mode("light") 
        self.configure(fg_color="#FCE4EC")

        self.step = 1

        self.label_pov = ctk.CTkLabel(self, text="jawbi bsara7a 💖👀", 
                                      font=("Arial", 22, "bold"), text_color="#880E4F")
        self.label_pov.pack(pady=30)
      
        real_path = r"C:\Users\youss\OneDrive\Desktop\images.png" # <--- ديري Ctrl+V هنا
        
        self.my_image = ctk.CTkImage(light_image=Image.open(real_path),
                                     
                                     size=(150, 150))
        
       
        # ------------------
       
        
       
        # 2. كتعرضها فـ Label بلاصة الـ Canvas
        self.image_label = ctk.CTkLabel(self, image=self.my_image, text="")
        self.image_label.pack(pady=10)
        # ---------------------------------

        # ... (باقي الكود كيبقى كيفما هو)

        # السؤال
        self.question_label = ctk.CTkLabel(self, text="Wach Katbghinii?", 
                                           font=("Arial", 20, "bold"), text_color="#AD1457")
        self.question_label.pack(pady=20)

        # إطار الأزرار
        self.button_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.button_frame.pack(pady=20)

        self.btn_ah = ctk.CTkButton(self.button_frame, text="AH", width=100, height=45,
                                    fg_color="#D81B60", hover_color="#AD1457",
                                    command=self.process_ah)
        self.btn_ah.grid(row=0, column=0, padx=20)

        self.btn_la = ctk.CTkButton(self.button_frame, text="LA", width=100, height=45,
                                    fg_color="white", text_color="#D81B60", border_width=2,
                                    border_color="#D81B60", hover_color="#F8BBD0",
                                    command=self.process_la)
        self.btn_la.grid(row=0, column=1, padx=20)

    def process_la(self):
        real_path = r"C:\Users\youss\OneDrive\Desktop\WhatsApp Image 2026-03-27 at 23.19.14.jpeg" # <--- ديري Ctrl+V هنا
        
        self.my_image = ctk.CTkImage(light_image=Image.open(real_path),
                                     
                                     size=(150, 150))
        if self.step == 1:
            self.question_label.configure(text="Wach mat2akdaaa? 🤔")
            self.btn_ah = ctk.CTkButton(self.button_frame, text="AH", width=120, height=50,
                                    fg_color="#D81B60", hover_color="#AD1457",
                                    command=self.process_ah)
            self.btn_ah.grid(row=0, column=0, padx=20)
            self.step = 2
        elif self.step == 2:
            self.question_label.configure(text="Takdi? 😱")
            self.btn_ah = ctk.CTkButton(self.button_frame, text="AH", width=130, height=55,
                                    fg_color="#D81B60", hover_color="#AD1457",
                                    command=self.process_ah)
            self.btn_ah.grid(row=0, column=0, padx=20)
            self.step = 3
        elif self.step == 3 :
            self.question_label.configure(text="chofi wkan? 😱") 
            self.btn_ah = ctk.CTkButton(self.button_frame, text="AH", width=160, height=65,
                                    fg_color="#D81B60", hover_color="#AD1457",
                                    command=self.process_ah)
            self.step = 4
        elif self.step == 4 :
            self.question_label.configure(text="rah anskhaaff \n takdi? 😱")
            self.btn_ah = ctk.CTkButton(self.button_frame, text="AH", width=170, height=75,
                                    fg_color="#D81B60", hover_color="#AD1457",
                                    command=self.process_ah)
            self.step = 5
            
        elif self.step == 5 :
            self.show_final_result("Hchoma 3lik  \n Sf 9l9tini 😢💔")
    def process_ah(self):
            self.step = 1
            self.show_final_result("knt 3arfha! Hta ana kanbghik! ❤️✨")
        

    def show_final_result(self, message):
        # كتمحي الأزرار وكتعرض النتيجة
        self.button_frame.destroy()
        self.question_label.configure(text=message, font=("Arial", 22, "bold"))
        self.label_pov.configure(text="The End! ✨")

if __name__ == "__main__":
    app = LoveApp()
    app.mainloop()
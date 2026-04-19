import customtkinter as ctk
from tkinter import messagebox
from models.salle import Salle
from services.services_salle import ServiceSalle

class ViewSalle(ctk.CTk):

    def __init__(self):
        super().__init__()
        self.title("Gestion des Salles")
        self.service_salle = ServiceSalle()
        self._build_info_frame()
        self._build_action_frame()

    def _build_info_frame(self):
        self.cadreInfo = ctk.CTkFrame(self, corner_radius=10)
        self.cadreInfo.pack(pady=10, padx=10)

        ctk.CTkLabel(self.cadreInfo, text="Code :").grid(row=0, column=0, padx=5, pady=5)
        self.entry_code = ctk.CTkEntry(self.cadreInfo)
        self.entry_code.grid(row=0, column=1, padx=5, pady=5)

        ctk.CTkLabel(self.cadreInfo, text="Description :").grid(row=1, column=0, padx=5, pady=5)
        self.entry_desc = ctk.CTkEntry(self.cadreInfo)
        self.entry_desc.grid(row=1, column=1, padx=5, pady=5)

        ctk.CTkLabel(self.cadreInfo, text="Catégorie :").grid(row=2, column=0, padx=5, pady=5)
        self.entry_cat = ctk.CTkEntry(self.cadreInfo)
        self.entry_cat.grid(row=2, column=1, padx=5, pady=5)

        ctk.CTkLabel(self.cadreInfo, text="Capacité :").grid(row=3, column=0, padx=5, pady=5)
        self.entry_cap = ctk.CTkEntry(self.cadreInfo)
        self.entry_cap.grid(row=3, column=1, padx=5, pady=5)

    def _build_action_frame(self):
        self.cadreActions = ctk.CTkFrame(self, corner_radius=10)
        self.cadreActions.pack(pady=10, padx=10)

        ctk.CTkButton(self.cadreActions, text="Ajouter",    command=self.ajouter_salle).grid(row=0, column=0, padx=5)
        ctk.CTkButton(self.cadreActions, text="Modifier",   command=self.modifier_salle).grid(row=0, column=1, padx=5)
        ctk.CTkButton(self.cadreActions, text="Supprimer",  command=self.supprimer_salle).grid(row=0, column=2, padx=5)
        ctk.CTkButton(self.cadreActions, text="Rechercher", command=self.rechercher_salle).grid(row=0, column=3, padx=5)

    def ajouter_salle(self):
        s = Salle(self.entry_code.get(), self.entry_desc.get(),
                  self.entry_cat.get(), int(self.entry_cap.get() or 0))
        ok, msg = self.service_salle.ajouter_salle(s)
        messagebox.showinfo("Info", msg)
        self.lister_salles()

    def modifier_salle(self):
        s = Salle(self.entry_code.get(), self.entry_desc.get(),
                  self.entry_cat.get(), int(self.entry_cap.get() or 0))
        ok, msg = self.service_salle.modifier_salle(s)
        messagebox.showinfo("Info", msg)
        self.lister_salles()

    def supprimer_salle(self):
        self.service_salle.supprimer_salle(self.entry_code.get())
        messagebox.showinfo("Info", "Salle supprimée.")
        self.lister_salles()

    def rechercher_salle(self):
        s = self.service_salle.rechercher_salle(self.entry_code.get())
        if s:
            self.entry_desc.delete(0, "end"); self.entry_desc.insert(0, s.description)
            self.entry_cat.delete(0, "end");  self.entry_cat.insert(0, s.categorie)
            self.entry_cap.delete(0, "end");  self.entry_cap.insert(0, s.capacite)
        else:
            messagebox.showwarning("Avertissement", "Salle introuvable.")
from classes import *
import customtkinter as ctk
from tkinter import ttk, messagebox

class AdCampaignApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Gestion des Publicités en Ligne")
        self.geometry("1024x600")

        # List to store campaigns
        self.campaigns = []

        # Input Fields
        self.label_name = ctk.CTkLabel(self, text="Nom de la Campagne:")
        self.label_name.grid(row=0, column=0, padx=10, pady=10)
        self.entry_name = ctk.CTkEntry(self)
        self.entry_name.grid(row=0, column=1, padx=10, pady=10)

        self.label_budget = ctk.CTkLabel(self, text="Budget (€):")
        self.label_budget.grid(row=1, column=0, padx=10, pady=10)
        self.entry_budget = ctk.CTkEntry(self)
        self.entry_budget.grid(row=1, column=1, padx=10, pady=10)

        self.label_type = ctk.CTkLabel(self, text="Type de Publicité:")
        self.label_type.grid(row=2, column=0, padx=10, pady=10)
        self.ad_types = ["Google Ads", "Facebook Ads", "YouTube Ads", "Influenceurs"]
        self.combo_type = ctk.CTkComboBox(self, values=self.ad_types)
        self.combo_type.grid(row=2, column=1, padx=10, pady=10)

        # Buttons
        self.button_add = ctk.CTkButton(self, text="Ajouter", command=self.add_campaign)
        self.button_add.grid(row=3, column=0, padx=10, pady=10)

        self.button_delete = ctk.CTkButton(self, text="Supprimer", command=self.delete_campaign)
        self.button_delete.grid(row=3, column=1, padx=10, pady=10)

        self.button_modify = ctk.CTkButton(self, text="Modifier", command=self.modify_campaign)
        self.button_modify.grid(row=3, column=2, padx=10, pady=10)

        # Treeview to display campaigns
        self.tree = ttk.Treeview(self, columns=("Nom", "Budget", "Canal", "Type", "Portée"), show="headings")
        self.tree.heading("Nom", text="Nom")
        self.tree.heading("Budget", text="Budget (€)")
        self.tree.heading("Canal", text="Canal")
        self.tree.heading("Type", text="Type")
        self.tree.heading("Portée", text="Portée Estimée")
        self.tree.grid(row=4, column=0, columnspan=3, padx=10, pady=10)

    # Add Campaign
    def add_campaign(self):
        try:
            nom = self.entry_name.get()
            budget = float(self.entry_budget.get())
            canal = "Réseaux sociaux"  # Default channel
            ad_type = self.combo_type.get()

            if budget <= 0:
                raise InvalidBudgetError()

            if ad_type == "Google Ads":
                campaign = GoogleAdsCampaign(nom, budget, canal, cpc=2.5)  # Example CPC
            elif ad_type == "Facebook Ads":
                campaign = FacebookAdsCampaign(nom, budget, canal, cpm=5.0)  # Example CPM
            elif ad_type == "YouTube Ads":
                campaign = YoutubeAdsCampaign(nom, budget, canal, cpv=0.1)  # Example CPV
            elif ad_type == "Influenceurs":
                campaign = InfluencersCampaign(nom, budget, canal, cpe=0.5)  # Example CPE

            self.campaigns.append(campaign)
            self.update_treeview()
        except InvalidBudgetError:
            messagebox.showerror("Erreur", "Le budget doit être positif.")
        except ValueError:
            messagebox.showerror("Erreur", "Veuillez entrer un budget valide.")

    # Delete Campaign
    def delete_campaign(self):
        selected_item = self.tree.selection()
        if selected_item:
            self.tree.delete(selected_item)

    # Modify Campaign
    def modify_campaign(self):
        selected_item = self.tree.selection()
        if selected_item:
            # Get selected campaign details
            item = self.tree.item(selected_item)
            campaign_name = item["values"][0]

            # Find the campaign in the list
            for campaign in self.campaigns:
                if campaign.nom == campaign_name:
                    new_budget = float(self.entry_budget.get())
                    if new_budget <= 0:
                        messagebox.showerror("Erreur", "Le budget doit être positif.")
                        return
                    campaign.budget = new_budget
                    self.update_treeview()
                    break

    # Update Treeview
    def update_treeview(self):
        self.tree.delete(*self.tree.get_children())
        for campaign in self.campaigns:
            self.tree.insert("", "end", values=(
                campaign.nom,
                f"{campaign.budget:.2f}€",
                campaign.canal,
                campaign.__class__.__name__,
                f"{campaign.calculer_portee():.2f}"
            ))

# Run the Application
if __name__ == "__main__":
    app = AdCampaignApp()
    app.mainloop()
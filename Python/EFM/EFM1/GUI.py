import customtkinter as ctk
from tkinter import *
from tkinter import ttk, messagebox
from classes import *


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("1000x800")
        self.title("Ad Campaign Manager")
        self.background_color = "#1f1f1f"

        # frames creation
            # the main container
        frames_container = ctk.CTkFrame(self, width=980, height=400)
        frames_container.pack_propagate(False)
        frames_container.pack(pady=10)
        
        
            # container for the initial inputs
        inputs_frame = ctk.CTkFrame(frames_container, width=980, height=150, fg_color='transparent')
        inputs_frame.pack_propagate(False)
        
            # container frame for the additional inputs
        moreInputs = ctk.CTkFrame(frames_container, width=980, height=150, fg_color='transparent')
        moreInputs.pack_propagate(False)
        
            # container for the buttons
        btn_frame = ctk.CTkFrame(frames_container, width=980, height=100, fg_color='transparent')
        btn_frame.pack_propagate(False)
        
            # container for the tree view
        tv_frame = ctk.CTkFrame(self, width=980, height=300)
        
        # rendering the frames
        inputs_frame.pack(pady=10)
        moreInputs.pack(pady=10)
        btn_frame.pack(pady=0)
        tv_frame.pack(pady=10)
        
        
        
        # widget creation
        self.name_entry = ctk.CTkEntry(inputs_frame, placeholder_text="Ad campaign name", width=200)
        self.budget_entry = ctk.CTkEntry(inputs_frame, placeholder_text="Budget (€)", width=200)
        self.ad_select = ctk.CTkComboBox(inputs_frame, values=["select campaign type","Google Ads", "Facebook Ads", "Youtube Ads", "Influencers"], width=200, command=self.showMoreInputs)
        
        
        # the buttons
        self.add_btn = ctk.CTkButton(btn_frame, text="Add", width=200, command=self.addCampaign)
        self.update_btn = ctk.CTkButton(btn_frame, text="Update", width=200 ,fg_color='green')
        self.remove_btn = ctk.CTkButton(btn_frame, text="Remove", width=200,fg_color='red')
        
        
        # additional inputs that will be hidden away till a selection is made
         
            # the inputs
        self.cpm = ctk.CTkEntry(moreInputs, placeholder_text="CPM (€)", width=200)
        self.cpv = ctk.CTkEntry(moreInputs, placeholder_text="CPV (€)", width=200)
        self.cpc = ctk.CTkEntry(moreInputs, placeholder_text="CPC (€)", width=200)
        self.cpe = ctk.CTkEntry(moreInputs, placeholder_text="CPE (€)", width=200)
            # packing the inputs
        self.cpc.pack_forget()
        self.cpm.pack_forget()
        self.cpv.pack_forget()
        self.cpe.pack_forget()
        # rendering the widgets in the frames
        self.name_entry.pack(pady=10)
        self.budget_entry.pack(pady=10)
        self.ad_select.pack(pady=10)
        
        
        self.add_btn.grid(row=0, column=0, padx=10)
        self.update_btn.grid(row=0, column=1, padx=10)
        self.remove_btn.grid(row=0, column=2, padx=10)
        
        
        # tree view creation
        self.tv = ttk.Treeview(tv_frame, columns=('Ad campaign name', 'Budget', "Channel", "Campaign type", "Estimated revenue"), show='headings',)
        
        # the columns
        self.tv.column('Ad campaign name', width=200)
        self.tv.column('Budget', width=150)
        self.tv.column('Channel', width=150)
        self.tv.column('Campaign type', width=200)
        self.tv.column('Estimated revenue', width=200)
        
        
        
        self.tv.heading('Ad campaign name', text='Ad campaign name')
        self.tv.heading('Budget', text='Budget')
        self.tv.heading('Channel', text='Channel')
        self.tv.heading('Campaign type', text='Campaign type')
        self.tv.heading('Estimated revenue', text='Estimated revenue')
        
        self.tv.pack(fill=BOTH,expand=True)
        self.tv.bind("<<TreeviewSelect>>", self.on_select)
        self.campaigns = []
        
        
    # method to populate the treeview
    def fillTv(self):
        self.tv.delete(*self.tv.get_children())
        for campaign in self.campaigns:
            self.tv.insert("", "end", values=(campaign.nom, campaign.budget, campaign.canal, campaign.campaignType, campaign.estimatedRevenue))
        
        pass
    
    # method to show inputs for the extra options
    def showMoreInputs(self, value):
        if value == "Google Ads":
            self.cpc.pack()
            self.cpm.pack_forget()
            self.cpv.pack_forget()
            self.cpe.pack_forget()
            
        elif value == "Facebook Ads":
            self.cpm.pack()
            self.cpc.pack_forget()
            self.cpv.pack_forget()
            self.cpe.pack_forget()
            
        elif value == "Youtube Ads":
            self.cpv.pack()
            self.cpc.pack_forget()
            self.cpm.pack_forget()
            self.cpe.pack_forget()
        elif value == "Influencers":
            self.cpe.pack()
            self.cpv.pack_forget()
            self.cpc.pack_forget()
            self.cpm.pack_forget()
        elif value == 'select campaign type':
            self.cpc.pack_forget()
            self.cpm.pack_forget()
            self.cpv.pack_forget()
            self.cpe.pack_forget()
            
    
    def emptyInputs(self):
        self.name_entry.delete(0, END)
        self.budget_entry.delete(0, END)
        self.ad_select.set("select campaign type")
        self.cpc.delete(0, END)
        self.cpm.delete(0, END)
        self.cpv.delete(0, END)
    
    
    # method to add a new campaign
    def addCampaign(self):
        campaignName = self.name_entry.get()
        campaignBudget = self.budget_entry.get()
        campaignType = self.ad_select.get()
        cpc = self.cpc.get()
        cpm = self.cpm.get()
        cpv = self.cpv.get()
        cpe = self.cpe.get()
        if campaignName == "" or campaignBudget == "" or campaignType == "" or campaignType == "select campaign type":
            messagebox.showerror("Error", "Please fill in all the fields.")
            return
            
        elif campaignType == "Google Ads":
            self.campaigns.append(GoogleAdsCampaign(campaignName, campaignBudget, "Google Ads", cpc))
        elif campaignType == "Facebook Ads":
            self.campaigns.append(FacebookAdsCampaign(campaignName, campaignBudget, "Facebook Ads"), cpm)
        elif campaignType == "Youtube Ads":
            self.campaigns.append(YoutubeAdsCampaign(campaignName, campaignBudget, "Youtube Ads", cpv))
        elif campaignType == "Influencers":
            self.campaigns.append(InfluencersCampaign(campaignName, campaignBudget, "Influencers",cpe))
        
        # hiding the additional inputs
        self.cpc.pack_forget()
        self.cpm.pack_forget()
        self.cpv.pack_forget()
        
        self.emptyInputs()
        self.fillTv()
        
    
    
    
    # method to remove a campaign
    def removeCampaign (self):
        pass
    
    
    
    
    # method to update a campaign
    def updateCampaign (self):
        selected = self.tv.focus()
        values = self.tv.item(selected)
        if len(values["values"]) > 0:
            self.name_entry.insert(0, values["values"][0])
            self.budget_entry.insert(0, values["values"][1])
            self.ad_select.set(values["values"][2])
            self.cpc.insert(0, values["values"][3])
            self.cpm.insert(0, values["values"][4])
            self.cpv.insert(0, values["values"][5])
        
        
        



# starting the app
app = App()
app.mainloop()
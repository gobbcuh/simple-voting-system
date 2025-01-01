import tkinter as tk
from tkinter import messagebox

class VotingSystemGUI:
    def __init__(self, root):
        self.voters = {}
        self.parties = {}
        self.senatorial_candidates = []
        self.votes = {}
        self.senate_votes = {}

        self.root = root
        self.root.title("2025 Philippine Senate Election: Online Voting System")
        self.root.geometry("400x600")
        self.root.configure(bg="#29482b")
        self.create_main_menu()

    def create_main_menu(self):
        self.clear_frame()

        main_panel = tk.Frame(self.root, bg="#1e2d24", bd=2)
        main_panel.place(relx=0.5, rely=0.5, anchor="center", width=1500, height=500)

        tk.Label(main_panel, text="2025 PHILIPPINE\nSENATORIAL ELECTION", 
                 font=('Arial', 14, 'bold'), fg="white", bg="#1e2d24").pack(pady=(20, 5))
        tk.Label(main_panel, text="Karapatan ay Gamitin,\nBumoto para sa Isang Hangarin\n", 
                 font=('Arial', 10, 'bold'), fg="light gray", bg="#1e2d24").pack()

        button_style = {
            "font": ('Arial', 12),
            "bg": "#2c3e30",
            "fg": "white",
            "width": 25,
            "height": 2,
            "relief": "groove"
        }

        tk.Button(main_panel, text="Registration for Candidacy", command=self.register_candidacy_menu, **button_style).pack(pady=10)
        tk.Button(main_panel, text="Registration for Voting", command=self.register_voter_menu, **button_style).pack(pady=10)
        tk.Button(main_panel, text="Voting Menu", command=self.voting_menu, **button_style).pack(pady=10)
        tk.Button(main_panel, text="Quit", command=self.root.quit, **button_style).pack(pady=10)

        tk.Label(main_panel, text="A BRIGHTER FUTURE\nSTARTS WITH YOUR VOTE", 
                 font=('Arial', 10, 'bold'), fg="white", bg="#1e2d24").pack(pady=(20, 10))

    def register_candidacy_menu(self):
        self.clear_frame()
        
        container_frame = tk.Frame(self.root, bg="#2c3e30")
        container_frame.pack(expand=True) 

        tk.Label(container_frame, text="Candidacy Registration", font=('Arial', 13, 'bold'), fg="white", bg="#2c3e30", width=1500).pack(pady=18)
        tk.Button(container_frame, text="Register as Party List", command=self.register_party_list, width=25).pack(pady=10)
        tk.Button(container_frame, text="Register as Senator", command=self.register_senator, width=25).pack(pady=10)
        tk.Button(container_frame, text="Return to Main Menu", command=self.create_main_menu, width=25).pack(pady=10)

    def register_party_list(self):
        self.clear_frame()

        container_frame = tk.Frame(self.root, bg="#2c3e30")
        container_frame.pack(expand=True) 

        tk.Label(container_frame, text="Register a Party List", font=('Arial', 13, 'bold'), fg="white", bg="#2c3e30", width=1500).pack(pady=10)

        tk.Label(container_frame, text="Party List Name:").pack(pady=(5, 0))
        party_name_entry = tk.Entry(container_frame)
        party_name_entry.pack(pady=(0, 10))

        tk.Label(container_frame, text="Add Members:").pack(pady=(5, 0))

        member_entries = []
        for i in range(5): 
            member_entry = tk.Entry(container_frame)
            member_entry.pack(pady=2)
            member_entries.append(member_entry)

        def submit_party():
            party_name = party_name_entry.get()
            members = [entry.get() for entry in member_entries if entry.get().strip()]
            if not party_name or not members:
                messagebox.showerror("Error", "Please fill in the party name and members.")
                return
            self.parties[party_name] = members
            messagebox.showinfo("Success", f"Party '{party_name}' registered successfully!")
            self.create_main_menu()

        tk.Button(container_frame, text="Submit", command=submit_party).pack(pady=10)
        tk.Button(container_frame, text="Return to Main Menu", command=self.create_main_menu).pack(pady=10)

    def register_senator(self):
        self.clear_frame()

        container_frame = tk.Frame(self.root, bg="#2c3e30")
        container_frame.pack(expand=True)  

        tk.Label(container_frame, text="Register Senatorial Candidate", font=('Arial', 13, 'bold'), fg="white", bg="#2c3e30", width=1500).pack(pady=10)

        tk.Label(container_frame, text="Candidate Name:").pack(pady=(5, 0))
        candidate_entry = tk.Entry(container_frame)
        candidate_entry.pack(pady=(0, 10))

        def submit_senator():
            candidate_name = candidate_entry.get()
            if not candidate_name:
                messagebox.showerror("Error", "Candidate name cannot be empty.")
                return
            self.senatorial_candidates.append(candidate_name)
            messagebox.showinfo("Success", f"Candidate '{candidate_name}' registered successfully!")
            self.create_main_menu()

        tk.Button(container_frame, text="Submit", command=submit_senator).pack(pady=10)
        tk.Button(container_frame, text="Return to Main Menu", command=self.create_main_menu).pack(pady=10)

    def register_voter_menu(self):
        self.clear_frame()

        container_frame = tk.Frame(self.root, bg="#2c3e30")
        container_frame.pack(expand=True)  

        tk.Label(container_frame, text="Voter Registration", font=('Arial', 13, 'bold'), fg="white", bg="#2c3e30", width=1500).pack(pady=20)

        tk.Label(container_frame, text="Name:").pack(pady=(5, 0))
        name_entry = tk.Entry(container_frame)
        name_entry.pack(pady=(0, 10))

        tk.Label(container_frame, text="Age:").pack(pady=(5, 0))
        age_entry = tk.Entry(container_frame)
        age_entry.pack(pady=(0, 10))

        tk.Label(container_frame, text="Contact Number:").pack(pady=(5, 0))
        contact_entry = tk.Entry(container_frame)
        contact_entry.pack(pady=(0, 10))

        tk.Label(container_frame, text="Address:").pack(pady=(5, 0))
        address_entry = tk.Entry(container_frame)
        address_entry.pack(pady=(0, 10))

        def submit_voter():
            name = name_entry.get()
            age = age_entry.get()
            contact_number = contact_entry.get()
            address = address_entry.get()

            if not age.isdigit() or int(age) < 18:
                messagebox.showerror("Invalid", "Age must be a valid number and at least 18.")
                return

            self.voters[name] = {
                'age': int(age),
                'contact': contact_number,
                'address': address
            }

            messagebox.showinfo("Success", f"{name} is now registered as a voter!")
            self.create_main_menu()

        tk.Button(container_frame, text="Submit", command=submit_voter).pack(pady=10)
        tk.Button(container_frame, text="Return to Main Menu", command=self.create_main_menu).pack(pady=10)

    def voting_menu(self):
        self.clear_frame()

        container_frame = tk.Frame(self.root, bg="#2c3e30")
        container_frame.pack(expand=True)  

        tk.Label(container_frame, text="Voting Menu", font=('Arial', 13, 'bold'), fg="white", bg="#2c3e30", width=1500).pack(pady=20)

        tk.Button(container_frame, text="Vote", command=self.vote_initial, width=25).pack(pady=10)
        tk.Button(container_frame, text="Show Party List", command=self.show_parties, width=25).pack(pady=10)
        tk.Button(container_frame, text="Show Senatorial Candidates", command=self.show_senators, width=25).pack(pady=10)
        tk.Button(container_frame, text="Show Votes", command=self.show_votes, width=25).pack(pady=10)
        tk.Button(container_frame, text="Return to Main Menu", command=self.create_main_menu, width=25).pack(pady=10)

    def vote_initial(self):
        self.clear_frame()

        container_frame = tk.Frame(self.root, bg="#2c3e30")
        container_frame.place(relx=0.5, rely=0.5, anchor='center')

        tk.Label(container_frame, text="Voting", font=('Arial', 13, 'bold'), fg="white", bg="#2c3e30", width=1500).grid(row=0, column=0, pady=20)

        tk.Label(container_frame, text="Your Name:").grid(row=1, column=0, pady=(5, 0))
        name_entry = tk.Entry(container_frame)
        name_entry.grid(row=2, column=0, pady=(0, 10))

        tk.Label(container_frame, text="Contact Number:").grid(row=3, column=0, pady=(5, 0))
        contact_entry = tk.Entry(container_frame)
        contact_entry.grid(row=4, column=0, pady=(0, 10))

        def validate_voter():
            voter_name = name_entry.get()
            contact = contact_entry.get()

            if voter_name not in self.voters or contact != self.voters[voter_name]['contact']:
                messagebox.showerror("Error", "Voter not registered or contact number mismatch.")
                return

            self.show_voting_options(voter_name)

        tk.Button(container_frame, text="Proceed to Vote", command=validate_voter).grid(row=5, column=0, pady=10)
        tk.Button(container_frame, text="Return to Voting Menu", command=self.voting_menu).grid(row=6, column=0, pady=10)

    def show_voting_options(self, voter_name):
        self.clear_frame()

        container_frame = tk.Frame(self.root, bg="#2c3e30")
        container_frame.place(relx=0.5, rely=0.5, anchor='center') 

        tk.Label(container_frame, text="Voting Options", font=('Arial', 13, 'bold'), fg="white", bg="#2c3e30", width=1500).grid(row=0, column=0, pady=20)

        tk.Label(container_frame, text="Enter Your Chosen Party List:").grid(row=1, column=0, pady=(5, 0))
        party_entry = tk.Entry(container_frame)
        party_entry.grid(row=2, column=0, pady=(0, 10))

        tk.Label(container_frame, text="Enter 12 Senatorial Candidates (comma-separated):").grid(row=3, column=0, pady=(5, 0))
        senators_entry = tk.Entry(container_frame)
        senators_entry.grid(row=4, column=0, pady=(0, 10))

        def submit_vote():
            chosen_party = party_entry.get()
            selected_senators = [name.strip() for name in senators_entry.get().split(',')]

            if chosen_party not in self.parties:
                messagebox.showerror("Invalid Vote", "Party list not registered.")
                return

            if len(selected_senators) != 12 or not all(candidate in self.senatorial_candidates for candidate in selected_senators):
                messagebox.showerror("Invalid Vote", "Please enter exactly 12 valid senatorial candidates.")
                return

            self.votes[chosen_party] = self.votes.get(chosen_party, 0) + 1
            for candidate in selected_senators:
                self.senate_votes[candidate] = self.senate_votes.get(candidate, 0) + 1

            messagebox.showinfo("Vote Cast", "Your vote has been successfully cast.")
            self.create_main_menu()

        tk.Button(container_frame, text="Submit Vote", command=submit_vote).grid(row=5, column=0, pady=10)
        tk.Button(container_frame, text="Return to Voting Menu", command=self.voting_menu).grid(row=6, column=0, pady=10)

    def show_parties(self):
        self.clear_frame()

        container_frame = tk.Frame(self.root, bg="#2c3e30")
        container_frame.place(relx=0.5, rely=0.5, anchor='center') 

        tk.Label(container_frame, text="Registered Parties", font=('Arial', 13, 'bold'), fg="white", bg="#2c3e30", width=1500).grid(row=0, column=0, pady=10)

        if not self.parties:
            tk.Label(container_frame, text="No registered parties yet.", font=('Arial', 9)).grid(row=1, column=0)
        else:
            for idx, (party, members) in enumerate(self.parties.items(), start=1):
                tk.Label(container_frame, text=f"{party} - Members: {', '.join(members)}").grid(row=idx + 1, column=0, pady=2)

        tk.Button(container_frame, text="Return to Voting Menu", command=self.voting_menu).grid(row=len(self.parties) + 2, column=0, pady=20)

    def show_senators(self):
        self.clear_frame()

        container_frame = tk.Frame(self.root, bg="#2c3e30")
        container_frame.place(relx=0.5, rely=0.5, anchor='center')  

        tk.Label(container_frame, text="Registered Senatorial Candidates", font=('Arial', 13, 'bold'), fg="white", bg="#2c3e30", width=1500).grid(row=0, column=0, pady=10)

        if not self.senatorial_candidates:
            tk.Label(container_frame, text="No registered senatorial candidates yet.", font=('Arial', 9)).grid(row=1, column=0)
        else:
            for idx, candidate in enumerate(self.senatorial_candidates, start=1):
                tk.Label(container_frame, text=candidate).grid(row=idx + 1, column=0, pady=2)

        tk.Button(container_frame, text="Return to Voting Menu", command=self.voting_menu).grid(row=len(self.senatorial_candidates) + 2, column=0, pady=20)

    def show_votes(self):
        self.clear_frame()

        container_frame = tk.Frame(self.root, bg="#2c3e30")
        container_frame.place(relx=0.5, rely=0.5, anchor='center') 

        tk.Label(container_frame, text="Current Votes", font=('Arial', 13, 'bold'), fg="white", bg="#2c3e30", width=1500).grid(row=0, column=0, pady=10)

        tk.Label(container_frame, text="Party List Votes:", font=('Arial', 10, 'bold')).grid(row=1, column=0, pady=10)
        if not self.votes:
            tk.Label(container_frame, text="No votes cast for any party list yet.", font=('Arial', 9)).grid(row=2, column=0)
        else:
            for idx, (party, count) in enumerate(self.votes.items(), start=3):
                tk.Label(container_frame, text=f"{party}: {count} votes").grid(row=idx, column=0)

        tk.Label(container_frame, text="Senatorial Votes:", font=('Arial', 10, 'bold')).grid(row=len(self.votes) + 3, column=0, pady=10)
        if not self.senate_votes:
            tk.Label(container_frame, text="No votes cast for any senatorial candidate yet.", font=('Arial', 9)).grid(row=len(self.votes) + 4, column=0)
        else:
            for idx, (candidate, count) in enumerate(self.senate_votes.items(), start=len(self.votes) + 5):
                tk.Label(container_frame, text=f"{candidate}: {count} votes").grid(row=idx, column=0)

        tk.Button(container_frame, text="Return to Voting Menu", command=self.voting_menu).grid(row=len(self.votes) + len(self.senate_votes) + 5, column=0, pady=20)

    def clear_frame(self):
        for widget in self.root.winfo_children():
            widget.destroy()

root = tk.Tk()
VotingSystemGUI(root)
root.mainloop()
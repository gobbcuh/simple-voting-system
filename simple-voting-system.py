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
        self.root.geometry("400x600")  # Set a fixed window size for consistency
        self.root.configure(bg="#29482b")  # Deep green background
        self.create_main_menu()

    def create_main_menu(self):
        self.clear_frame()

        # Main Panel
        main_panel = tk.Frame(self.root, bg="#1e2d24", bd=2)
        main_panel.place(relx=0.5, rely=0.5, anchor="center", width=320, height=500)

        # Header Text
        tk.Label(main_panel, text="2025 PHILIPPINE\nSENATORIAL ELECTION", 
                 font=('Arial', 14, 'bold'), fg="white", bg="#1e2d24").pack(pady=(20, 5))
        tk.Label(main_panel, text="Karapatan ay Gamitin,\nBumoto para sa Isang Hangarin\n", 
                 font=('Arial', 10), fg="light gray", bg="#1e2d24").pack()

        # Buttons
        button_style = {
            "font": ('Arial', 12),
            "bg": "#2c3e30",  # Subtle dark green tint
            "fg": "white",
            "width": 25,
            "height": 2,
            "relief": "flat"
        }

        tk.Button(main_panel, text="Registration for Candidacy", command=self.register_candidacy_menu, **button_style).pack(pady=10)
        tk.Button(main_panel, text="Registration for Voting", command=self.register_voter_menu, **button_style).pack(pady=10)
        tk.Button(main_panel, text="Voting Menu", command=self.voting_menu, **button_style).pack(pady=10)
        tk.Button(main_panel, text="Quit", command=self.root.quit, **button_style).pack(pady=10)

        # Footer Text
        tk.Label(main_panel, text="A BRIGHTER FUTURE\nSTARTS WITH YOUR VOTE", 
                 font=('Arial', 10, 'bold'), fg="white", bg="#1e2d24").pack(pady=(20, 10))

    def register_candidacy_menu(self):
        self.clear_frame()

        tk.Label(self.root, text="Candidacy Registration", font=('Arial', 16)).pack(pady=20)

        tk.Button(self.root, text="Register as Party List", command=self.register_party_list, width=25).pack(pady=10)
        tk.Button(self.root, text="Register as Senator", command=self.register_senator, width=25).pack(pady=10)
        tk.Button(self.root, text="Return to Main Menu", command=self.create_main_menu, width=25).pack(pady=10)

    def register_party_list(self):
        self.clear_frame()

        tk.Label(self.root, text="Register a Party List", font=('Arial', 16)).pack(pady=10)
        
        tk.Label(self.root, text="Party List Name:").pack(pady=(5, 0))
        party_name_entry = tk.Entry(self.root)
        party_name_entry.pack(pady=(0, 10))

        tk.Label(self.root, text="Add Members:").pack(pady=(5, 0))

        member_entries = []
        for i in range(5):  # Add 5 input boxes for 5 members
            member_entry = tk.Entry(self.root)
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

        tk.Button(self.root, text="Submit", command=submit_party).pack(pady=10)
        tk.Button(self.root, text="Return to Main Menu", command=self.create_main_menu).pack(pady=10)

    def register_senator(self):
        self.clear_frame()

        tk.Label(self.root, text="Register Senatorial Candidate", font=('Arial', 16)).pack(pady=10)

        tk.Label(self.root, text="Candidate Name:").pack(pady=(5, 0))
        candidate_entry = tk.Entry(self.root)
        candidate_entry.pack(pady=(0, 10))

        def submit_senator():
            candidate_name = candidate_entry.get()
            if not candidate_name:
                messagebox.showerror("Error", "Candidate name cannot be empty.")
                return
            self.senatorial_candidates.append(candidate_name)
            messagebox.showinfo("Success", f"Candidate '{candidate_name}' registered successfully!")
            self.create_main_menu()

        tk.Button(self.root, text="Submit", command=submit_senator).pack(pady=10)
        tk.Button(self.root, text="Return to Main Menu", command=self.create_main_menu).pack(pady=10)

    def register_voter_menu(self):
        self.clear_frame()

        tk.Label(self.root, text="Voter Registration", font=('Arial', 16)).pack(pady=20)

        tk.Label(self.root, text="Name:").pack(pady=(5, 0))
        name_entry = tk.Entry(self.root)
        name_entry.pack(pady=(0, 10))

        tk.Label(self.root, text="Age:").pack(pady=(5, 0))
        age_entry = tk.Entry(self.root)
        age_entry.pack(pady=(0, 10))

        tk.Label(self.root, text="Contact Number:").pack(pady=(5, 0))
        contact_entry = tk.Entry(self.root)
        contact_entry.pack(pady=(0, 10))

        tk.Label(self.root, text="Address:").pack(pady=(5, 0))
        address_entry = tk.Entry(self.root)
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

        tk.Button(self.root, text="Submit", command=submit_voter).pack(pady=10)
        tk.Button(self.root, text="Return to Main Menu", command=self.create_main_menu).pack(pady=10)

    def voting_menu(self):
        self.clear_frame()

        tk.Label(self.root, text="Voting Menu", font=('Arial', 16)).pack(pady=20)

        tk.Button(self.root, text="Vote", command=self.vote_initial, width=25).pack(pady=10)
        tk.Button(self.root, text="Show Party List", command=self.show_parties, width=25).pack(pady=10)
        tk.Button(self.root, text="Show Senatorial Candidates", command=self.show_senators, width=25).pack(pady=10)
        tk.Button(self.root, text="Show Votes", command=self.show_votes, width=25).pack(pady=10)
        tk.Button(self.root, text="Return to Main Menu", command=self.create_main_menu, width=25).pack(pady=10)

    def vote_initial(self):
        self.clear_frame()

        tk.Label(self.root, text="Voting", font=('Arial', 16)).pack(pady=20)

        tk.Label(self.root, text="Your Name:").pack(pady=(5, 0))
        name_entry = tk.Entry(self.root)
        name_entry.pack(pady=(0, 10))

        tk.Label(self.root, text="Contact Number:").pack(pady=(5, 0))
        contact_entry = tk.Entry(self.root)
        contact_entry.pack(pady=(0, 10))

        def validate_voter():
            voter_name = name_entry.get()
            contact = contact_entry.get()

            if voter_name not in self.voters or contact != self.voters[voter_name]['contact']:
                messagebox.showerror("Error", "Voter not registered or contact number mismatch.")
                return

            self.show_voting_options(voter_name)

        tk.Button(self.root, text="Proceed to Vote", command=validate_voter).pack(pady=10)
        tk.Button(self.root, text="Return to Voting Menu", command=self.voting_menu).pack(pady=10)

    def show_voting_options(self, voter_name):
        self.clear_frame()

        tk.Label(self.root, text="Voting Options", font=('Arial', 16)).pack(pady=20)

        tk.Label(self.root, text="Enter Your Chosen Party List:").pack(pady=(5, 0))
        party_entry = tk.Entry(self.root)
        party_entry.pack(pady=(0, 10))

        tk.Label(self.root, text="Enter 12 Senatorial Candidates (comma-separated):").pack(pady=(5, 0))
        senators_entry = tk.Entry(self.root)
        senators_entry.pack(pady=(0, 10))

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

        tk.Button(self.root, text="Submit Vote", command=submit_vote).pack(pady=10)
        tk.Button(self.root, text="Return to Voting Menu", command=self.voting_menu).pack(pady=10)

    def show_parties(self):
        self.clear_frame()

        tk.Label(self.root, text="Registered Parties", font=('Arial', 16)).pack(pady=10)

        if not self.parties:
            tk.Label(self.root, text="No registered parties yet.", font=('Arial', 12)).pack()
        else:
            for party, members in self.parties.items():
                tk.Label(self.root, text=f"{party} - Members: {', '.join(members)}").pack(pady=2)

        tk.Button(self.root, text="Return to Voting Menu", command=self.voting_menu).pack(pady=20)

    def show_senators(self):
        self.clear_frame()

        tk.Label(self.root, text="Registered Senatorial Candidates", font=('Arial', 16)).pack(pady=10)

        if not self.senatorial_candidates:
            tk.Label(self.root, text="No registered senatorial candidates yet.", font=('Arial', 12)).pack()
        else:
            for candidate in self.senatorial_candidates:
                tk.Label(self.root, text=candidate).pack(pady=2)

        tk.Button(self.root, text="Return to Voting Menu", command=self.voting_menu).pack(pady=20)

    def show_votes(self):
        self.clear_frame()

        tk.Label(self.root, text="Current Votes", font=('Arial', 16)).pack(pady=10)

        tk.Label(self.root, text="Party List Votes:", font=('Arial', 14, 'bold')).pack(pady=10)
        if not self.votes:
            tk.Label(self.root, text="No votes cast for any party list yet.", font=('Arial', 12)).pack()
        else:
            for party, count in self.votes.items():
                tk.Label(self.root, text=f"{party}: {count} votes").pack()

        tk.Label(self.root, text="Senatorial Votes:", font=('Arial', 14, 'bold')).pack(pady=10)
        if not self.senate_votes:
            tk.Label(self.root, text="No votes cast for any senatorial candidate yet.", font=('Arial', 12)).pack()
        else:
            for candidate, count in self.senate_votes.items():
                tk.Label(self.root, text=f"{candidate}: {count} votes").pack()

        tk.Button(self.root, text="Return to Voting Menu", command=self.voting_menu).pack(pady=20)

    def clear_frame(self):
        for widget in self.root.winfo_children():
            widget.destroy()

root = tk.Tk()
VotingSystemGUI(root)
root.mainloop()
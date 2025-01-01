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
        self.create_main_menu()

    def create_main_menu(self):
        self.clear_frame()

        tk.Label(self.root, text="2025 Philippine Senate Election", font=('Arial', 16)).pack(pady=20)

        tk.Button(self.root, text="Registration for Candidacy", command=self.register_candidacy_menu, width=25).pack(pady=10)
        tk.Button(self.root, text="Registration for Voting", command=self.register_voter_menu, width=25).pack(pady=10)
        tk.Button(self.root, text="Voting Menu", command=self.voting_menu, width=25).pack(pady=10)
        tk.Button(self.root, text="Quit", command=self.root.quit, width=25).pack(pady=10)

    def register_candidacy_menu(self):
        self.clear_frame()

        tk.Label(self.root, text="Candidacy Registration", font=('Arial', 16)).pack(pady=20)

        tk.Button(self.root, text="Register as Party List", command=self.register_party_list, width=25).pack(pady=10)
        tk.Button(self.root, text="Register as Senator", command=self.register_senator, width=25).pack(pady=10)
        tk.Button(self.root, text="Return to Main Menu", command=self.create_main_menu, width=25).pack(pady=10)

    def register_party_list(self):
        self.clear_frame()

        tk.Label(self.root, text="Register a Party List", font=('Arial', 16)).pack(pady=10)
        
        tk.Label(self.root, text="Party List Name:").pack()
        party_name_entry = tk.Entry(self.root)
        party_name_entry.pack()

        tk.Label(self.root, text="Add Members:").pack()

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

        tk.Label(self.root, text="Candidate Name:").pack()
        candidate_entry = tk.Entry(self.root)
        candidate_entry.pack()

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

        tk.Label(self.root, text="Name:").pack()
        name_entry = tk.Entry(self.root)
        name_entry.pack()

        tk.Label(self.root, text="Age:").pack()
        age_entry = tk.Entry(self.root)
        age_entry.pack()

        tk.Label(self.root, text="Contact Number:").pack()
        contact_entry = tk.Entry(self.root)
        contact_entry.pack()

        tk.Label(self.root, text="Address:").pack()
        address_entry = tk.Entry(self.root)
        address_entry.pack()

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

        tk.Label(self.root, text="Your Name:").pack()
        name_entry = tk.Entry(self.root)
        name_entry.pack()

        tk.Label(self.root, text="Contact Number:").pack()
        contact_entry = tk.Entry(self.root)
        contact_entry.pack()

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

        tk.Label(self.root, text="Enter Your Chosen Party List:").pack()
        chosen_party_entry = tk.Entry(self.root)
        chosen_party_entry.pack()

        tk.Label(self.root, text="Select Senators (must be 12):").pack()
        senator_entries = []
        for i in range(12):
            senator_entry = tk.Entry(self.root)
            senator_entry.pack(pady=2)
            senator_entries.append(senator_entry)

        def submit_vote():
            chosen_party = chosen_party_entry.get()
            selected_senators = [entry.get().strip() for entry in senator_entries if entry.get().strip()]

            if chosen_party not in self.parties:
                messagebox.showerror("Error", "Invalid Party List selected.")
                return

            if len(selected_senators) != 12:
                messagebox.showerror("Error", "You must select exactly 12 senators.")
                return

            # Validate senator names against registered candidates
            for senator in selected_senators:
                if senator not in self.senatorial_candidates:
                    messagebox.showerror("Error", f"Invalid senator name: {senator}. Please register candidates correctly.")
                    return

            # Save votes
            self.votes[voter_name] = {
                'party': chosen_party,
                'senators': selected_senators
            }

            messagebox.showinfo("Success", f"Vote cast successfully for {voter_name}.")
            self.create_main_menu()

        tk.Button(self.root, text="Submit Vote", command=submit_vote).pack(pady=10)
        tk.Button(self.root, text="Return to Voting Menu", command=self.voting_menu).pack(pady=10)

    def show_parties(self):
        self.clear_frame()

        tk.Label(self.root, text="Registered Party Lists", font=('Arial', 16)).pack(pady=20)

        for party, members in self.parties.items():
            tk.Label(self.root, text=f"Party: {party}, Members: {', '.join(members)}").pack(pady=2)

        tk.Button(self.root, text="Return to Voting Menu", command=self.voting_menu).pack(pady=10)

    def show_senators(self):
        self.clear_frame()

        tk.Label(self.root, text="Registered Senatorial Candidates", font=('Arial', 16)).pack(pady=20)

        for candidate in self.senatorial_candidates:
            tk.Label(self.root, text=f"Candidate: {candidate}").pack(pady=2)

        tk.Button(self.root, text="Return to Voting Menu", command=self.voting_menu).pack(pady=10)

    def show_votes(self):
        self.clear_frame()
        tk.Label(self.root, text="Votes Cast", font=('Arial', 16)).pack(pady=10)

        for voter, vote_info in self.votes.items():
            tk.Label(self.root, text=f"Voter: {voter}, Party: {vote_info['party']}, Senators: {', '.join(vote_info['senators'])}").pack(pady=2)

        tk.Button(self.root, text="Return to Voting Menu", command=self.voting_menu).pack(pady=10)

    def clear_frame(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = VotingSystemGUI(root)
    root.mainloop()
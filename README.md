# **Simple Voting System**

This is a Python project I made to simulate a simple voting system. Right now, it’s a **local application** that runs only on the device it’s installed on. I designed it to resemble and function like an online voting system, utilizing **Tkinter** for the interface. I haven’t deployed it to a web server because I’m still working on the basics, but I’d love to explore making it fully online in the future.  

Note: The use of the 2025 Philippine Senatorial Election is only for context in this exercise. This project is a simplified simulation and does not accurately reflect the actual senatorial election process.

---
## **✨ Features**

### **📝 1. Registration**
- **Candidates** can register as either a **Party List** or a **Senatorial Candidate**.  
- **Voters** can sign up by entering their **name, age, contact number, and address**.  
  - To ensure eligibility, only those aged 18 and above are allowed to register.  
  - There’s validation to make sure inputs are realistic.  

### **🗳️ 2. Voting Process**
- Registered voters must confirm their identity by entering their **name** and **contact number**. This step ensures that only registered individuals can vote.  
- Voters can cast their votes for:  
  - **Up to 12 senatorial candidates**.  
  - **One party list**.  
- The system ensures you don’t exceed the allowed number of votes.  

### **🔍 3. Transparency**
- The app provides a list of all registered **Party Lists** and **Senatorial Candidates** for reference.  
- A live **vote tally** shows how many votes each candidate and party has received, keeping the process open and easy to track.  

### **🖥️ 4. Tkinter Interface**
- I used **Tkinter** to build a user-friendly interface. It’s simple but effective for this type of project, making it easy to navigate and use.

---

## **💻 How to Use the System**

### **Requirements**
1. Python version 3.8 or newer.  
2. Tkinter (usually pre-installed with Python).  

### **Steps to Run**
1. Download or clone the project files to your computer.  
2. Open your terminal and navigate to the folder where the files are stored.  
3. Run the following command:  
   ```bash
   python voting_system.py
   ```
4. The main menu will open, and you can choose what to do next.  

---

## **🔑 Key Actions**
- **Register as a Candidate**:  
  Choose between **Party List** or **Senatorial Candidate**, then fill in the necessary details.  
- **Register as a Voter**:  
  Enter your **name, age, contact number**, and **address**. If you’re under 18, the system will notify you that you’re not eligible to vote.  
- **Vote**:  
  Confirm your identity by entering your **name** and **contact number**, then proceed to vote. Make sure to stay within the allowed number of votes.  
- **View Candidates and Results**:  
  Check the list of registered candidates and the current vote tally.

---

## **🌐 Why It’s Local (For Now)** 
This isn’t a fully online voting system yet. It’s more of a **local application** that mimics how an online system works. It runs directly on your computer and doesn’t require the internet or a web server to operate.  

I wanted to dive into real-world programming exercises to help me improve my skills in Python. Though it’s a simple project at the moment, it’s been a great way to understand concepts like registration, input validation, and basic security. This is just the beginning, and I’m excited to keep refining it and eventually make it fully online.

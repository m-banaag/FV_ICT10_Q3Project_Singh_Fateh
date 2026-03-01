from pyscript import document

# --- SEATWORK 2 DATA ---
TEAMS = {
    "Yellow Tigers": "https://lh7-rt.googleusercontent.com/docsz/AD_4nXdI0SCrx93LCnJR8Nwd_BUgISDhvkkfm-BT-3I8n0FEHdiPW2VB7rUGwJWQgCD0x2qaKn5CX9Z_Icf-F7fKzXWLrmaN6J3p7f6lr8IFki7Gwrj7YiVCGDv4-ZQPZdFrwzvtZ7SDir5o8uBMnkUTfjw?key=ZleEhdKJAAHCBHL55WGzYw",
    "Blue Bears": "https://lh7-rt.googleusercontent.com/docsz/AD_4nXesq1NaV9kV06LBOyOXpL_GWwt9iHbAXnCK7OIYJpgsPxJVaAS3Gq4C37HHo0JecwfMVQ0iIPDdYrpy3AoVkV94uEDJfO2gQC7FxnqS8uq_82J7te-iCdPx0lkjCEGpySaBg6B9ojbTJJK0vlV4mQ?key=ZleEhdKJAAHCBHL55WGzYw",
    "Red Bulldogs": "https://lh7-rt.googleusercontent.com/docsz/AD_4nXcaXqWjUGLrrzi0ARgE-1yDeZxShxocLA3KRpQ0yLr9dlxWDlNQtZHAhrmqJ3sVkgNYONGcGrz6iPZqkXzRCI1rbOrD58ucbBqTH-D-wuObksqvITnJ9jP0I71yKlcEP0uFBS7sAuZRrMx5Td44pBM?key=ZleEhdKJAAHCBHL55WGzYw",
    "Green Hornets": "https://lh7-rt.googleusercontent.com/docsz/AD_4nXcUMgblQF0EfXIgNSCxhpnbCAqMjsu6Mk0BaPYidMIHqWkTkRbKtueo0Ed4a9aW62mgkodL0cMfE9RQZ7bTOLIQ-fpZx9TAWabR3EaZeDaRgrc3LRhpJyETAZtT5T7gqlKDPl-dJLV9331eFCMDrwQ?key=ZleEhdKJAAHCBHL55WGzYw"
}

ASSIGNMENTS = {
    "7-Emerald": "Blue Bears", "7-Ruby": "Red Bulldogs", "7-Topaz": "Yellow Tigers", "7-Sapphire": "Green Hornets",
    "8-Emerald": "Red Bulldogs", "8-Ruby": "Yellow Tigers", "8-Topaz": "Green Hornets", "8-Sapphire": "Blue Bears",
    "9-Emerald": "Yellow Tigers", "9-Ruby": "Green Hornets", "9-Topaz": "Blue Bears", "9-Sapphire": "Red Bulldogs",
    "10-Emerald": "Green Hornets", "10-Ruby": "Blue Bears", "10-Topaz": "Red Bulldogs", "10-Sapphire": "Yellow Tigers"
}

# --- PLAYER ROSTER DATA ---
classmates = [
    "AGUDO, Jairo James Sta Maria", "ALAIZA, Mikko Jaden Alupani", "AL HAZMI, Naser Abdullah",
    "BANAAG, Matthew Diaz", "BARCELONA, Emille Sebastian Tamayo", "BRION, Cyrene Maghirang",
    "BUO, Miguel Sealtiel Encarnacion", "CASTRO, Lian Candice Galvez", "CRUZ, Shia Adam Jayzen Panganiban",
    "DEL PRADO, Karla Cassandra Cruz", "ENTRADA, Gianna Noelle Dimabuyu", "FRANCISCO, Gavin Waytan",
    "GAVINA, Adrian Erick Valencia", "GOYENECHEA, Xylee Araos", "GUEVARRA, Sofia Francesca Remo",
    "HABERIA, Ioana Biel Banayad", "JANAYAN, Alexander Joel Marayag", "LIBUTAN, Jabez Nimrod Marabarbas",
    "LUBO, Arabella Elyzza Sabile", "MANUEL, Ala Luisa Ismael", "MARIPOSQUE, Janine Rasing",
    "PAGTALUNAN, Rycob Andrew Dimayuga", "REYES, Lucas Tabotabo", "SINGH, Fateh",
    "SUBAAN, Tyronne Jaiho Ballestros", "TAN, Audrey Alexia Hernandez", "VARGAS, Alexandra Milan Espiritu",
    "ZALDIVAR, James Guile Monroyo"
]

# --- SKILLS TEST LOGIC ---
def verify_account(event):
    # Defining Variables
    username = document.querySelector("#user_input").value
    password = document.querySelector("#pass_input").value
    log = document.querySelector("#feedback-log")
    success_card = document.querySelector("#success-card")
    # If-Else Statements
    issues = []
    if len(username) < 7: issues.append("Username requires at least 7 characters.")
    if len(password) < 10: issues.append("Password requires at least 10 characters.")
    if not any(c.isalpha() for c in password): issues.append("Password requires at least one letter.")
    if not any(c.isdigit() for c in password): issues.append("Password requires at least one number.")
    
    # Display if the login is successful or not
    if not issues:
        log.innerHTML = '<span style="color:#FFD700; font-weight:bold;">SUCCESS: ACCOUNT CREATED</span>'
        success_card.style.display = "block"
    else:
        log.innerHTML = f'<span style="color:#ff4d4d; font-weight:bold;">{"<br>".join(issues)}</span>'
    

# --- SEATWORK 2 LOGIC ---
def check_status(event):
    # Defining Variables
    is_reg = document.querySelector("#reg_yes").checked
    is_med = document.querySelector("#med_yes").checked
    grade = document.querySelector("#grade").value
    section = document.querySelector("#section").value
    msg = document.querySelector("#status-msg")
    pic = document.querySelector("#team-img")
    
    # If-Else Statements
    pic.style.display = "none"
    if not is_reg:
        # Not Registered Online
        msg.innerText = "INSTRUCTION: Please register online first."
        msg.style.color = "#ff4d4d"
    elif not is_med:
        # No Medical Clearance
        msg.innerText = "INSTRUCTION: Please secure a medical clearance."
        msg.style.color = "#ff4d4d"
    elif not grade or not section:
        # No Grade or Section Selected
        msg.innerText = "INSTRUCTION: Select Grade and Section."
        msg.style.color = "#ff4d4d"
    else:
        # Successful Result
        team = ASSIGNMENTS.get(f"{grade}-{section}")
        msg.innerHTML = f"<span style='color: #FFD700;'>CONGRATULATIONS!</span><br>You are a {team}."
        msg.style.color = "white"
        pic.src = TEAMS[team]
        pic.style.display = "block"

# --- PROJECT PLAYER LIST LOGIC ---
def display_players(event):
    container = document.querySelector("#player-list")
    html_output = ""
    # Python Loop implementation
    for i, name in enumerate(classmates, 1):
        html_output += f"<div style='padding:12px; border-bottom:1px solid #333; font-weight:500;'>{i}. {name}</div>"
    container.innerHTML = html_output

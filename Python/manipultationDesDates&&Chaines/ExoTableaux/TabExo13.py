# Écrire un programme qui prend la date actuelle et renvoie le nombre 
# de jours fériés restants dans l'année (en utilisant une liste fixe de jours 
# fériés pour votre pays).

from datetime import datetime
holidays = {
    "New Year's Day": "January 1, 2024",  # New Year's Day (Gregorian calendar)
    "Labour Day": "May 1, 2024",          # Labour Day
    "Throne Day": "July 30, 2024",        # Throne Day (Fête du Trône)
    "Revolution Day": "August 20, 2024",  # Revolution Day
    "King's Feast": "August 21, 2024",    # King's Feast (Fête du Roi)
    "Independence Day": "November 18, 2024",  # Independence Day (Fête de l'Indépendance)

    # Islamic holidays (dates vary each year depending on the lunar calendar)
    "Eid al-Fitr": "April 10, 2024",   # Eid al-Fitr (End of Ramadan)
    "Eid al-Adha": "June 5, 2024",     # Eid al-Adha (Feast of Sacrifice)
    "Islamic New Year": "July 7, 2024",  # Islamic New Year (Hijri New Year)
    "Mawlid al-Nabi": "September 15, 2024",  # Mawlid al-Nabi (Prophet Muhammad's Birthday)
    
    # Islamic holidays, dates may vary based on moon sighting
    "Fête de l'Armistice": "November 11, 2024",  # Armistice Day (Fête de l'Armistice)
}


today = datetime.now()

for holiday, date in holidays.items():
    date = datetime.strptime(date, "%B %d, %Y")
    if date > today:
        print(f"The next holiday is {holiday} on {date.strftime('%B %d, %Y')}.")
        break
    
    
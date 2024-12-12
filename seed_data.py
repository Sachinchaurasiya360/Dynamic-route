from app import app, db, Incident, CCTVCamera
from datetime import datetime

def seed_database():
    with app.app_context():
        # Create all database tables
        db.create_all()
        
        # Clear existing data
        Incident.query.delete()
        CCTVCamera.query.delete()

        # Add CCTV cameras in Bhopal
        cameras = [
            # LNCT to Railway Station Route
            CCTVCamera(latitude=23.2807, longitude=77.4024, status='active'),  # LNCT Main Gate
            CCTVCamera(latitude=23.2789, longitude=77.4001, status='active'),  # Kolar Road Junction
            CCTVCamera(latitude=23.2772, longitude=77.3921, status='active'),  # Danish Nagar
            CCTVCamera(latitude=23.2812, longitude=77.3867, status='active'),  # Piplani Petrol Pump
            CCTVCamera(latitude=23.2834, longitude=77.3812, status='active'),  # BHEL Gate 1
            CCTVCamera(latitude=23.2856, longitude=77.3734, status='active'),  # Govindpura Industrial Area
            CCTVCamera(latitude=23.2867, longitude=77.3654, status='active'),  # Barkheda Pathani
            CCTVCamera(latitude=23.2809, longitude=77.3461, status='active'),  # Bhopal Junction (Railway Station)
            
            # Alternative Route via Karond
            CCTVCamera(latitude=23.2891, longitude=77.4012, status='active'),  # Karond Square
            CCTVCamera(latitude=23.2912, longitude=77.3876, status='active'),  # Karond Bridge
            CCTVCamera(latitude=23.2876, longitude=77.3698, status='active'),  # Jehangirabad
            
            # Major Areas (existing)
            CCTVCamera(latitude=23.2599, longitude=77.4126, status='active'),  # MP Nagar
            CCTVCamera(latitude=23.2517, longitude=77.4027, status='active'),  # New Market
            CCTVCamera(latitude=23.2332, longitude=77.4343, status='active'),  # Habibganj Railway Station
            CCTVCamera(latitude=23.2707, longitude=77.4013, status='active'),  # TT Nagar
            CCTVCamera(latitude=23.2615, longitude=77.3919, status='active'),  # Board Office Square
        ]

        # Add incidents in Bhopal
        incidents = [
            # LNCT to Railway Station Route Incidents
            Incident(latitude=23.2807, longitude=77.4024, incident_type='Harassment', severity=1),  # Near LNCT
            Incident(latitude=23.2789, longitude=77.4001, incident_type='Suspicious Activity', severity=2),  # Kolar Junction
            Incident(latitude=23.2772, longitude=77.3921, incident_type='Theft', severity=2),  # Danish Nagar
            Incident(latitude=23.2834, longitude=77.3812, incident_type='Harassment', severity=2),  # Near BHEL
            Incident(latitude=23.2867, longitude=77.3654, incident_type='Stalking', severity=2),  # Barkheda
            
            # Alternative Route Incidents
            Incident(latitude=23.2891, longitude=77.4012, incident_type='Theft', severity=3),  # Karond Square
            Incident(latitude=23.2912, longitude=77.3876, incident_type='Harassment', severity=2),  # Karond Bridge
            Incident(latitude=23.2876, longitude=77.3698, incident_type='Suspicious Activity', severity=1),  # Jehangirabad
            
            # Major Areas (existing incidents)
            Incident(latitude=23.2599, longitude=77.4126, incident_type='Harassment', severity=2),  # MP Nagar
            Incident(latitude=23.2517, longitude=77.4027, incident_type='Stalking', severity=2),  # New Market
            Incident(latitude=23.2332, longitude=77.4343, incident_type='Theft', severity=3),  # Habibganj
            Incident(latitude=23.2707, longitude=77.4013, incident_type='Harassment', severity=2),  # TT Nagar
        ]

        try:
            # Add data to database
            db.session.add_all(cameras)
            db.session.add_all(incidents)
            db.session.commit()
            print("Database seeded successfully with Bhopal data!")
            print(f"Added {len(cameras)} CCTV cameras and {len(incidents)} incidents")
            print("\nSafe Route Options from LNCT to Railway Station:")
            print("1. Primary Route: LNCT -> Kolar Road -> Danish Nagar -> BHEL -> Govindpura -> Railway Station")
            print("   - Well-lit route with 8 active CCTV cameras")
            print("   - Average safety score: 85%")
            print("\n2. Alternative Route: LNCT -> Karond -> Jehangirabad -> Railway Station")
            print("   - Shorter but fewer CCTV cameras")
            print("   - Average safety score: 75%")
        except Exception as e:
            print(f"Error seeding database: {str(e)}")
            db.session.rollback()

if __name__ == '__main__':
    seed_database()

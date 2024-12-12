from app import app, db, Incident, Camera
from datetime import datetime

def seed_database():
    with app.app_context():
        # Create all database tables
        db.create_all()
        
        # Clear existing data
        Incident.query.delete()
        Camera.query.delete()

        # Add CCTV cameras in Bhopal
        cameras = [
            # Educational Institutions
            Camera(latitude=23.2807, longitude=77.4024, status='active'),  # LNCT Main Gate
            Camera(latitude=23.2814, longitude=77.4028, status='active'),  # LNCT Campus Interior
            Camera(latitude=23.2332, longitude=77.4343, status='active'),  # MANIT
            Camera(latitude=23.2328, longitude=77.4339, status='active'),  # MANIT Gate
            Camera(latitude=23.2163, longitude=77.4356, status='active'),  # Barkatullah University
            Camera(latitude=23.2168, longitude=77.4361, status='active'),  # University Gate
            Camera(latitude=23.2501, longitude=77.4897, status='active'),  # BMHRC
            
            # Transport Hubs
            Camera(latitude=23.2809, longitude=77.3461, status='active'),  # Bhopal Junction (Railway Station)
            Camera(latitude=23.2815, longitude=77.3465, status='active'),  # Railway Station Platform 1
            Camera(latitude=23.2812, longitude=77.3458, status='active'),  # Railway Station Exit
            Camera(latitude=23.2332, longitude=77.4343, status='active'),  # Habibganj Railway Station
            Camera(latitude=23.2328, longitude=77.4338, status='active'),  # Habibganj Station Exit
            Camera(latitude=23.2863, longitude=77.3375, status='active'),  # Nadra Bus Stand
            Camera(latitude=23.2633, longitude=77.4107, status='active'),  # ISBT
            
            # Major Markets
            Camera(latitude=23.2517, longitude=77.4027, status='active'),  # New Market
            Camera(latitude=23.2522, longitude=77.4032, status='active'),  # New Market Central
            Camera(latitude=23.2512, longitude=77.4022, status='active'),  # New Market Parking
            Camera(latitude=23.2599, longitude=77.4126, status='active'),  # MP Nagar Zone 1
            Camera(latitude=23.2595, longitude=77.4121, status='active'),  # MP Nagar Zone 2
            Camera(latitude=23.2334, longitude=77.4294, status='active'),  # 10 Number Market
            Camera(latitude=23.2528, longitude=77.4015, status='active'),  # Chowk Bazar
            
            # Important Intersections
            Camera(latitude=23.2615, longitude=77.3919, status='active'),  # Board Office Square
            Camera(latitude=23.2707, longitude=77.4013, status='active'),  # TT Nagar Square
            Camera(latitude=23.2891, longitude=77.4012, status='active'),  # Karond Square
            Camera(latitude=23.2834, longitude=77.3812, status='active'),  # BHEL Gate 1
            Camera(latitude=23.2789, longitude=77.4001, status='active'),  # Kolar Junction
            Camera(latitude=23.2856, longitude=77.3734, status='active'),  # Govindpura
            Camera(latitude=23.2632, longitude=77.3854, status='active'),  # Roshanpura Square
            Camera(latitude=23.2508, longitude=77.4021, status='active'),  # Mata Mandir Square
            
            # Residential Areas
            Camera(latitude=23.2772, longitude=77.3921, status='active'),  # Danish Nagar
            Camera(latitude=23.2867, longitude=77.3654, status='active'),  # Barkheda
            Camera(latitude=23.2912, longitude=77.3876, status='active'),  # Karond Colony
            Camera(latitude=23.2876, longitude=77.3698, status='active'),  # Jehangirabad
            Camera(latitude=23.2641, longitude=77.4021, status='active'),  # Arera Colony
            Camera(latitude=23.2812, longitude=77.3867, status='active'),  # Piplani
            Camera(latitude=23.2534, longitude=77.4312, status='active'),  # Shahpura
            Camera(latitude=23.2823, longitude=77.3512, status='active'),  # Bairagarh
            
            # Tourist Spots
            Camera(latitude=23.2836, longitude=77.3513, status='active'),  # Van Vihar Entry
            Camera(latitude=23.2829, longitude=77.3508, status='active'),  # Van Vihar Interior
            Camera(latitude=23.2507, longitude=77.3428, status='active'),  # Upper Lake View
            Camera(latitude=23.2515, longitude=77.3425, status='active'),  # Boat Club
            Camera(latitude=23.2625, longitude=77.4021, status='active'),  # DB Mall
            Camera(latitude=23.2630, longitude=77.4026, status='active'),  # DB Mall Parking
            
            # Additional Coverage
            Camera(latitude=23.2876, longitude=77.3698, status='active'),  # Jehangirabad Police Station
            Camera(latitude=23.2641, longitude=77.4021, status='active'),  # E-7 Arera Colony
            Camera(latitude=23.2534, longitude=77.4312, status='active'),  # Shahpura Lake
            Camera(latitude=23.2823, longitude=77.3512, status='active'),  # Bairagarh Bus Stop
            Camera(latitude=23.2545, longitude=77.4024, status='active'),  # Polytechnic Square
            Camera(latitude=23.2812, longitude=77.3867, status='active'),  # Piplani Market
        ]

        # Add incidents in Bhopal (keeping existing incidents)
        incidents = [
            # LNCT to Railway Station Route Incidents
            Incident(latitude=23.2807, longitude=77.4024, severity=1),
            Incident(latitude=23.2789, longitude=77.4001, severity=2),
            Incident(latitude=23.2772, longitude=77.3921, severity=1),
            
            # Major Areas
            Incident(latitude=23.2599, longitude=77.4126, severity=2),  # MP Nagar
            Incident(latitude=23.2517, longitude=77.4027, severity=1),  # New Market
            Incident(latitude=23.2707, longitude=77.4013, severity=1),  # TT Nagar
        ]

        # Add all cameras and incidents to database
        for camera in cameras:
            db.session.add(camera)
        
        for incident in incidents:
            incident.timestamp = datetime.utcnow()  # Set current timestamp
            db.session.add(incident)

        # Commit all changes
        db.session.commit()
        print(f"Added {len(cameras)} cameras and {len(incidents)} incidents to the database")

if __name__ == '__main__':
    seed_database()

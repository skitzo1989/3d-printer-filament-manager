#!/usr/bin/env python3
"""
Populate the database with comprehensive sample filament data
"""

import requests
import json
from datetime import datetime, timedelta
import random

BASE_URL = "http://localhost:8847"

# Sample data with variety of brands, materials, colors, and specifications
sample_filaments = [
    # Hatchbox PLA Collection
    {
        "brand": "Hatchbox",
        "material": "PLA",
        "color": "True Black",
        "diameter": 1.75,
        "weight": 1000.0,
        "storage_location": "Dry Box A - Section 1",
        "purchase_price": 22.99,
        "notes": "Excellent quality, consistent diameter, perfect for beginners"
    },
    {
        "brand": "Hatchbox",
        "material": "PLA",
        "color": "True White",
        "diameter": 1.75,
        "weight": 950.0,
        "storage_location": "Dry Box A - Section 2",
        "purchase_price": 22.99,
        "notes": "Great surface finish, minimal stringing"
    },
    {
        "brand": "Hatchbox",
        "material": "PLA",
        "color": "Transparent Red",
        "diameter": 1.75,
        "weight": 800.0,
        "storage_location": "Dry Box A - Section 3",
        "purchase_price": 24.99,
        "notes": "Beautiful transparency when printed with correct settings"
    },
    
    # PRUSAMENT Premium Collection
    {
        "brand": "PRUSAMENT",
        "material": "PLA",
        "color": "Galaxy Black",
        "diameter": 1.75,
        "weight": 1000.0,
        "storage_location": "Premium Shelf - Top",
        "purchase_price": 34.99,
        "notes": "Premium quality with sparkle effect, tight tolerances ±0.02mm"
    },
    {
        "brand": "PRUSAMENT",
        "material": "PETG",
        "color": "Prusa Orange",
        "diameter": 1.75,
        "weight": 1000.0,
        "storage_location": "Premium Shelf - Top",
        "purchase_price": 34.99,
        "notes": "Signature Prusa orange color, excellent chemical resistance"
    },
    {
        "brand": "PRUSAMENT",
        "material": "ABS",
        "color": "Jet Black",
        "diameter": 1.75,
        "weight": 1000.0,
        "storage_location": "Premium Shelf - Middle",
        "purchase_price": 34.99,
        "notes": "High-end ABS with superior layer adhesion"
    },
    
    # eSUN Value Collection
    {
        "brand": "eSUN",
        "material": "PLA",
        "color": "Cool White",
        "diameter": 1.75,
        "weight": 1000.0,
        "storage_location": "Drawer 1 - Left",
        "purchase_price": 19.99,
        "notes": "Good value filament, reliable printing"
    },
    {
        "brand": "eSUN",
        "material": "ABS",
        "color": "Silver",
        "diameter": 1.75,
        "weight": 1000.0,
        "storage_location": "Drawer 1 - Right",
        "purchase_price": 21.99,
        "notes": "Metallic finish, good for functional parts"
    },
    {
        "brand": "eSUN",
        "material": "PETG",
        "color": "Natural Clear",
        "diameter": 1.75,
        "weight": 950.0,
        "storage_location": "Drawer 2 - Center",
        "purchase_price": 23.99,
        "notes": "Crystal clear transparency, food safe"
    },
    
    # Overture Premium Collection
    {
        "brand": "Overture",
        "material": "PLA",
        "color": "Matte Black",
        "diameter": 1.75,
        "weight": 1000.0,
        "storage_location": "Shelf B - Section 1",
        "purchase_price": 25.99,
        "notes": "Beautiful matte finish, low gloss surface"
    },
    {
        "brand": "Overture",
        "material": "ABS",
        "color": "White",
        "diameter": 1.75,
        "weight": 1000.0,
        "storage_location": "Shelf B - Section 2",
        "purchase_price": 26.99,
        "notes": "Excellent for post-processing, smooth finish"
    },
    
    # SUNLU Flexible Materials
    {
        "brand": "SUNLU",
        "material": "TPU",
        "color": "Clear",
        "diameter": 1.75,
        "weight": 500.0,
        "storage_location": "Flexible Materials Box",
        "purchase_price": 28.99,
        "notes": "Shore 95A hardness, excellent flexibility and clarity"
    },
    {
        "brand": "SUNLU",
        "material": "TPU",
        "color": "Red",
        "diameter": 1.75,
        "weight": 450.0,
        "storage_location": "Flexible Materials Box",
        "purchase_price": 28.99,
        "notes": "Great for phone cases, gaskets, and flexible parts"
    },
    
    # Polymaker Specialty Materials
    {
        "brand": "Polymaker",
        "material": "PLA",
        "color": "Army Green",
        "diameter": 1.75,
        "weight": 1000.0,
        "storage_location": "Specialty Materials Drawer",
        "purchase_price": 29.99,
        "notes": "PolyTerra PLA - eco-friendly with matte finish"
    },
    {
        "brand": "Polymaker",
        "material": "PETG",
        "color": "Transparent Blue",
        "diameter": 1.75,
        "weight": 1000.0,
        "storage_location": "Specialty Materials Drawer",
        "purchase_price": 32.99,
        "notes": "PolyLite PETG - excellent clarity and chemical resistance"
    },
    
    # 3DHojor Quality Collection
    {
        "brand": "3DHojor",
        "material": "PLA",
        "color": "Silk Gold",
        "diameter": 1.75,
        "weight": 1000.0,
        "storage_location": "Silk Filaments Section",
        "purchase_price": 24.99,
        "notes": "Beautiful silk finish with metallic sheen"
    },
    {
        "brand": "3DHojor",
        "material": "ABS",
        "color": "Blue",
        "diameter": 1.75,
        "weight": 1000.0,
        "storage_location": "Standard ABS Shelf",
        "purchase_price": 23.99,
        "notes": "Consistent quality, good dimensional accuracy"
    },
    
    # Specialty and Filled Materials
    {
        "brand": "Hatchbox",
        "material": "WOOD",
        "color": "Natural Wood",
        "diameter": 1.75,
        "weight": 750.0,
        "storage_location": "Specialty Materials - Top Shelf",
        "purchase_price": 29.99,
        "notes": "Wood-filled PLA, can be sanded and stained, smells like wood"
    },
    {
        "brand": "Proto-pasta",
        "material": "METAL",
        "color": "Stainless Steel",
        "diameter": 1.75,
        "weight": 500.0,
        "storage_location": "Metal Fill Section",
        "purchase_price": 39.99,
        "notes": "Heavy metal-filled PLA, can be polished to metallic finish"
    },
    {
        "brand": "NinjaFlex",
        "material": "TPU",
        "color": "Flamingo Pink",
        "diameter": 1.75,
        "weight": 500.0,
        "storage_location": "Flexible Materials Box",
        "purchase_price": 34.99,
        "notes": "Ultra-flexible, Shore 85A, perfect for wearables"
    },
    
    # High-Temperature Materials
    {
        "brand": "BASF",
        "material": "ASA",
        "color": "Natural",
        "diameter": 1.75,
        "weight": 750.0,
        "storage_location": "High Temp Materials",
        "purchase_price": 45.99,
        "notes": "UV resistant, excellent for outdoor applications"
    },
    {
        "brand": "Polymaker",
        "material": "PC",
        "color": "Clear",
        "diameter": 1.75,
        "weight": 500.0,
        "storage_location": "Engineering Plastics",
        "purchase_price": 59.99,
        "notes": "Engineering grade polycarbonate, very strong and heat resistant"
    },
    {
        "brand": "Taulman",
        "material": "NYLON",
        "color": "Natural",
        "diameter": 1.75,
        "weight": 450.0,
        "storage_location": "Engineering Plastics",
        "purchase_price": 49.99,
        "notes": "Bridge Nylon - excellent strength and flexibility, hygroscopic"
    },
    
    # Support Materials
    {
        "brand": "eSUN",
        "material": "PVA",
        "color": "Natural",
        "diameter": 1.75,
        "weight": 350.0,
        "storage_location": "Support Materials - Sealed Container",
        "purchase_price": 39.99,
        "notes": "Water-soluble support material, store in airtight container"
    },
    {
        "brand": "Polymaker",
        "material": "HIPS",
        "color": "White",
        "diameter": 1.75,
        "weight": 1000.0,
        "storage_location": "Support Materials Shelf",
        "purchase_price": 26.99,
        "notes": "Dissolves in limonene, good support material for ABS"
    },
    
    # Large Format (3mm) Filaments
    {
        "brand": "Hatchbox",
        "material": "PLA",
        "color": "Green",
        "diameter": 3.0,
        "weight": 1000.0,
        "storage_location": "3mm Filaments - Rack A",
        "purchase_price": 28.99,
        "notes": "3mm diameter for older printers, same great Hatchbox quality"
    },
    {
        "brand": "eSUN",
        "material": "ABS",
        "color": "Black",
        "diameter": 3.0,
        "weight": 1000.0,
        "storage_location": "3mm Filaments - Rack A",
        "purchase_price": 31.99,
        "notes": "3mm ABS for industrial applications"
    },
    
    # Budget Options
    {
        "brand": "AmazonBasics",
        "material": "PLA",
        "color": "Blue",
        "diameter": 1.75,
        "weight": 1000.0,
        "storage_location": "Budget Filaments Drawer",
        "purchase_price": 18.99,
        "notes": "Budget-friendly option, decent quality for learning"
    },
    {
        "brand": "Inland",
        "material": "PLA",
        "color": "Yellow",
        "diameter": 1.75,
        "weight": 1000.0,
        "storage_location": "Budget Filaments Drawer",
        "purchase_price": 16.99,
        "notes": "Micro Center brand, good value for practice prints"
    },
    
    # Exotic Colors and Effects
    {
        "brand": "ZIRO",
        "material": "PLA",
        "color": "Silk Rainbow",
        "diameter": 1.75,
        "weight": 800.0,
        "storage_location": "Silk/Special Effects Section",
        "purchase_price": 26.99,
        "notes": "Color-changing silk finish, beautiful rainbow effect"
    },
    {
        "brand": "GEEETECH",
        "material": "PLA",
        "color": "Glow in Dark Green",
        "diameter": 1.75,
        "weight": 1000.0,
        "storage_location": "Special Effects Shelf",
        "purchase_price": 24.99,
        "notes": "Charges with light and glows in the dark for hours"
    }
]

def add_filament(filament_data):
    """Add a single filament to the database"""
    try:
        response = requests.post(f"{BASE_URL}/api/filaments", json=filament_data)
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Added: {data['brand']} {data['material']} {data['color']}")
            return True
        else:
            print(f"❌ Failed to add {filament_data['brand']} {filament_data['material']}: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Error adding {filament_data['brand']} {filament_data['material']}: {e}")
        return False

def clear_existing_data():
    """Clear existing test data (optional)"""
    try:
        response = requests.get(f"{BASE_URL}/api/filaments")
        if response.status_code == 200:
            filaments = response.json()
            test_brands = ["Test Brand", "Test Enhanced", "Super Long Brand Name"]
            
            for filament in filaments:
                if filament['brand'] in test_brands:
                    delete_response = requests.delete(f"{BASE_URL}/api/filaments/{filament['id']}")
                    if delete_response.status_code == 200:
                        print(f"🗑️  Removed test data: {filament['brand']} {filament['material']}")
                    
    except Exception as e:
        print(f"⚠️  Could not clear test data: {e}")

def populate_database():
    """Populate the database with all sample filaments"""
    print("🚀 Starting database population with sample filaments...")
    print("=" * 60)
    
    # Optionally clear test data
    clear_existing_data()
    
    success_count = 0
    total_count = len(sample_filaments)
    
    for i, filament in enumerate(sample_filaments, 1):
        print(f"\n[{i}/{total_count}] Adding {filament['brand']} {filament['material']}...")
        
        # Add some purchase dates (random dates within last year)
        if 'purchase_date' not in filament:
            days_ago = random.randint(30, 365)
            purchase_date = datetime.now() - timedelta(days=days_ago)
            filament['purchase_date'] = purchase_date.isoformat()
        
        if add_filament(filament):
            success_count += 1
    
    print("\n" + "=" * 60)
    print(f"✅ Successfully added {success_count}/{total_count} filaments!")
    print(f"🎯 Database now contains a diverse collection of:")
    print(f"   • {len(set(f['brand'] for f in sample_filaments))} different brands")
    print(f"   • {len(set(f['material'] for f in sample_filaments))} different materials")
    print(f"   • {len(set(f['color'] for f in sample_filaments))} different colors")
    print(f"   • Both 1.75mm and 3.0mm diameters")
    print(f"   • Range from budget to premium filaments")
    print(f"   • Specialty materials and effects")
    
    print(f"\n🌐 View your collection at: http://localhost:8847")
    print(f"➕ Test enhanced lookup at: http://localhost:8847/add")

if __name__ == "__main__":
    try:
        populate_database()
    except requests.exceptions.ConnectionError:
        print("❌ Error: Could not connect to the server.")
        print("Please make sure the FastAPI server is running on http://localhost:8847")
        print("Run: python main.py")
    except KeyboardInterrupt:
        print("\n⏹️  Operation cancelled by user")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
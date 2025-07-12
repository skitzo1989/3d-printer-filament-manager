"""
Filament specification lookup service
"""

import re
from typing import Dict, Optional, List
import requests
from bs4 import BeautifulSoup
import asyncio

class FilamentLookup:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        })

    async def search_filament_specs(self, brand: str, material: str, color: str = "") -> Dict:
        """
        Search for filament specifications online using search engine
        """
        try:
            # Try to search for specific brand/material combination
            search_results = await self._search_web(brand, material, color)
            if search_results["found"]:
                return search_results
            
            # Fallback to material defaults with enhanced information
            return self._get_material_defaults(material)
            
        except Exception as e:
            print(f"Error during lookup: {e}")
            return self._get_material_defaults(material)

    async def _search_web(self, brand: str, material: str, color: str = "") -> Dict:
        """Search the web for filament specifications"""
        
        # For now, return enhanced defaults with brand-specific notes
        # In a full implementation, this would use a search API or web scraping
        
        enhanced_specs = self._get_material_defaults(material)
        if enhanced_specs["found"]:
            # Add brand-specific enhancements
            brand_lower = brand.lower()
            
            # Brand-specific temperature and speed recommendations
            brand_specific_settings = {
                "hatchbox": {
                    "PLA": {"nozzle_temp_recommended": 205, "print_speed_recommended": 65},
                    "ABS": {"nozzle_temp_recommended": 238, "print_speed_recommended": 55},
                    "PETG": {"nozzle_temp_recommended": 240, "print_speed_recommended": 50}
                },
                "esun": {
                    "PLA": {"nozzle_temp_recommended": 210, "print_speed_recommended": 60},
                    "ABS": {"nozzle_temp_recommended": 240, "print_speed_recommended": 50},
                    "PETG": {"nozzle_temp_recommended": 235, "print_speed_recommended": 45}
                },
                "prusament": {
                    "PLA": {"nozzle_temp_recommended": 215, "print_speed_recommended": 70},
                    "ABS": {"nozzle_temp_recommended": 255, "print_speed_recommended": 60},
                    "PETG": {"nozzle_temp_recommended": 250, "print_speed_recommended": 55}
                },
                "overture": {
                    "PLA": {"nozzle_temp_recommended": 200, "print_speed_recommended": 60},
                    "ABS": {"nozzle_temp_recommended": 235, "print_speed_recommended": 50},
                    "PETG": {"nozzle_temp_recommended": 230, "print_speed_recommended": 45}
                },
                "sunlu": {
                    "PLA": {"nozzle_temp_recommended": 200, "print_speed_recommended": 60},
                    "TPU": {"nozzle_temp_recommended": 225, "print_speed_recommended": 15}
                },
                "polymaker": {
                    "PLA": {"nozzle_temp_recommended": 210, "print_speed_recommended": 60},
                    "PETG": {"nozzle_temp_recommended": 245, "print_speed_recommended": 50}
                },
                "3dhojor": {
                    "PLA": {"nozzle_temp_recommended": 205, "print_speed_recommended": 60},
                    "ABS": {"nozzle_temp_recommended": 240, "print_speed_recommended": 50}
                }
            }
            
            brand_notes = {
                "hatchbox": "Known for consistent quality and easy printing",
                "esun": "Good value filaments with reliable performance", 
                "sunlu": "Popular brand with good color selection",
                "overture": "Premium quality with excellent surface finish",
                "prusament": "High-end filament with tight tolerances",
                "polymaker": "Innovative materials and specialty filaments",
                "inland": "Budget-friendly option with decent quality",
                "ziro": "Known for silk finish and vibrant colors",
                "amazonbasics": "Basic quality, good for learning",
                "geeetech": "Eco-friendly options available",
                "3dhojor": "Quality filament with good dimensional accuracy and consistency"
            }
            
            # Apply brand-specific settings if available
            if brand_lower in brand_specific_settings:
                material_upper = material.upper()
                if material_upper in brand_specific_settings[brand_lower]:
                    brand_settings = brand_specific_settings[brand_lower][material_upper]
                    if "nozzle_temp_recommended" in brand_settings:
                        enhanced_specs["nozzle_temp_recommended"] = brand_settings["nozzle_temp_recommended"]
                    if "print_speed_recommended" in brand_settings:
                        enhanced_specs["print_speed_recommended"] = brand_settings["print_speed_recommended"]
            
            if brand_lower in brand_notes:
                enhanced_specs["notes"] += f" | {brand_notes[brand_lower]}"
                enhanced_specs["source"] = f"Enhanced Database ({brand} {material})"
            
            # Color-specific adjustments
            if color.lower() in ["transparent", "clear", "natural"]:
                if material.upper() == "PETG":
                    enhanced_specs["notes"] += " | Excellent transparency when printed correctly"
                elif material.upper() == "PLA":
                    enhanced_specs["notes"] += " | Good for vases and decorative items"
        
        return enhanced_specs

    async def _search_manufacturer_site(self, brand: str, material: str) -> Dict:
        """Search manufacturer websites for specifications"""
        specs = {"found": False}
        
        # Common manufacturer domains and patterns
        manufacturer_domains = {
            "hatchbox": "hatchbox3d.com",
            "esun": "esun3d.com", 
            "sunlu": "sunlu.com",
            "overture": "overture3d.com",
            "prusament": "prusa3d.com",
            "polymaker": "polymaker.com",
            "inland": "inlandfilament.com"
        }
        
        brand_lower = brand.lower()
        if brand_lower in manufacturer_domains:
            try:
                # Search the manufacturer site
                search_url = f"https://www.google.com/search?q=site:{manufacturer_domains[brand_lower]} {material} temperature"
                # This would need to be implemented with proper web scraping
                # For now, return default specs
                pass
            except:
                pass
        
        return specs

    async def _search_general_databases(self, brand: str, material: str, color: str) -> Dict:
        """Search general 3D printing databases and forums"""
        specs = {"found": False}
        
        # This would search sites like:
        # - 3dprintingmedia.network
        # - all3dp.com
        # - matterhackers.com
        # - reddit.com/r/3Dprinting
        
        # For implementation, we'd use web scraping here
        # For now, return material defaults
        return specs

    def _get_material_defaults(self, material: str) -> Dict:
        """Get default temperature settings for material types"""
        material_defaults = {
            "PLA": {
                "nozzle_temp_min": 190,
                "nozzle_temp_max": 220,
                "nozzle_temp_recommended": 200,
                "bed_temp": 60,
                "print_speed_recommended": 60,
                "notes": "Easy to print, biodegradable, low warping",
                "typical_properties": ["Low shrinkage", "Good surface finish", "Biodegradable"]
            },
            "ABS": {
                "nozzle_temp_min": 220,
                "nozzle_temp_max": 250,
                "nozzle_temp_recommended": 235,
                "bed_temp": 90,
                "print_speed_recommended": 50,
                "notes": "Strong and durable, requires heated bed, can warp",
                "typical_properties": ["High strength", "Impact resistant", "Can be post-processed"]
            },
            "PETG": {
                "nozzle_temp_min": 220,
                "nozzle_temp_max": 250,
                "nozzle_temp_recommended": 235,
                "bed_temp": 75,
                "print_speed_recommended": 45,
                "notes": "Chemical resistant, food safe, clear prints possible",
                "typical_properties": ["Chemical resistant", "Food safe", "Good transparency"]
            },
            "TPU": {
                "nozzle_temp_min": 210,
                "nozzle_temp_max": 230,
                "nozzle_temp_recommended": 220,
                "bed_temp": 50,
                "print_speed_recommended": 20,
                "notes": "Flexible filament, print slowly, reduce retraction",
                "typical_properties": ["Flexible", "Rubber-like", "Impact resistant"]
            },
            "ASA": {
                "nozzle_temp_min": 240,
                "nozzle_temp_max": 260,
                "nozzle_temp_recommended": 250,
                "bed_temp": 90,
                "print_speed_recommended": 45,
                "notes": "UV resistant, similar to ABS but better outdoor performance",
                "typical_properties": ["UV resistant", "Weather resistant", "High temperature resistance"]
            },
            "PC": {
                "nozzle_temp_min": 270,
                "nozzle_temp_max": 300,
                "nozzle_temp_recommended": 285,
                "bed_temp": 110,
                "print_speed_recommended": 30,
                "notes": "Very strong, high temperature resistance, requires all-metal hotend",
                "typical_properties": ["Very high strength", "High temperature resistance", "Transparent"]
            },
            "NYLON": {
                "nozzle_temp_min": 240,
                "nozzle_temp_max": 280,
                "nozzle_temp_recommended": 260,
                "bed_temp": 80,
                "print_speed_recommended": 35,
                "notes": "Very strong, flexible, absorbs moisture easily",
                "typical_properties": ["Very strong", "Flexible", "Chemical resistant", "Hygroscopic"]
            },
            "WOOD": {
                "nozzle_temp_min": 190,
                "nozzle_temp_max": 220,
                "nozzle_temp_recommended": 205,
                "bed_temp": 60,
                "print_speed_recommended": 40,
                "notes": "Wood-filled PLA, can be sanded and stained, may clog nozzle",
                "typical_properties": ["Wood appearance", "Can be post-processed", "Natural smell"]
            },
            "METAL": {
                "nozzle_temp_min": 190,
                "nozzle_temp_max": 220,
                "nozzle_temp_recommended": 210,
                "bed_temp": 60,
                "print_speed_recommended": 35,
                "notes": "Metal-filled PLA, heavy, can be polished",
                "typical_properties": ["Metallic appearance", "Heavy", "Can be polished"]
            },
            "HIPS": {
                "nozzle_temp_min": 220,
                "nozzle_temp_max": 240,
                "nozzle_temp_recommended": 230,
                "bed_temp": 90,
                "print_speed_recommended": 50,
                "notes": "Good support material, dissolves in limonene",
                "typical_properties": ["Good support material", "Lightweight", "Can be dissolved"]
            },
            "PVA": {
                "nozzle_temp_min": 180,
                "nozzle_temp_max": 200,
                "nozzle_temp_recommended": 190,
                "bed_temp": 60,
                "print_speed_recommended": 25,
                "notes": "Water-soluble support material, store in dry conditions",
                "typical_properties": ["Water soluble", "Support material", "Hygroscopic"]
            }
        }
        
        material_upper = material.upper()
        if material_upper in material_defaults:
            defaults = material_defaults[material_upper].copy()
            defaults.update({
                "found": True,
                "source": "Material Database (Default Values)"
            })
            return defaults
        
        # Unknown material
        return {
            "found": False,
            "source": "Unknown material",
            "nozzle_temp_min": None,
            "nozzle_temp_max": None,
            "nozzle_temp_recommended": None,
            "bed_temp": None,
            "print_speed_recommended": None,
            "notes": "Unknown material - please check manufacturer specifications",
            "typical_properties": []
        }

    def get_common_brands(self) -> List[str]:
        """Get the complete list of common brands"""
        return [
            "Hatchbox", "eSUN", "SUNLU", "Overture", "PRUSAMENT", "Polymaker",
            "AmazonBasics", "Inland", "ZIRO", "FormFutura", "NinjaFlex",
            "GEEETECH", "Matterhackers", "Proto-pasta", "ColorFabb",
            "Fiberlogy", "Devil Design", "BASF", "Ultimaker", "Verbatim",
            "3D Solutech", "TIANSE", "TECBEARS", "ANYCUBIC", "Creality",
            "3DHojor", "Prusa", "Bambu Lab", "Polyplus", "Repetier",
            "3DXTECH", "Fillamentum", "E3D", "Push Plastic", "Atomic Filament",
            "IC3D", "Taulman", "NinjaFlex", "SainSmart", "KODAK", "Gizmo Dorks"
        ]

    async def get_all_brands(self) -> List[str]:
        """Get all available brands for autocomplete"""
        return sorted(self.get_common_brands())

    async def get_brand_suggestions(self, partial_brand: str) -> List[str]:
        """Get brand suggestions based on partial input"""
        common_brands = self.get_common_brands()
        
        partial_lower = partial_brand.lower()
        
        # First, find brands that start with the partial input
        starts_with = [brand for brand in common_brands 
                      if brand.lower().startswith(partial_lower)]
        
        # Then, find brands that contain the partial input
        contains = [brand for brand in common_brands 
                   if partial_lower in brand.lower() and not brand.lower().startswith(partial_lower)]
        
        # Combine and return top matches (prioritize starts_with)
        suggestions = starts_with + contains
        
        return suggestions[:10]  # Return top 10 matches

# Global instance
filament_lookup = FilamentLookup()
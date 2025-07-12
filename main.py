from fastapi import FastAPI, Depends, HTTPException, Request, Form, Query
from fastapi.responses import HTMLResponse, JSONResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from typing import List, Optional
from datetime import datetime
import os

from models import Filament, get_db, create_tables
from schemas import FilamentCreate, FilamentUpdate, FilamentResponse
from filament_lookup import filament_lookup

app = FastAPI(title="3D Printer Filament Manager", version="1.0.0")

# Create database tables
create_tables()

# Set up templates and static files
templates = Jinja2Templates(directory="templates")

# Create static and templates directories if they don't exist
os.makedirs("static", exist_ok=True)
os.makedirs("templates", exist_ok=True)

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Serve favicon files at root level for compatibility
@app.get("/favicon.ico")
def favicon():
    return FileResponse("static/favicon.ico")

@app.get("/favicon.svg")
def favicon_svg():
    return FileResponse("static/favicon.svg")

@app.get("/site.webmanifest")
def webmanifest():
    return FileResponse("static/site.webmanifest")

# API Routes
@app.get("/api/filaments", response_model=List[FilamentResponse])
def get_filaments(db: Session = Depends(get_db)):
    return db.query(Filament).all()

@app.get("/api/filaments/{filament_id}", response_model=FilamentResponse)
def get_filament(filament_id: int, db: Session = Depends(get_db)):
    filament = db.query(Filament).filter(Filament.id == filament_id).first()
    if not filament:
        raise HTTPException(status_code=404, detail="Filament not found")
    return filament

@app.post("/api/filaments", response_model=FilamentResponse)
def create_filament(filament: FilamentCreate, db: Session = Depends(get_db)):
    db_filament = Filament(**filament.dict())
    db.add(db_filament)
    db.commit()
    db.refresh(db_filament)
    return db_filament

@app.put("/api/filaments/{filament_id}", response_model=FilamentResponse)
def update_filament(filament_id: int, filament: FilamentUpdate, db: Session = Depends(get_db)):
    db_filament = db.query(Filament).filter(Filament.id == filament_id).first()
    if not db_filament:
        raise HTTPException(status_code=404, detail="Filament not found")
    
    for key, value in filament.dict(exclude_unset=True).items():
        setattr(db_filament, key, value)
    
    db_filament.updated_at = datetime.utcnow()
    db.commit()
    db.refresh(db_filament)
    return db_filament

@app.delete("/api/filaments/{filament_id}")
def delete_filament(filament_id: int, db: Session = Depends(get_db)):
    db_filament = db.query(Filament).filter(Filament.id == filament_id).first()
    if not db_filament:
        raise HTTPException(status_code=404, detail="Filament not found")
    
    db.delete(db_filament)
    db.commit()
    return {"message": "Filament deleted successfully"}

# Lookup endpoints
@app.get("/api/lookup/filament")
async def lookup_filament_specs(
    brand: str = Query(..., description="Filament brand"),
    material: str = Query(..., description="Filament material"),
    color: Optional[str] = Query(None, description="Filament color")
):
    """Look up filament specifications from online sources"""
    try:
        specs = await filament_lookup.search_filament_specs(brand, material, color or "")
        return JSONResponse(content=specs)
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"error": f"Lookup failed: {str(e)}"}
        )

@app.get("/api/lookup/brands")
async def get_brand_suggestions(q: str = Query(..., description="Partial brand name")):
    """Get brand name suggestions"""
    try:
        suggestions = await filament_lookup.get_brand_suggestions(q)
        return JSONResponse(content={"suggestions": suggestions})
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"error": f"Brand lookup failed: {str(e)}"}
        )

@app.get("/api/brands/all")
async def get_all_brands():
    """Get all available brands for autocomplete"""
    try:
        all_brands = await filament_lookup.get_all_brands()
        return JSONResponse(content={"brands": all_brands})
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"error": f"Failed to fetch brands: {str(e)}"}
        )

# Web interface routes
@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/test", response_class=HTMLResponse)
def test_lookup_page(request: Request):
    """Test page for lookup functionality"""
    with open("test_lookup_browser.html", "r") as f:
        return HTMLResponse(content=f.read())

@app.get("/test-button", response_class=HTMLResponse)
def test_button_page(request: Request):
    """Simple button test page"""
    with open("test_button.html", "r") as f:
        return HTMLResponse(content=f.read())

@app.get("/favicon-test", response_class=HTMLResponse)
def favicon_test_page(request: Request):
    """Test page to verify favicon functionality"""
    favicon_test_html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Favicon Test - Filament Manager</title>
        <link rel="icon" type="image/svg+xml" href="/static/favicon.svg">
        <link rel="icon" type="image/x-icon" href="/static/favicon.ico">
        <link rel="icon" type="image/png" sizes="32x32" href="/static/favicon-32x32.png">
        <link rel="icon" type="image/png" sizes="16x16" href="/static/favicon-16x16.png">
        <style>
            body { font-family: Arial, sans-serif; padding: 20px; }
            .favicon-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 20px; margin: 20px 0; }
            .favicon-item { text-align: center; padding: 20px; border: 1px solid #ddd; border-radius: 8px; }
            .favicon-item img { margin: 10px; }
        </style>
    </head>
    <body>
        <h1>🎨 Favicon Test Page</h1>
        <p>Check the browser tab to see the favicon! Also check out the different formats below:</p>
        
        <div class="favicon-grid">
            <div class="favicon-item">
                <h3>ICO Format</h3>
                <img src="/static/favicon.ico" alt="ICO favicon" style="width: 32px; height: 32px;">
                <p><code>favicon.ico</code></p>
            </div>
            
            <div class="favicon-item">
                <h3>SVG Format</h3>
                <img src="/static/favicon.svg" alt="SVG favicon" style="width: 32px; height: 32px;">
                <p><code>favicon.svg</code></p>
            </div>
            
            <div class="favicon-item">
                <h3>PNG 32x32</h3>
                <img src="/static/favicon-32x32.png" alt="PNG 32x32 favicon">
                <p><code>favicon-32x32.png</code></p>
            </div>
            
            <div class="favicon-item">
                <h3>PNG 16x16</h3>
                <img src="/static/favicon-16x16.png" alt="PNG 16x16 favicon">
                <p><code>favicon-16x16.png</code></p>
            </div>
            
            <div class="favicon-item">
                <h3>Apple Touch Icon</h3>
                <img src="/static/apple-touch-icon.png" alt="Apple touch icon" style="width: 60px; height: 60px;">
                <p><code>apple-touch-icon.png</code></p>
            </div>
            
            <div class="favicon-item">
                <h3>Android Chrome 192</h3>
                <img src="/static/android-chrome-192x192.png" alt="Android chrome icon" style="width: 60px; height: 60px;">
                <p><code>android-chrome-192x192.png</code></p>
            </div>
        </div>
        
        <h2>Quick Links</h2>
        <ul>
            <li><a href="/">🏠 Home (Filament Inventory)</a></li>
            <li><a href="/add">➕ Add Filament</a></li>
            <li><a href="/test">🧪 Lookup Test</a></li>
        </ul>
        
        <h2>Browser Tab Test</h2>
        <p>The browser tab for this page should show a blue cube icon! The favicon represents a 3D cube 
        matching the theme of your 3D printer filament manager.</p>
        
        <h2>Technical Details</h2>
        <ul>
            <li><strong>Theme Color:</strong> <span style="background: #007bff; color: white; padding: 2px 8px; border-radius: 4px;">#007bff (Bootstrap Primary Blue)</span></li>
            <li><strong>Icon Style:</strong> 3D isometric cube</li>
            <li><strong>Formats:</strong> SVG, ICO, PNG (multiple sizes)</li>
            <li><strong>PWA Ready:</strong> Includes web manifest</li>
        </ul>
    </body>
    </html>
    """
    return HTMLResponse(content=favicon_test_html)

@app.get("/debug", response_class=HTMLResponse)
def debug_lookup(request: Request):
    """Debug page for testing lookup functionality"""
    debug_html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Debug Lookup Function</title>
        <script src="https://unpkg.com/axios/dist/axios.min.js"></script>
    </head>
    <body>
        <h1>Lookup Function Debug</h1>
        
        <div>
            <label>Brand:</label>
            <input type="text" id="brand" value="Hatchbox">
        </div>
        
        <div>
            <label>Material:</label>
            <select id="material">
                <option value="PLA">PLA</option>
                <option value="ABS">ABS</option>
            </select>
        </div>
        
        <button id="lookupBtn">Test Lookup</button>
        
        <div id="results"></div>
        
        <script>
            console.log('Debug script loaded');
            
            document.getElementById('lookupBtn').addEventListener('click', async function() {
                console.log('Lookup button clicked');
                
                const brand = document.getElementById('brand').value;
                const material = document.getElementById('material').value;
                
                console.log('Brand:', brand, 'Material:', material);
                
                try {
                    const url = `/api/lookup/filament?brand=${encodeURIComponent(brand)}&material=${encodeURIComponent(material)}`;
                    console.log('Making request to:', url);
                    
                    const response = await axios.get(url);
                    console.log('Response:', response.data);
                    
                    document.getElementById('results').innerHTML = '<pre>' + JSON.stringify(response.data, null, 2) + '</pre>';
                    
                } catch (error) {
                    console.error('Error:', error);
                    document.getElementById('results').innerHTML = 'Error: ' + error.message;
                }
            });
        </script>
    </body>
    </html>
    """
    return HTMLResponse(content=debug_html)

@app.get("/add", response_class=HTMLResponse)
def add_filament_form(request: Request):
    return templates.TemplateResponse("add.html", {"request": request})

@app.post("/add", response_class=HTMLResponse)
async def add_filament(
    request: Request,
    brand: str = Form(...),
    material: str = Form(...),
    color: str = Form(...),
    diameter: float = Form(1.75),
    weight: str = Form(""),
    storage_location: str = Form(""),
    nozzle_temp_min: str = Form(""),
    nozzle_temp_max: str = Form(""),
    nozzle_temp_recommended: str = Form(""),
    bed_temp: str = Form(""),
    print_speed_recommended: str = Form(""),
    notes: str = Form(""),
    purchase_price: str = Form(""),
    db: Session = Depends(get_db)
):
    # Helper function to convert empty strings to None or parse numbers
    def parse_optional_float(value: str) -> Optional[float]:
        return float(value) if value.strip() else None
    
    def parse_optional_int(value: str) -> Optional[int]:
        return int(value) if value.strip() else None
    
    def parse_optional_str(value: str) -> Optional[str]:
        return value.strip() if value.strip() else None
    
    try:
        filament_data = {
            "brand": brand,
            "material": material,
            "color": color,
            "diameter": diameter,
            "weight": parse_optional_float(weight),
            "storage_location": parse_optional_str(storage_location),
            "nozzle_temp_min": parse_optional_int(nozzle_temp_min),
            "nozzle_temp_max": parse_optional_int(nozzle_temp_max),
            "nozzle_temp_recommended": parse_optional_int(nozzle_temp_recommended),
            "bed_temp": parse_optional_int(bed_temp),
            "print_speed_recommended": parse_optional_int(print_speed_recommended),
            "notes": parse_optional_str(notes),
            "purchase_price": parse_optional_float(purchase_price),
            "purchase_date": datetime.utcnow()
        }
        
        # Remove None values
        filament_data = {k: v for k, v in filament_data.items() if v is not None}
        
        db_filament = Filament(**filament_data)
        db.add(db_filament)
        db.commit()
        
        return templates.TemplateResponse("add.html", {
            "request": request, 
            "success": True, 
            "message": "Filament added successfully!"
        })
        
    except ValueError as e:
        return templates.TemplateResponse("add.html", {
            "request": request, 
            "error": True, 
            "message": f"Invalid number format: {str(e)}"
        })
    except Exception as e:
        return templates.TemplateResponse("add.html", {
            "request": request, 
            "error": True, 
            "message": f"Error adding filament: {str(e)}"
        })

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8847)
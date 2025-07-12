# Enhanced Lookup Feature Documentation

## Overview
The enhanced lookup feature automatically fills in comprehensive filament specifications based on brand and material selection, including manufacturer-specific recommended temperatures and optimal print speeds.

## How It Works

### 1. **Button States**

#### **Initial State**
- **Text**: "🔍 Lookup"
- **Style**: Blue outline button (`btn-outline-primary`)
- **Enabled**: Only when both brand and material are filled

#### **Loading State**
- **Text**: "🔄 Looking up..."
- **Style**: Blue outline button with spinner
- **Enabled**: Disabled during lookup

#### **Success State** ✅
- **Text**: "✅ Lookup Complete"
- **Style**: Green button (`btn-success`)
- **Duration**: 5 seconds, then resets
- **Triggered**: When specifications found successfully

#### **Default State** ⚠️
- **Text**: "⚠️ Defaults Used"  
- **Style**: Yellow/warning button (`btn-warning`)
- **Duration**: 5 seconds, then resets
- **Triggered**: When no specific specs found, defaults applied

#### **Error State** ❌
- **Text**: "❌ Error"
- **Style**: Red button (`btn-danger`)
- **Duration**: Until reset
- **Triggered**: When lookup fails

### 2. **Auto-fill Behavior**

When lookup succeeds, the following fields are automatically filled:
- **Nozzle Temperature Min** (e.g., 190°C)
- **Nozzle Temperature Max** (e.g., 220°C)  
- **Recommended Nozzle Temperature** (e.g., 205°C) - Manufacturer/brand-specific optimal temperature
- **Bed Temperature** (e.g., 60°C)
- **Recommended Print Speed** (e.g., 60 mm/s) - Optimal speed for quality prints
- **Notes** (appended with brand/material specific information)

### 3. **Brand Suggestions**

As you type in the brand field:
- **Dropdown appears** with matching brand suggestions
- **API call** to `/api/lookup/brands?q={partial_name}`
- **Click to select** from suggestions
- **Auto-enables** lookup button when brand + material selected

### 4. **Supported Brands**

Currently includes suggestions for 40+ brands:
- Hatchbox, eSUN, SUNLU, Overture, PRUSAMENT, Polymaker
- AmazonBasics, Inland, ZIRO, FormFutura, NinjaFlex
- GEEETECH, Matterhackers, Proto-pasta, ColorFabb
- 3DHojor, ANYCUBIC, Creality, and more

**Brands with Specific Temperature/Speed Profiles:**
- **Hatchbox**: Optimized temperatures and speeds for consistent printing
- **eSUN**: Higher temperature recommendations for strong layer adhesion
- **PRUSAMENT**: Premium settings for maximum quality
- **Overture**: Conservative settings for excellent surface finish
- **SUNLU**: Specialized TPU settings for flexible materials
- **Polymaker**: Advanced material-specific optimizations
- **3DHojor**: Balanced settings for dimensional accuracy

### 5. **Material Database**

Default specifications for:
- **PLA**: 190-220°C nozzle (rec: 200°C), 60°C bed, 60 mm/s
- **ABS**: 220-250°C nozzle (rec: 235°C), 90°C bed, 50 mm/s  
- **PETG**: 220-250°C nozzle (rec: 235°C), 75°C bed, 45 mm/s
- **TPU**: 210-230°C nozzle (rec: 220°C), 50°C bed, 20 mm/s
- **ASA**: 240-260°C nozzle (rec: 250°C), 90°C bed, 45 mm/s
- **PC**, **Nylon**, **HIPS**, **PVA**, Wood Fill, Metal Fill, etc.

### 6. **API Endpoints**

#### Brand Suggestions
```
GET /api/lookup/brands?q={partial_brand_name}
Response: {"suggestions": ["Brand1", "Brand2", ...]}
```

#### Filament Specifications
```
GET /api/lookup/filament?brand={brand}&material={material}&color={color}
Response: {
  "found": true,
  "source": "Enhanced Database (Brand Material)",
  "nozzle_temp_min": 190,
  "nozzle_temp_max": 220,
  "nozzle_temp_recommended": 205,
  "bed_temp": 60,
  "print_speed_recommended": 65,
  "notes": "Material properties and brand notes",
  "typical_properties": ["Property1", "Property2"]
}
```

## Usage Instructions

### **For Users**
1. **Enter Brand**: Type brand name (suggestions will appear)
2. **Select Material**: Choose from dropdown
3. **Click Lookup**: Button becomes enabled automatically
4. **View Results**: Temperature fields auto-fill, success message appears
5. **Button Changes**: Shows completion state for 5 seconds

### **For Developers**
- **Add New Brands**: Update `common_brands` list in `filament_lookup.py`
- **Add Brand Notes**: Update `brand_notes` dictionary
- **Add Materials**: Update `material_defaults` dictionary
- **Modify Temperatures**: Edit default temperature ranges

## Error Handling

- **Network errors**: Shows error state, allows retry
- **Invalid responses**: Falls back to material defaults
- **Empty results**: Uses material database defaults
- **Missing data**: Gracefully handles partial information

## User Experience Features

- **Real-time validation**: Button enables/disables as you type
- **Visual feedback**: Color-coded completion states
- **Auto-reset**: Button returns to normal after 5 seconds
- **Non-blocking**: Can continue using form during/after lookup
- **Helpful messages**: Clear indication of what happened

## Future Enhancements

- **Web scraping**: Could add real manufacturer website lookup
- **User contributions**: Allow users to submit specifications
- **Caching**: Store frequently looked up combinations
- **Offline mode**: Local database for common materials
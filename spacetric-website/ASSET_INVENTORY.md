# SPACETRIC WEBSITE - ASSET INVENTORY

## 📋 Complete Photo & Asset Management Guide

This document provides you with direct access to all images used across the Spacetric website, organized by category and purpose. You can easily replace any image by updating the URL in the corresponding HTML file.

---

## 🏢 MAIN BRANDING & HERO IMAGES

### Homepage Hero Banner
- **Current Image**: https://images.unsplash.com/photo-1614366502473-e54666693b44
- **Usage**: Main homepage hero background
- **Description**: Modern solar panel installation with blue sky
- **File Location**: `/main-pages/index.html` (line ~167)

### Alternative Hero Options
- **Option 2**: https://images.unsplash.com/photo-1615232714706-6b3adc67138b
- **Option 3**: https://images.unsplash.com/photo-1615630859219-0459703c34e6

### About Section Image
- **Current Image**: https://images.unsplash.com/photo-1680281707612-171a5194d50f
- **Usage**: About section "Modern Infrastructure" image
- **Description**: Modern building with green roof showing sustainable infrastructure
- **File Location**: `/main-pages/index.html` (about section)

---

## ⚡ ENERGY SOLUTIONS IMAGES

### Energy Hero Banner
- **Current Image**: https://images.unsplash.com/photo-1615232714706-6b3adc67138b
- **Usage**: Energy solutions page hero background
- **Description**: Professional solar panel array installation
- **File Location**: `/content/energy/energy-solutions.html`

### Solar Power Systems
- **Current Image**: https://images.unsplash.com/photo-1615630859219-0459703c34e6
- **Usage**: Solar Power Systems section illustration
- **Description**: Solar panel installation with monitoring equipment
- **File Location**: `/content/energy/energy-solutions.html`

### Energy Storage Systems
- **Current Image**: https://images.unsplash.com/photo-1693680204133-5711f0a74465
- **Usage**: Energy Storage Solutions section
- **Description**: Modern infrastructure with energy systems
- **File Location**: `/content/energy/energy-solutions.html`

---

## 💧 WATER SOLUTIONS IMAGES

### Water Hero Banner
- **Current Image**: https://images.unsplash.com/photo-1674578745937-c73f81bdda07
- **Usage**: Water solutions page hero background
- **Description**: Large-scale water treatment tanks and infrastructure
- **File Location**: `/content/water/water-solutions.html`

### Water Treatment Systems
- **Current Image**: https://images.unsplash.com/photo-1533077162801-86490c593afb
- **Usage**: Water Treatment Systems section illustration
- **Description**: Aerial view of water treatment facility with filtration ponds
- **File Location**: `/content/water/water-solutions.html`

### Water Purification Technology
- **Current Image**: https://images.unsplash.com/photo-1617155093730-a8bf47be792d
- **Usage**: Advanced Purification Technology section
- **Description**: Laboratory-grade water purification system
- **File Location**: `/content/water/water-solutions.html`

### Additional Water Images Available:
- **Option 1**: https://images.unsplash.com/photo-1636649389054-e5dcea139e64 (Circular water processing structure)
- **Option 2**: https://images.unsplash.com/photo-1623986854615-85baba27dfb6 (Professional purification equipment)
- **Option 3**: https://images.pexels.com/photos/6812505/pexels-photo-6812505.jpeg (Water testing/analysis)

---

## 🔒 SECURITY SOLUTIONS IMAGES

### Available Security Images:
- **Modern Security Camera**: https://images.unsplash.com/photo-1549109926-58f039549485
- **Dome Security Camera**: https://images.unsplash.com/photo-1528312635006-8ea0bc49ec63
- **CCTV Installation**: https://images.unsplash.com/photo-1589935447067-5531094415d1
- **Building Security**: https://images.unsplash.com/photo-1585206031650-9e9a7c87dcfe
- **Surveillance Dome Cameras**: https://images.unsplash.com/photo-1618908839493-516deaa83c79
- **Professional Installation**: https://images.unsplash.com/photo-1650214962171-8198a113621a
- **Security Monitoring**: https://images.unsplash.com/photo-1640826028382-e209fad88fa7
- **Security Equipment**: https://images.pexels.com/photos/33119793/pexels-photo-33119793.jpeg
- **Camera Installation**: https://images.pexels.com/photos/3205735/pexels-photo-3205735.jpeg

---

## 📡 TELECOMMUNICATIONS IMAGES

### Available Telecom Images:
- **Telecom Tower in Field**: https://images.unsplash.com/photo-1660082217875-e72dd943f0a8
- **Winter Hill Transmitter**: https://images.unsplash.com/photo-1648069625963-ba32600e43f7
- **Telecom Infrastructure**: https://images.pexels.com/photos/33107545/pexels-photo-33107545.jpeg
- **Communication Tower**: https://images.pexels.com/photos/3062229/pexels-photo-3062229.jpeg
- **Hillside Tower**: https://images.unsplash.com/photo-1708481295267-4b1859f4ffc2
- **Cell Tower**: https://images.unsplash.com/photo-1700463108455-956c595bc97b
- **Power Infrastructure**: https://images.unsplash.com/photo-1710906806691-e767d6520525
- **Network Equipment**: https://images.unsplash.com/photo-1563884705074-7c8b15f16295

---

## 🎨 HOW TO REPLACE IMAGES

### Method 1: Direct URL Replacement
1. Open the HTML file containing the image you want to replace
2. Find the image URL (usually in `src=""` or `url()` attributes)
3. Replace the URL with your new image URL
4. Save the file

### Method 2: Using Local Images
1. Create an `assets/images/` folder in your project
2. Place your new image in the folder
3. Update the HTML to reference the local file:
   ```html
   <img src="assets/images/your-new-image.jpg" alt="Description">
   ```

### Example Replacement:
**Before:**
```html
<img src="https://images.unsplash.com/photo-1614366502473-e54666693b44" alt="Solar Energy">
```

**After (with your image):**
```html
<img src="assets/images/spacetric-solar-installation.jpg" alt="Spacetric Solar Installation">
```

---

## 📁 FILE STRUCTURE OVERVIEW

```
/app/spacetric-website/
├── main-pages/
│   └── index.html (Homepage with hero and about images)
├── content/
│   ├── energy/
│   │   └── energy-solutions.html (Energy page with solar images)
│   ├── water/
│   │   └── water-solutions.html (Water page with treatment images)
│   ├── security/
│   │   └── security-solutions.html (Security page - to be created)
│   └── telecom/
│       └── telecom-solutions.html (Telecom page - to be created)
├── assets/
│   ├── images/ (Create this folder for your custom images)
│   ├── logos/ (Create this folder for logos)
│   └── banners/ (Create this folder for banner images)
└── ASSET_INVENTORY.md (This file)
```

---

## 🔍 IMAGE CATEGORIES & PURPOSES

### By Section:
- **Hero Banners**: Large, high-impact background images for page headers
- **Feature Illustrations**: Supporting images for service descriptions
- **Technology Showcase**: Images showing equipment and installations
- **Infrastructure**: Images showing scale and professional installations

### By Quality Requirements:
- **High Resolution**: Hero banners and main section images
- **Medium Resolution**: Service cards and feature illustrations
- **Icon Style**: Simple illustrations for service icons

---

## 💡 TIPS FOR IMAGE REPLACEMENT

### Best Practices:
1. **Maintain Aspect Ratio**: Keep similar dimensions to current images
2. **Professional Quality**: Use high-resolution, professional images
3. **Consistent Style**: Maintain visual consistency across the site
4. **Optimize Size**: Compress images for faster loading
5. **Alt Text**: Update alt text descriptions when changing images

### Recommended Image Sizes:
- **Hero Banners**: 1920x800px or larger
- **Section Images**: 800x400px
- **Service Cards**: 400x300px
- **Icons**: 100x100px

### Color Scheme:
- **Primary**: #0066cc (Blue)
- **Secondary**: #00a86b (Green)
- **Accent**: #ff6b35 (Orange)
- **Water Theme**: #0077be (Water Blue)

---

## 📞 NEED HELP?

If you need assistance with:
- Image replacement
- File organization  
- Technical modifications
- Custom design work

Contact your development team or refer to the HTML files directly for specific implementation details.

---

**Last Updated**: January 2025
**Website Version**: Spacetric v1.0
**Total Images Catalogued**: 25+